# 创建环境

```
source <conda root path>/etc/profile.d/conda.sh
conda create -n pytorch python=3.10
conda activate pytorch
conda env list
conda list
conda config --show-sources
conda remove  --name  env_name  --all
```

### 1、中科院镜像
```
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/msys2/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/bioconda/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/menpo/
conda config --set show_channel_urls yes
```

### 2、清华镜像
```
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/tensorflow/linux/cpu/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
conda config --set show_channel_urls yes
```

### 3、查看conda设置
```
conda config --show
```
查看镜像源
```
conda config --show channels
```
将以上配置文件写在，查看命令  ~/.condarc中 vim ~/.condarc

### 4、还原所有镜像
```
conda config --remove-key channels
```

## pip源
```
https://pypi.tuna.tsinghua.edu.cn/simple
https://mirrors.aliyun.com/pypi/simple/
https://mirrors.163.com/pypi/simple/  

pip install torch==1.8.1 -i https://mirrors.aliyun.com/pypi/simple/
```

## 将项目导入github
```shell
git init     # 把项目初始化,相当于在项目的跟目录生成一个 .git 目录
git add .    # 把项目的所有文件加入暂存区
git commit -am '项目初始化'     # 把项目提交到本地仓库，引号里面的是这次提交的注释，方便以后查看。
git remote rm origin  # 先删除远程 Git 仓库
git remote add origin https://github.com/BobinYang/   #为本地的仓库创建一个远程仓库. 例如：git remote add origin https://github.com/BobinYang/HtmlAgilityPackSample.git
git pull --rebase origin master  # 把远端仓库中的代码 拉到本地进得合并一下。
```

cv2安装
```shell
pip install opencv-python
```



conda config --set show_channel_urls yes  
vim ~/.condarc
```shell 
channels:
  - defaults
show_channel_urls: true
default_channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
custom_channels:
  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch-lts: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  simpleitk: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud

```
清除索引缓存
conda clean --all --yes  
conda clean -i

```angular2html
创建虚拟环境：conda create -n 环境名称 python=版本号
查看已有虚拟环境：conda env list
激活虚拟环境：conda activate 环境名称
删除虚拟环境：conda remove -n 环境名称 --all
查看当前环境下已安装的包：conda list
导出当前环境下的包：conda env export > environment.yml
根据导出的包安装环境：conda env create -f environment.yml
安装包：conda install 包名
安装下载到本地的包：conda install --use-local  包路径
卸载当前环境下包：conda uninstall 包名
卸载指定虚拟环境中的包：conda remove --name 环境名称 包名
```