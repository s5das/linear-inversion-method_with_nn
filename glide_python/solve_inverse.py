import numpy as np
from scipy.linalg import lu_factor, lu_solve, inv

def solve_inverse(matrices, params):
    sigmaD = 0.2
    
    # Compute Y2 = CA'
    matrices.Y2 = matrices.cov @ matrices.G.T
    
    # Compute Y1 = GCG' + Cee
    matrices.Y1 = matrices.G @ matrices.Y2
    np.fill_diagonal(matrices.Y1, matrices.Y1.diagonal() + sigmaD**2)
    
    lu, piv = lu_factor(matrices.Y1)
    matrices.Y1 = lu_solve((lu, piv), np.eye(params.n))
    
    # Compute H = GA'Y1^(-1)
    matrices.Y2 = matrices.G.T @ matrices.Y1
    
    # Compute apriori age
    matrices.zz = np.log(matrices.zc + matrices.elev) - np.log(matrices.A @ matrices.edot_pr)
    
    # Compute BB = Y2 * zz
    matrices.BB = matrices.Y2 @ matrices.zz
    
    matrices.edot = np.exp(np.log(matrices.edot_pr) + matrices.BB)
    
    matrices.H = matrices.cov @ matrices.Y2
    matrices.edot_dat = np.exp(np.log(matrices.edot_pr) + matrices.H @ matrices.zz)
    
    print(f"edot min/max at data points: {matrices.edot_dat.min()} / {matrices.edot_dat.max()}")
    
    matrices.edot_pr = matrices.edot_dat