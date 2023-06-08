---
title: "NTU ML"
---
This note is the lecture note for [李宏毅(NTU) machine learning 2022](https://speech.ee.ntu.edu.tw/~hylee/ml/2022-spring.php)

## Lecture 1:Introduction of Deep Learning

### Preparation

#### Pre1

- 机器学习实际上是通过机器构造一个隐式的函数

- two main function of machine learning
  - Regression: The function outputs a scalar
  - Classification
  - Structured Learning: create something with structure(image, document)
- Label 学习中的真实值$y$（预测值为$\hat{y}$）

​		feature input所蕴含的某种信息

- *Does local minima truly cause the problem?*

#### Pre2

- 多个piecewise linear curve可以逼近任意曲线

  用sigmoid函数表达一个piecewise linear curve

​	<img src="http://img.reedyoung.cn/image-20220915221127215.png" alt="image-20220915221127215" style="zoom: 33%;" />

- epoch与batch

​	<img src="C:\Users\杨思源\AppData\Roaming\Typora	ypora-user-images\image-20220915235644151.png" alt="image-20220915235644151" style="zoom: 33%;" />

### Class Material

#### week1

- Supervised Learning, Self-supervised Learning, RL...

#### pytorch1

## Lecture 2:What to do if my network fails to train

###  Preparation

### Class Material

#### week2

- 模型复杂度model complexity

  $\mathcal{H}$是模型参数可取值的集合，用其元素个数$\left | \mathcal{H} ight |$表示模型复杂度

  <img src="C:\Users\杨思源\AppData\Roaming\Typora	ypora-user-images\image-20220916164234379.png" alt="image-20220916164234379" style="zoom:50%;" />
  
   
