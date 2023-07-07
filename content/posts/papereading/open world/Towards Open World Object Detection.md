---
title: "Towards Open World Object Detection"
date: 2022-09-23T13:28:51+00:00
tags: ['papereading', 'open world']
---
论文链接：

### Abstract

提出：

- Open World Object Detection 问题
  1.  模型能够在无明确监督的情形下将无标签物体识别为'unknown'
  1.  当逐步输入相应的标签时，能够学习到已识别的'unknown'类别中去

- <u>O</u>pen Wo<u>r</u>ld Object D<u>e</u>tector ORE

  基于**Contrastive clustering**和**Energy based unknown identification**

发现：

- we find that identifying and characterising unknown instances helps to reduce confusion in an incremental object detection setting, where we achieve state-ofthe-art performance, with no extra methodological effort.

  我们发现识别和表征未知实例有助于减少incremental object detection设置中的混淆，在这种设置中我们实现了SOTA，而无需额外的方法论。

### Intro

<img src="http://img.reedyoung.cn/image-20220923140021014.png" alt="image-20220923140021014" style="zoom: 67%;margin: 0 auto;" />

问题对比：

- <u>Open set learning / Incremental Learning / Open world object Detection</u> 

### 方法

- ORE

  - Faster R-CNN 作为detector

    ROI(region of interest) pooling

    region proposal network

  - contrastive learning

  - auto-labelling unknowns with RPN

  - Energy Based Unknown Identifier

  - Alleviating Forgetting

---

**question**

- [ ] 关于Faster R-CNN

  RPN 的作用

- [ ] 为什么faster r-cnn 比其他识别算法对open set效果好

- [x] 数据泄露

  后续工作有改进，所以不必太关注实验数据

- [x] 几个子任务的对比：

  Incremental Obeject Detection

  Open world classification

  Open set classification

  Open set detection

   --其实与之前的工作没有太显著的区别，但是把不同角度的任务进行了综合，进而提出了Open World

- [ ] EBM energy based model

  以 熵 的角度理解，用来描述概率分布

- [x] 为什么能把背景识别为背景，而unknown不是背景？

  在大数据集上预训练
