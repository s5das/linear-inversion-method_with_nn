import numpy as np

def closure_temps(cooling, temp, iflag):
    mz = len(cooling)
    closure = np.zeros(mz)
    
    energy_values = {
        1: 147e3,
        2: 208e3,
        3: 138e3,
        4: 169e3,
        5: 268e3,
        6: 180e3,
        7: 197e3,
    }
    diff_values = {
        1: 2.05e6 * 3600 * 24 * 365.25e6,
        2: 4.0e8 * 3600 * 24 * 365.25e6,
        3: 7.64e7 * 3600 * 24 * 365.25e6,
        4: 7.03e5 * 3600 * 24 * 365.25e6,
        5: 1320 * 3600 * 24 * 365.25e6,
        6: 3.91 * 3600 * 24 * 365.25e6,
        7: 733 * 3600 * 24 * 365.25e6,
    }
    
    energy = energy_values.get(iflag, 147e3) / (4.184 * 1e3)
    geom = 1.0
    diff = diff_values.get(iflag, 2.05e6 * 3600 * 24 * 365.25e6)
    r = 8.314
    
    cooling = np.maximum(cooling, 1.0 / 10.0)
    tau = r * (temp + 273.0) ** 2 / (energy * cooling)
    closure = energy / r / np.log(geom * tau * diff) - 273.0
    
    return closure

def tridag(a, b, c, r):
    n = len(r)
    u = np.zeros(n)
    gam = np.zeros(n)
    
    if b[0] == 0:
        raise ValueError("tridag failed: b[0] cannot be zero")
    
    bet = b[0]
    u[0] = r[0] / bet
    
    for j in range(1, n):
        gam[j] = c[j - 1] / bet
        bet = b[j] - a[j] * gam[j]
        if bet == 0:
            raise ValueError("tridag failed")
        u[j] = (r[j] - a[j] * u[j - 1]) / bet
    
    for j in range(n - 2, -1, -1):
        u[j] -= gam[j + 1] * u[j + 1]
    
    return u

def find_zc(matrices, params):
    mz = 131
    dz = params['zl'] / (mz - 1)
    
    temp = np.zeros(mz)
    temp2 = np.zeros(mz)
    
    diag = np.zeros(mz)
    sup = np.zeros(mz)
    inf = np.zeros(mz)
    f = np.zeros(mz)
    temp_pr = np.zeros(mz)
    temp_age = np.zeros(mz)
    tdot = np.zeros(mz)
    closure = np.zeros(mz)
    
    dt = 0.5 * (dz ** 2) / params['kappa']
    tstart = 0.0
    tend = params['t_total']
    temp[:] = np.linspace(params['Ts'], params['Tb'], mz)
    
    xtime = tstart
    
    while xtime < tend:
        lambda_ = params['kappa'] * dt / (2.0 * dz ** 2)
        exhum = np.interp(xtime, matrices['tsteps_sum'], matrices['edot_dat'])
        alpha = exhum * dt / (4.0 * dz)
        
        ax = alpha - lambda_
        bx = 1 + 2 * lambda_
        cx = - (lambda_ + alpha)
        
        for i in range(1, mz - 1):
            diag[i] = bx
            sup[i] = cx
            inf[i] = ax
            f[i] = (lambda_ - alpha) * temp[i - 1] + (1 - 2 * lambda_) * temp[i] + (lambda_ + alpha) * temp[i + 1] + params['hp'] * dt
        
        diag[0] = diag[-1] = 1.0
        f[0] = params['Ts']
        f[-1] = temp[-2] + (temp[-1] - temp[-2])
        
        temp = tridag(inf, diag, sup, f)
        xtime += dt
    
    for i in range(mz - 1):
        tdot[i] = (temp_age[i] - temp_pr[i] + (temp_pr[i + 1] - temp_pr[i]) * dz) / dt
    
    closure = closure_temps(tdot, temp_age, matrices['isys'])
    
    for i in range(mz - 1):
        if temp_age[i] > closure[i]:
            M = dz / (closure[i] - closure[i - 1])
            P = dz / (temp_age[i] - temp_age[i - 1])
            Tc = (M * closure[i - 1] - P * temp_age[i - 1]) / (M - P)
            xjunk = M * (Tc - closure[i])
            matrices['zc'] = dz * (i - 1) + xjunk
            break
