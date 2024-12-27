### Current progress：
inverse method 从age ele数据求解 exhumation rates
利用exhumation rates和nangs方法完成对微分方程的求解得到T
### todo:
利用神经网络输入T得到model parameter covariance matrix，C
### Installation

    conda install mamba
    mamba create -n LIMN python=3.12 cmake=3.14.0
    mamba activate LIMN
    #安装torch
    mamba install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia
    #安装项目依赖
    pip insatll -r requirement.txt
    
### Testing

inverse_method.ipynb 利用现有数据集测试inverse_method 
solve_temprature.ipynb 利用nangs求解温度方程得到Tm(t,z)