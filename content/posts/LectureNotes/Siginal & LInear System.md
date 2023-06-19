---
title: Signal&LinearSystem
author: Reed
time: 2023/6/11
category: LectureNotes
---

## Ch.1 绪论

### 信号

周期信号

信号的平均功率

<img src="http://img.reedyoung.cn/image-20230410210537473.png" alt="image-20230410210537473" style="zoom:50%;" />

能量信号与功率信号：

<img src="http://img.reedyoung.cn/image-20230410210624353.png" alt="image-20230410210624353" style="zoom:50%;" />

### 系统

What is a System?

<img src="http://img.reedyoung.cn/image-20230410211139200.png" alt="image-20230410211139200" style="zoom: 25%;" />

<img src="http://img.reedyoung.cn/image-20230410211204338.png" alt="image-20230410211204338" style="zoom: 25%;" />

线性系统与非线性系统

​	线性系统：就是具有齐次性和叠加性的系统

零输入响应和零状态响应

<img src="http://img.reedyoung.cn/image-20230410213753029.png" alt="image-20230410213753029" style="zoom:33%;" />

时不变系统：响应形状不随激励的施加时间而改变

<img src="http://img.reedyoung.cn/image-20230610114750467.png" alt="image-20230610114750467" style="zoom: 33%;" />

因果系统：响应不早于激励的系统

<img src="http://img.reedyoung.cn/image-20230610114818015.png" alt="image-20230610114818015" style="zoom:50%;" />

## Ch.2 连续系统的时域分析

线性时不变系统的数学模型 $\rightarrow$ 线性常系数微分方程

<img src="http://img.reedyoung.cn/image-20230610121940634.png" alt="image-20230610121940634" style="zoom: 33%;" />

经典法：<img src="http://img.reedyoung.cn/image-20230610122013554.png" alt="image-20230610122013554" style="zoom: 33%;" />



### ZIR / ZSR 方法：

<img src="http://img.reedyoung.cn/image-20230610124611825.png" alt="image-20230610124611825" style="zoom:33%;" />

算子表示法 转移算子

<img src="http://img.reedyoung.cn/image-20230610125749485.png" alt="image-20230610125749485" style="zoom:50%;" />

算子的性质

1. p多项式可以展开和因式分解
2. <img src="http://img.reedyoung.cn/image-20230610125924938.png" alt="image-20230610125924938" style="zoom:33%;" />
3. <img src="http://img.reedyoung.cn/image-20230610130044723.png" alt="image-20230610130044723" style="zoom: 25%;" />
4. <img src="http://img.reedyoung.cn/image-20230610130103824.png" alt="image-20230610130103824" style="zoom:25%;" />

零状态 vs 零输入：

<img src="http://img.reedyoung.cn/image-20230610143523245.png" alt="image-20230610143523245" style="zoom: 33%;" />

零输入响应求解：与齐次通解求法相同，待定系数直接由初始条件求出

奇异函数：

- 单位斜变 $R(t)$
- 单位阶跃 $ \varepsilon(t) / u(t)$
- 方波(门函数) $G(t)$
- 单位冲激 
- 冲击偶信号

单位冲激响应$h(t)$

​	通过单位冲激响应来判断系统的因果性

单位阶跃响应$r_\epsilon(t)$

<img src="http://img.reedyoung.cn/image-20230610141133231.png" alt="image-20230610141133231" style="zoom:25%;" />

求单位冲激响应

<img src="http://img.reedyoung.cn/image-20230610142406236.png" alt="image-20230610142406236" style="zoom: 33%;" />

<img src="http://img.reedyoung.cn/image-20230610142524528.png" alt="image-20230610142524528" style="zoom:33%;" />

即：求$D(p)h_0(t)=\delta(t)$时，按照$D(p)h_0(t)=0$和附加的初始条件来求零输入即可

例题：

<img src="http://img.reedyoung.cn/image-20230610144747373.png" alt="image-20230610144747373" style="zoom:25%;" />

### 转移算子 部分分式

冲激响应：部分分式分解法，对转移算子$H(p)$分解

简单系统：

