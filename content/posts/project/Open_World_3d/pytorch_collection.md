---
title: "pytorch_collection"
---
- ```python
  torch.from_numpy(i)
  ```

  numpy array -> tensor

- ```
  torch.LongTensor
  ```

  torch.tensor 是 32浮点；torch.LongTensor 是 64位整形

- MSE, Mean Squared Error, 均方损失，用于回归模型

  CE, Cross Entropy, 交叉熵，用于分类模型

  Softmax 将数据变换为概率形式

- model.train()方法：训练前调用以启用BatchNorm和dropout

  model.eval()方法：evaluate前调用，关闭BN和dropout；否则会在eval时改变权值

- 
