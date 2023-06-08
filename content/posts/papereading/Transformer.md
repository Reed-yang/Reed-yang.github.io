---
title: "Transformer"
---
论文阅读顺序：

1. 标题+作者
2. 摘要
3. 结论
4. 导言
5. 相关工作
6. 模型
7. 实验
8. 评论



Multi-headed Attention: 为了模拟CNN可以达到多通道输出

### Model Architecture

自回归模型

​	：(对于decoder)过去时刻的输出也会作为当前时刻的输入

<img src="http://img.reedyoung.cn/image-20230411103531006.png" alt="image-20230411103531006" style="zoom: 67%;" />

LayerNorm vs. BatchNorm

​	**Batch**: What is Batch? 一捆Data，以便处理时并行

​	Normalization: 均值化0，方差化1

​	BatchNorm就是对每个Batch(包含了不同的样本)做Normalization

​	LayerNorm就是对每个样本(包含了样本的特征feature)做Normalization

<img src="http://img.reedyoung.cn/image-20230411122954746.png" alt="image-20230411122954746" style="zoom: 25%;" />

Attention & Multi-Head 计算图：

<img src="http://img.reedyoung.cn/image-20230411132642454.png" alt="image-20230411132642454" style="zoom: 50%;" />

关注Attention算法：Key-Value pair 的作用，与Query对权重的影响

FFN: = MLP

Positional Encoding: 处理使Attention能获取时序信息

---

实验：

Dropout: 大量使用，做正则化，Dropout的意义？

---

评论：

Transformer在大数据集上还未出现数据饱和，也即，没有出现过拟合等现象
