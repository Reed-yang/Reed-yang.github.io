---
title: "ViT"
date: 2023-04-16T10:34:20+00:00
tags: ['papereading']
---
划分Patch：为了减少序列长度，按像素计算长度过长，将16x16的Patch作为一个元素，生成序列

Transformer vs. CNN: Transformer相比卷积缺少归纳偏置(inductive biases, 先验知识或者先验假设)

- CNN的inductive biases
  1. Locality 局部性
  2. translation equivalence 平移不变性

Transformer在大规模数据集上预训练，可以达到归纳偏置d
