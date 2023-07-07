---
title: "Research_proc"
date: 2023-04-28T09:46:39+00:00
tags: ['uncategorized']
---
- [x] install ST 环境
- [ ] 跑 ST 代码

### ST环境

运行clash：需要保持terminal

```bash
cd ~/clash
./clash -d .
```

`pandas` incompatible with `numpy`

```bash
ImportError: this version of pandas is incompatible with numpy < 1.20.3
your numpy version is 1.19.5.
Please upgrade numpy to >= 1.20.3 to use this pandas version
```

-->installed `pandas == 1.3.5`

cuda==11.1 for **torch_sparse couldn't match with torch before**

torch 检测不到gpu，但nvcc -V版本显示11.1

已经拷贝cudnn

### ST Debug

可以运行

### Opwd

<img src="http://img.reedyoung.cn/image-20230523130759850.png" alt="image-20230523130759850" style="zoom:50%;margin: 0 auto;" />

What am I doing right now?

- 搞清楚ST的输出形式，如何与OpenSeg拼接起来 **opwd line 527**

---

实现三种方法的对比实验: This Three all uncerntainty-based methods

![image-20230526215551842](http://img.reedyoung.cn/image-20230526215551842.png)

### MSP in 

- What is MSP: Maximum Softmax Probability
- The uncertainty-based methods also work poorly as we find the network predicts the novel classes as old classes with high confidence scores：![image-20230527144034767](http://img.reedyoung.cn/image-20230527144034767.png)

---

- 实现ST + MSP

  - st-opwd源码分析
    - upsamples 和 memorycell的区别，为何并列使用
    - memorycell具体用途分析，为什么这样构造网络
    - 是怎么实现MSP计算的

- 读MSP论文

  - **blog: [A Simple Adjustment Improves Out-of-Distribution Detection for Any Classifier](https://pub.towardsai.net/a-simple-adjustment-improves-out-of-distribution-detection-for-any-classifier-5e96bbb2d627)**

    <img src="http://img.reedyoung.cn/image-20230531152954215.png" alt="image-20230531152954215" style="zoom: 67%;margin: 0 auto;" />

    they do not explicitly estimate epistemic uncertainty

    ***class confident thresholds*:** 

    <img src="http://img.reedyoung.cn/image-20230531154153993.png" alt="image-20230531154153993" style="zoom: 80%;margin: 0 auto;" />

  - Paper: A Baseline for Detecting Misclassified and OOD Examples in Neural Networks

    - Precision: 查准率，就是正确率(实际上意味着：pred=1时，label=1的概率)
    - Recall: 查全率，Recall = 1意味着 **label = 1时，pred = 1概率为1**
    - AUROC / AUPR 阈值无关

### REAL

- RCs: add several redundancy classifiers (RCs) on the basis of the original network to predict the probability of the unknown class

- Train: training strategies for the OSeg and IL tasks under REAL, based on the unknown object synthesis, predictive distribution calibration, and pseudo label generation

![image-20230701110453228](http://img.reedyoung.cn/image-20230701110453228.png)

主要的修改应该集中在

1. train.py 模型结构和前向方法
2. 损失计算和指标评估

---

- [x] copy a model
- [x] 写标签代码
- [x] SigleUnkFullTrainMSP4GPUs

---

## Tips

- pycharm 中 `tensor().cpu().numpy()`可以更方便查询tensor的值
- tensorboard要在文件目录中查看，通过`ssh -L 8008:localhost:8008 docker@172.16.3.105 -p 322`端口映射到本地
- 关于tmux, click [here](http://louiszhai.github.io/2017/09/30/tmux/)

---

## Questions

23.6.1

- MemoryCell 用途？
- 如果AUROC / AUPR阈值无关，那么计算MSP的意义是什么？并没有改变分类器本身
- MSP 简读过，了解了AUROC / AUPR的原理和用途，这篇文章主要贡献是提出评价指标，在方法上MSP更多是简单的直觉(但也足够有效)，还有很多改进空间？师兄的新方法是什么？
- 关于OOD的blog，可以简单看一看，基于Class Confident Thresholds
- 怎么使用已经训练好的模型计算MSP AUPR

23.6.13

- OOD样本的选取会不会对aupr / auroc等评测指标的分数有很大影响；如何标准化

23.7.1

- <img src="http://img.reedyoung.cn/image-20230701153156986.png" alt="image-20230701153156986" style="zoom: 80%;margin: 0 auto;" />

  这张图怎么看？

- 

可以用meshlab可视化.ply文件

抓紧时间做REAL的实验

有时间可以重新训练msp的实验：每轮跑train和val的分数，尝试多卡

maxlogits和mcdropout优先级最后

---

## Errors

- **ATen/native/cuda/ScatterGatherKernel...**

  <img src="http://img.reedyoung.cn/1414d0ed6e47d8fa62865dfcfe273ba.png" alt="1414d0ed6e47d8fa62865dfcfe273ba"  />

pytorch 相关包导入会影响对torch.device的设置，也即在指定`os.environ["CUDA_VISIBLE_DEVICES"]`之前导入相关包可能会触发提前设置device

的bug，由于该bug可能导致后续对device的设置无效；最简单的方法是在`import os`后直接设置`os.environ["CUDA_VISIBLE_DEVICES"]`，或者在需要使用包时再进行导入，以免提前导入触发bug