1. <img src="http://img.reedyoung.cn/image-20230610145001629.png" alt="image-20230610145001629" style="zoom: 33%;" />
2. <img src="http://img.reedyoung.cn/image-20230610145019359.png" alt="image-20230610145019359" style="zoom: 25%;" />
3. <img src="http://img.reedyoung.cn/image-20230610145049144.png" alt="image-20230610145049144" style="zoom: 25%;" />

一些零状态响应的激励 / 响应对照：

<img src="http://img.reedyoung.cn/image-20230610151024742.png" alt="image-20230610151024742" style="zoom:33%;" />

### 卷积

<img src="http://img.reedyoung.cn/image-20230610151414875.png" alt="image-20230610151414875" style="zoom:33%;" />

卷积的图解法：

<img src="http://img.reedyoung.cn/image-20230610151514889.png" alt="image-20230610151514889" style="zoom: 25%;" />

**卷积的性质**：

<img src="http://img.reedyoung.cn/image-20230610152017540.png" alt="image-20230610152017540" style="zoom:33%;" />

卷积的微分与积分：

<img src="http://img.reedyoung.cn/image-20230610152106852.png" alt="image-20230610152106852" style="zoom:33%;" />

常用公式：(当有一函数可化为冲击函数时)
$$
f_{1}(t) * f_{2}(t)=\frac{d f_{1}(t)}{d t} * \int_{-\infty}^{t} f_{2}(\tau) d \tau
$$
奇异信号的卷积特性:

<img src="http://img.reedyoung.cn/image-20230610152137671.png" alt="image-20230610152137671" style="zoom:33%;" />

零输入响应 零状态响应

自然相应	受迫响应

瞬态响应	稳态响应...

## Ch.3 连续信号的正交分解

### 函数的正交

<img src="http://img.reedyoung.cn/image-20230610163759328.png" alt="image-20230610163759328" style="zoom:33%;" />

常见的完备正交函数集

<img src="http://img.reedyoung.cn/image-20230610164046350.png" alt="image-20230610164046350" style="zoom: 25%;" />

### 傅里叶级数

### 傅里叶积分 $ \rightarrow $ 傅里叶变换

<img src="http://img.reedyoung.cn/image-20230610171409405.png" alt="image-20230610171409405" style="zoom:33%;" />

傅里叶变换式：

- 单边指数函数：

  <img src="http://img.reedyoung.cn/image-20230610171526147.png" alt="image-20230610171526147" style="zoom: 25%;" />

- 双边指数信号

  <img src="http://img.reedyoung.cn/image-20230610171936192.png" alt="image-20230610171936192" style="zoom:25%;" />

- 单位冲激：
  $$
  \delta(t) \leftrightarrow 1
  $$

- 

傅里叶变换的特性：

- 线性特性：略
- 延时特性

<img src="http://img.reedyoung.cn/image-20230610174604195.png" alt="image-20230610174604195" style="zoom:33%;" />

- 移频

<img src="http://img.reedyoung.cn/image-20230610174617626.png" alt="image-20230610174617626" style="zoom:33%;" />

- 尺度变换

<img src="http://img.reedyoung.cn/image-20230610174628790.png" alt="image-20230610174628790" style="zoom:33%;" />

- 奇偶

<img src="http://img.reedyoung.cn/image-20230610174652559.png" alt="image-20230610174652559" style="zoom: 25%;" />

- 对称

<img src="http://img.reedyoung.cn/image-20230610174712855.png" alt="image-20230610174712855" style="zoom:33%;" />

- 微分：

<img src="http://img.reedyoung.cn/image-20230610174816378.png" alt="image-20230610174816378" style="zoom:33%;" />

- 积分

<img src="http://img.reedyoung.cn/image-20230610174830981.png" alt="image-20230610174830981" style="zoom:33%;" />

卷积定理：

<img src="http://img.reedyoung.cn/image-20230610174850083.png" alt="image-20230610174850083" style="zoom:33%;" />

Parseval's定理

<img src="http://img.reedyoung.cn/image-20230610175002582.png" alt="image-20230610175002582" style="zoom: 50%;" />







## Ch.4 连续时间系统的频域分析

