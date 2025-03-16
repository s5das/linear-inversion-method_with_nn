## Current progress：

1. 利用 $exhumation rates$ 和nangs方法完成对微分方程的求解得到 $Tm(t,z)$ 

2. 复现glide by Fox et al. (2014)代码
glide_python文件夹

- find_zc.py 求解zc参数

- solve_inverse 求解edot 和 edot_dat 参数

## Installation

    conda install mamba
    mamba create -n LIMN python=3.12 cmake=3.14.0
    mamba activate LIMN
    #安装torch
    mamba install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia
    #安装项目依赖
    pip insatll -r requirement.txt
    
## Testing

* solve_temprature.ipynb 利用nangs求解温度方程得到 $Tm(t,z)$ 

## glide公式整理
### find_zc

dz mz
temp(mz)
* 三角矩阵方程求解更新temp
$$A \cdot \text { temp }^{n+1}=f$$

f计算相关参数如下：
$$
   \lambda=\kappa \times dt/(2.*(dz**2))\\

  \alpha=e\times dt/(4\times dz)\\
 
   a=(\alpha-\lambda)\\
 
   b=(1+(2\times \lambda))\\
   
   c=-1\times(\lambda+\alpha)\\
$$
* 结合了时间方向的向后差分和空间方向的中心差分，用来计算温度随时间的变化率
$$
\frac{d T}{d t} \approx \frac{T{\mathrm{age}}(z)-T{\mathrm{pr}}(z)}{d t}+\frac{T{\mathrm{pr}}(z+\Delta z)-T{\mathrm{pr}}(z)}{\Delta z} \cdot \frac{\text { tdotdist }}{\Delta z}
$$

* Dodson 方程根具不同system类别定义相关参数
$$
T_{c}=\frac{E_{a}}{R \ln \left(g \tau D_{0} / a^{2}\right)}-273
$$


* 用Tc(z,t)和temp(z,t)交点求解Tc以及zc
$$

M=\frac{d z}{T_{c}(i)-T_{c}(i-1)}\\
P=\frac{d z}{T(i)-T(i-1)}\\
T_{c}=\frac{M T_{c, i-1}-P T_{i-1}}{M-P}

$$


### solve_inverse
1. 数据点x，y

2. 设置虚拟网格x_dummy,y_dummy



 * 计算虚拟网格点处edot
 $$edot = edot_pr + Cmm\times G'(ACG'+Cee) (log(Zc) - log(Aedot_pr))$$
  $$G(i, j)=\frac{\exp \left(\varepsilon_{j}\right) \Delta t}{z_{c, j}}$$

$$C_{M}(\mathrm{i}, \mathrm{j})=\sigma^{2} \exp \left(-\left(\frac{d}{L}\right)^{2}\right)$$
* 计算数据点处
$$
H = GA'(GCG'+Cee)
$$
$$
edot=H\times (zc-ta\times exp(espilon))
$$

## Todo:
