---
title: "train_struct"
date: 2022-10-13T16:42:50+00:00
tags: ['project', 'Open_World_3d']
---
### 常用import

- ```python
  import argparse
  ```

  参数处理

- ```python
  from tqdm import tqdm
  ```

  进度条

- ```python
  from utils.metric_util import per_class_iu, fast_hist_crop
  ```

- ```python
  from dataloader.pc_dataset import get_SemKITTI_label_name
  ```

- ```python
  from builder import data_builder, model_builder, loss_builder
  ```

  buider下三个文件：

  - loss_builder

  - data_builder

  - model_builder

- ```python
  from config.config import load_config_data
  ```

- ```python
  from utils.load_save_util import load_checkpoint
  ```

- ```python
  import spconv
  ```

  spconv, 稀疏卷积库

- 

### train_cylinder_asym_naive

使用 ./train_naive.sh 调用

---

**baseline** 使用open-set 2D semantic segmenattion用于3D作为比较，包括MSP, Maxlogit, and MC-Dropout

**upper bound** 上界设置为使用$\mathcal{K}_0 \cup \mathcal{K}_n $训练的网络

**loss**: 

- Lovasz loss 解决分割问题中类别分布不均匀的问题，[参考](https://blog.csdn.net/libo1004/article/details/118789323)
- wce Weighted cross-entropy (*WCE*) 带权重的交叉熵

​	

---

- [ ] ./config/config.py 中的结构及作用

- [x] 为什么找不到gpu

  注意用`watch nvidia-smi`查看占用

- [x] 在xdocker中运行`nvidia-smi`报错

  权限不足，sudo

- [ ] 能否在一个gpu上运行多个模型(debug时无速度需求，故显存足够即可，不消耗计算资源)

- [x] 保存文件路径设置

  不会创建父级目录，但可以生成目标文件，因此要记得更改至 y_semantic../... 并创建父级目录

- [x] 训练文件运行顺序 / 有无必要运行.sh

  参照readme / 在tmux中运行.sh即可，注意修改yaml

  主要改：num_workers, epoch, 保存参数路径

- [ ] 如何通过 feature extractor 后 再实现 逐点的语义分割？

  pointnet -> pointnet++ -> cylinder3d