### 频域分析法与系统函数

<img src="http://img.reedyoung.cn/image-20230610190838795.png" alt="image-20230610190838795" style="zoom:33%;" />
$$
\Rightarrow
$$
<img src="http://img.reedyoung.cn/image-20230610190909300.png" alt="image-20230610190909300" style="zoom: 50%;" />

频域分析步骤：

<img src="http://img.reedyoung.cn/image-20230610191007922.png" alt="image-20230610191007922" style="zoom: 33%;" />







## Ch.5 连续时间系统的复频域分析

拉普拉斯变换

与傅里叶变换的关系？

- 单边拉普拉斯变换：拉普拉斯变换指的是单边变换，变换下限从$0^{-}$开始

- 常见信号的拉普拉斯变换

<img src="http://img.reedyoung.cn/image-20230610224956287.png" alt="image-20230610224956287" style="zoom:33%;" />

- 性质

<img src="http://img.reedyoung.cn/image-20230610214009307.png" alt="image-20230610214009307" style="zoom: 67%;" />

拉普拉斯逆变换

- 留数法

- 部分分式展开法

<img src="http://img.reedyoung.cn/image-20230610213856946.png" alt="image-20230610213856946" style="zoom:33%;" />

系统函数

初值定理和终值定理的要点：

<img src="http://img.reedyoung.cn/image-20230610224438852.png" alt="image-20230610224438852" style="zoom: 33%;" />

画图，把n导数和系数的画法背下来





## Ch.6 连续时间系统的系统函数

### 极零点

### z-p点分布与频响特性

<img src="http://img.reedyoung.cn/image-20230610235940529.png" alt="image-20230610235940529" style="zoom:33%;" />

### 线性系统的稳定性

对于任何有界的输⼊，其响应也是有界的。

<img src="http://img.reedyoung.cn/image-20230611001202393.png" alt="image-20230611001202393" style="zoom:33%;" />

## Ch.7 离散时间系统的时域分析

理想抽样

香农取样定理

离散信号

- 单位阶跃序列
- 矩形序列
- 指数序列
- 正弦序列
- 复指数序列

离散信号的变换和运算

<img src="http://img.reedyoung.cn/image-20230611004805213.png" alt="image-20230611004805213" style="zoom: 33%;" />

移序算子

<img src="http://img.reedyoung.cn/image-20230611005004196.png" alt="image-20230611005004196" style="zoom:25%;" />

<img src="http://img.reedyoung.cn/image-20230611005029896.png" alt="image-20230611005029896" style="zoom: 33%;" />

差分算子

典型序列的差分：类似于求导

连续和离散之间的近似：

<img src="http://img.reedyoung.cn/image-20230611005300073.png" alt="image-20230611005300073" style="zoom:50%;" />

离散时间系统用差分方程来描述

线性移不变离散时间系统

<img src="http://img.reedyoung.cn/image-20230611005732966.png" alt="image-20230611005732966" style="zoom:50%;" />

### 常系数差分方程求解

<img src="http://img.reedyoung.cn/image-20230611010147720.png" alt="image-20230611010147720" style="zoom:33%;" />

迭代法

经典法：特征根，通解+特解

通解：

<img src="http://img.reedyoung.cn/image-20230611011456824.png" alt="image-20230611011456824" style="zoom:33%;" />

特解：

<img src="http://img.reedyoung.cn/image-20230611011150457.png" alt="image-20230611011150457" style="zoom: 33%;" />

ZIR / ZSR 方法：

零输入：由初始条件求得的齐次解

离散时间系统的单位样值响应：

<img src="http://img.reedyoung.cn/image-20230611011704774.png" alt="image-20230611011704774" style="zoom:33%;" />

求$h(n)$关键在于，在n=0时将接入的激励转化为起始条件，即x(0), x(-1)..的值





---

## questions

- <img src="http://img.reedyoung.cn/image-20230610114115154.png" alt="image-20230610114115154" style="zoom:33%;" />

- ![image-20230610171837662](http://img.reedyoung.cn/image-20230610171837662.png)

  什么是相频？

- 冲激响应为什么和零输入响应这么像？

- 