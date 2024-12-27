## Current progress：
1. inverse method 从age ele数据求解 exhumation rates（Beta）

2. 利用exhumation rates和nangs方法完成对微分方程的求解得到T

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

* solve_temprature.ipynb 利用nangs求解温度方程得到Tm(t,z)

## todo:
1. 修正inverse_method中数据集使用问题
1. 利用神经网络输入T得到model parameter covariance matrix，C