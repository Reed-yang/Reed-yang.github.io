---
title: "CLIP"
date: 2022-09-21T15:30:47+00:00
tags: ['papereading']
---
[OpenAI CLIP 官方文档](https://openai.com/blog/clip/)

zero-shot 基于图像文本对 学习 语义信号

模型过大，为加速训练采用很多加速技术：[How to Train Really Large Models on Many GPUs](https://lilianweng.github.io/posts/2021-09-25-train-large/)

prompt engineering

作者提出在对比学习中再结合生成式的目标函数，或许可以扩大模型的灵活性，不受限于输入文本数据的标签

主要影响：摆脱了原有训练数据 固定类别 的范式

---

**Question**

- fine-tune / linear porbe

- logistic regression