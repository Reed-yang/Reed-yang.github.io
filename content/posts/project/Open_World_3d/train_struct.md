---
title: "train_struct"
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

**upper bound** 上界设置为使用$\mathcal{K}_0 