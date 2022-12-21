# EZseqView

EZseqView is a pipeline for RNA-seq analyze and gene structure visualization

## 设计思路
当前转录组分析最常见的套路是“基因--转录本表达量-- 生物性状统计学相关性”分析流程。这类分析流程相当成熟，却经常出现组学研究的假阳性或假阴性，无法使用分子生物学手段复现。  
在此提出一个“基因--转录本表达量--生物性状相关性--蛋白三维结构预测--蛋白互作预测--蛋白与生物性状相关性”分析流程，一方面借助成熟的“基因表达-生物性状”相关性算法获取在生物性状变化中起主导地位的枢纽基因，另一方面借助新型的高准确度蛋白三维结构预测算法和蛋白结构域互作模拟算法，计算获取枢纽基因的蛋白与其下游调控蛋白的互作关系，规避当前蛋白组、代谢组和DAP-seq等技术无法全面反应蛋白与生物性状相关性的缺陷，同时输出基因表达量趋势图、基因表达相关性图、蛋白三维结构预测模型和蛋白互作三维模型等一系列可视化结果。由于AlphaFold2等高准确度蛋白三维结构预测算法的兴起，这一以计算为主的研究思路成为可能，实验验证当前已经能实现“基因--转录本表达量--生物性状相关性--蛋白三维结构预测”步骤的自动化，然而当前分子模拟等手段不能批量自动化实现从蛋白结构到蛋白互作预测的结果，每一个蛋白互作模型都必须手动预设参数与蛋白模型，致使上述计算研究思路只能实现从基因序列到枢纽基因三维结构的“端到端”效果，后续研究工作仍需手动设置运行。

## 使用前的准备
由于pipeline中包含对bash脚本的调用，当前暂不支持 win/macos 系统直接使用该程序。建议win/macos用户通过WSL和虚拟机生成Linux虚拟环境后，在虚拟环境内部运行该程序。  

建议的运行配置：  
| 组件  |           配置详情            |
| :---: | :---------------------------: |
|  CPU  |        16 core 及以上         |
|  RAM  |          64GB 及以上          |
|  GPU  | Volta及之后架构，显存10GB以上 |

### 安装容器基本运行环境（Linux）
1. 安装[Docker](https://www.docker.com/)或其余支持[OCI](https://opencontainers.org/)接口的容器引擎
   * 安装NVIDIA驱动（可选）
   * 安装容器NVIDIA支持（[NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html)，可选）
   * 设置容器以[非根用户模式](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user)运行
   * 测试NVIDIA驱动（可选）  
  
    ```bash
    docker run --rm --gpus all nvidia/cuda:11.0-base nvidia-smi
    ```
2. 从[docker hub ](https://hub.docker.com/)下载容器
   ```bash
   docker push aspreadfire/$packagename:$tagname 
   ```
   或使用dockerfile从头构建容器
   ```bash
   docker build -f $dockerfilename -t $contianer_name . 
   ```
3. 设置[conda](https://docs.conda.io/en/latest/)基础环境  
   ```bash
   conda create -n ezseqview -y 
   ```
   激活环境并下载python
   ```bash
   conda activate ezseqview | conda install python=3.9 -y 
   ```
   
# 快速开始
1. 克隆本项目至工作路径，并`cd`进入工作路径
```bash
   git clone https://github.com/Aspreadfire/EZseqView.git 
```
2. 安装python依赖
```bash
  pip install -r requirement.txt 
```  
3. 运行EZSeqView
```bash
  python ez_seq_view.py 
``` 
程序将以CLI面板的方式引导用户进行基础参数配置和流程配置
# TO DO
容器环境自动安装  
更丰富的CLI面板配置选项  
前端接口，用以提供网页面板支持
