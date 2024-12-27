## Current progress：
1. inverse method 利用 $age$ 以及 $ele$ 数据求解 $exhumation rates$（Beta）

2. 利用 $exhumation rates$ 和nangs方法完成对微分方程的求解得到 $Tm(t,z)$ 

## Installation

    conda install mamba
    mamba create -n LIMN python=3.12 cmake=3.14.0
    mamba activate LIMN
    #安装torch
    mamba install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia
    #安装项目依赖
    pip insatll -r requirement.txt
    
## Testing

* inverse_method.ipynb 利用现有数据集测试inverse_method 

* solve_temprature.ipynb 利用nangs求解温度方程得到 $Tm(t,z)$ 

## Todo:
1. 修正inverse_method中数据集使用问题
1. 利用神经网络输入 $T(t,z)$ 得到model parameter covariance matrix，  $C$ 