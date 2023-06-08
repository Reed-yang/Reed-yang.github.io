---
title: "Linear_Algebra_HUST"
---
- [Ch1 行列式](#ch1-行列式)
  - [一些定义](#一些定义)
  - [行列式的性质](#行列式的性质)
  - [行列式的计算](#行列式的计算)
  - [Cramer法则](#cramer法则)
- [Ch2 矩阵](#ch2-矩阵)
  - [(行列式的)一些性质](#行列式的一些性质)
  - [$A^{T}$的性质](#at的性质)
  - [可逆矩阵](#可逆矩阵)
  - [通过$A^\*$求$A^{-1}$](#通过a求a-1)
  - [逆矩阵的性质](#逆矩阵的性质)
  - [分块矩阵](#分块矩阵)
  - [矩阵的初等变换](#矩阵的初等变换)
  - [矩阵的秩](#矩阵的秩)
- [Ch3 向量](#ch3-向量)
  - [运算](#运算)
  - [向量组的线性相关性](#向量组的线性相关性)
  - [向量组的极大线性无关组](#向量组的极大线性无关组)
  - [向量空间](#向量空间)
  - [Euclidean空间 $\mathbb{R}^n$](#euclidean空间-mathbbrn)
- [Ch4 线性方程组](#ch4-线性方程组)
  - [Gauss 消元法](#gauss-消元法)
  - [齐次方程组解的结构](#齐次方程组解的结构)
  - [非齐次方程组解的结构](#非齐次方程组解的结构)
- [Ch5 相似矩阵](#ch5-相似矩阵)
  - [特征向量与特征值](#特征向量与特征值)
  - [特征向量的性质](#特征向量的性质)
  - [相似矩阵对角化](#相似矩阵对角化)
  - [应用：一阶齐次线性常系数微分方程组](#应用一阶齐次线性常系数微分方程组)
- [Ch6 二次型](#ch6-二次型)
  - [二次型及其矩阵表示](#二次型及其矩阵表示)
  - [标准形、规范形](#标准形规范形)
  - [矩阵合同](#矩阵合同)
  - [正交变换法化二次型为标准形](#正交变换法化二次型为标准形)
  - [几何意义](#几何意义)
  - [二次型的正定性](#二次型的正定性)
  - [Sylvester定理](#sylvester定理)


### Ch1 行列式

#### 一些定义

n阶行列式

n阶行列式的值是一个数

余子式

代数余子式

<img src="http://img.reedyoung.cn/image-20230321102004862.png" alt="image-20230321102004862" style="zoom: 33%;" />

n阶行列式的值的定义(公式)

<img src="http://img.reedyoung.cn/image-20230321102118925.png" alt="image-20230321102118925" style="zoom: 33%;" />

#### 行列式的性质

行列式与其转置的行列式相等：$D^T=D$

​		证明：数学归纳法

数乘：第二类初等变换

行列式的某一行（列）都乘以k，等于用k乘以行列式：

<img src="http://img.reedyoung.cn/image-20230321102810996.png" alt="image-20230321102810996" style="zoom: 33%;" />

​	推论：如果行列式某一行（列）都是0，则行列式为0

交换行列式的两行，行列式反号

​	<span id='ch1_1'>推论：若行列式两行（列）元素对应相等（成比例），行列式值为0</span>

​	推论：行列式任一行的所有元素与另一行对应元素的代数余子式乘积之和等于零

​			证明：放入新行列式$D_1$中，$D_1$有两行元素相同，故$D_1=0$

所以有：

<img src="http://img.reedyoung.cn/image-20230321110457803.png" alt="image-20230321110457803" style="zoom: 33%;" />

拆项：

<img src="http://img.reedyoung.cn/image-20230321110650171.png" alt="image-20230321110650171" style="zoom:33%;" />

第三类初等变换：

<img src="http://img.reedyoung.cn/image-20230321110744108.png" alt="image-20230321110744108" style="zoom:33%;" />

#### 行列式的计算

利用行列式的性质，使得要计算的行列式中有尽可能多的0，从而降阶和简化计算

三角行列式,$D=a_{11}a_{22}...a_{nn}$，只与主对角有关

爪型行列式（P15）

Vandermonde行列式P16

三对角行列式P18



#### Cramer法则

<img src="http://img.reedyoung.cn/image-20230321211808118.png" alt="image-20230321211808118" style="zoom:33%;" />

<img src="http://img.reedyoung.cn/image-20230321211819678.png" alt="image-20230321211819678" style="zoom:33%;" />

证明用到了[定理](#ch1_1)，

齐次方程组的非零解

<img src="http://img.reedyoung.cn/image-20230321222412650.png" alt="image-20230321222412650" style="zoom:33%;" />

### Ch2 矩阵

#### (行列式的)一些性质

矩阵无乘法交换律

矩阵有：结合律、分配律、数乘

矩阵的**行列式**，有性质：
$$
det(kA)=k^ndet(A)
$$


<img src="http://img.reedyoung.cn/image-20230321230032450.png" alt="image-20230321230032450" style="zoom:33%;" />

#### $A^{T}$的性质

**矩阵转置的行列式不变（数学归纳法）** 
$$
\Rightarrow |A^T|=|A|
$$


<img src="http://img.reedyoung.cn/image-20230321230105158.png" alt="image-20230321230105158" style="zoom:33%;" />

$$
r(A^TA)=r(A)=r(A^T)
$$


#### 可逆矩阵

​	可逆矩阵一定是方阵

​	可逆矩阵的逆矩阵是唯一的

证明 $A可逆 \Leftrightarrow det(A)=0$ ：

#### 通过$A^*$求$A^{-1}$

伴随矩阵：$A^*$是$A$每个元素换成其对应的代数余子式，然后取转置得到的矩阵,且有：
$$
A^{-1} = rac{A^*}{det(A)}
$$


<img src="http://img.reedyoung.cn/image-20230322000925109.png" alt="image-20230322000925109" style="zoom:33%;" />

<img src="http://img.reedyoung.cn/image-20230322001716872.png" alt="image-20230322001716872" style="zoom:33%;" />

#### 逆矩阵的性质

<img src="http://img.reedyoung.cn/image-20230322002855321.png" alt="image-20230322002855321" style="zoom: 33%;" />

​		最重要的：$AB = BA$

#### 分块矩阵

​	乘法、逆、转置

​	对角分块矩阵的逆：

<img src="http://img.reedyoung.cn/image-20230322120148524.png" alt="image-20230322120148524" style="zoom:33%;" />

#### 矩阵的初等变换

<img src="http://img.reedyoung.cn/image-20230322120540195.png" alt="image-20230322120540195" style="zoom:33%;" />

行阶梯形与行标准形

​	<img src="http://img.reedyoung.cn/image-20230322120704419.png" alt="image-20230322120704419" style="zoom:33%;" />

标准形

<img src="http://img.reedyoung.cn/image-20230322121044795.png" alt="image-20230322121044795" style="zoom:33%;" />

初等矩阵：对单位矩阵$I$实施一次初等变换得到的矩阵，成为初等矩阵

​	行初等与列初等，各自分为三种

对矩阵$A$实施一次行初等变换，相当于用相应的初等矩阵左乘；列初等变换相当于用相应的初等矩阵右乘

矩阵等价：

<img src="http://img.reedyoung.cn/image-20230322122214731.png" alt="image-20230322122214731" style="zoom:33%;" />

​			自反、对称、传递

初等变换求逆法：

<img src="http://img.reedyoung.cn/image-20230322125151595.png" alt="image-20230322125151595" style="zoom:33%;" />

#### 矩阵的秩

性质：

$$
满秩 \Leftrightarrow 可逆 \Leftrightarrow det(A) 
e 0
$$
<img src="http://img.reedyoung.cn/image-20230322131832370.png" alt="image-20230322131832370" style="zoom:33%;" />

初等变换不改变矩阵的秩

有关秩的定理：

​		矩阵乘积的秩不超过每个因子的秩：
$$
r(AB) \le min \{ r(A), r(B)\}
$$
​		Sylvester公式：

<img src="http://img.reedyoung.cn/image-20230322131959259.png" alt="image-20230322131959259" style="zoom:33%;" />

​	还有：

<img src="http://img.reedyoung.cn/image-20230322132141462.png" alt="image-20230322132141462" style="zoom:33%;" />

### Ch3 向量

除非特别说明，所有向量都指**列**向量

#### 运算

线性运算：加法与数乘

<img src="http://img.reedyoung.cn/image-20230322132503135.png" alt="image-20230322132503135" style="zoom:33%;" />

#### 向量组的线性相关性

线性组合

线性无关/相关：

<img src="http://img.reedyoung.cn/image-20230322185905251.png" alt="image-20230322185905251" style="zoom:33%;" />

​		即，仅当k1...kn都为0时向量的线性组合才为0，时，线性无关

​		若线性无关，则说明“不共线”(几何意义)

​		向量组$\left \{ lpha_1, lpha_2,  lpha_3..., lpha_m ight \} $线性无关 $\Leftrightarrow$ 其中至少有一个向量是其余向量的线性组合

性质：(好像没用)

<img src="http://img.reedyoung.cn/image-20230322192005922.png" alt="image-20230322192005922" style="zoom:33%;" />

#### 向量组的极大线性无关组

等价的向量组：<img src="http://img.reedyoung.cn/image-20230322192254803.png" alt="image-20230322192254803" style="zoom:33%;" />

<img src="http://img.reedyoung.cn/image-20230322194557827.png" alt="image-20230322194557827" style="zoom:33%;" />

由此引出极大线性无关组

<img src="http://img.reedyoung.cn/image-20230322201823058.png" alt="image-20230322201823058" style="zoom: 25%;" />

给定一个向量组，它的任何两个极大线性无关组都是等价的，从而所含向量一样多，因此：

<img src="http://img.reedyoung.cn/image-20230322200131219.png" alt="image-20230322200131219" style="zoom:33%;" />

向量组的秩与矩阵的秩的关系：

首先，对于矩阵$A$实行行初等变换，不会改变$A$的列向量组的线性相关性和线性组合关系

​	例题，求向量组的线性相关性，把列向量矩阵华为行标准形，有0行即线性相关

所以，**矩阵$A$的秩等于$A$的列向量组的秩**

->

<img src="http://img.reedyoung.cn/image-20230322201514379.png" alt="image-20230322201514379" style="zoom: 25%;" />



#### 向量空间

向量生成的线性空间

基：线性无关，任一向量都可表出

<img src="http://img.reedyoung.cn/image-20230323134009617.png" alt="image-20230323134009617" style="zoom:33%;" />

​	可逆矩阵(可逆变换)不改变向量组的线性相关性$\leftarrow$可逆矩阵等价于一系列初等矩阵的积

向量空间$V$的基实际上是$V$作为向量集合的极大线性无关组

过渡矩阵(基变换矩阵)

<img src="http://img.reedyoung.cn/image-20230323133326058.png" alt="image-20230323133326058" style="zoom:33%;" />

<span id = '坐标变换公式'>坐标变换公式</span>

<img src="http://img.reedyoung.cn/image-20230323172834259.png" alt="image-20230323172834259" style="zoom:33%;" />

用初等行变换求$C$（$A^{-1}B$）以及$C^{-1}X$：由过度矩阵可知$B=AC$

<img src="http://img.reedyoung.cn/image-20230323180659208.png" alt="image-20230323180659208" style="zoom:33%;" />

$lpha$关于$A$的坐标为$X$，有$Y=C^{-1}X$：因为[坐标变换公式](#坐标变换公式)

#### Euclidean空间 $\mathbb{R}^n$

内积(向量点乘)

Cauchy-Schwarz 不等式

<img src="http://img.reedyoung.cn/image-20230323183133562.png" alt="image-20230323183133562" style="zoom:33%;" />

夹角，夹角余弦

正规化

标准正交向量组

把 线性无关向量组 化为 正交向量组的 Gram-Schmidt 正交化方法

<img src="http://img.reedyoung.cn/image-20230323222529277.png" alt="image-20230323222529277" style="zoom:33%;" />

### Ch4 线性方程组

线性方程组 齐次/非齐次 解

等价的线性方程组

<img src="http://img.reedyoung.cn/image-20230324001303513.png" alt="image-20230324001303513" style="zoom:33%;" />

唯一解：

<img src="http://img.reedyoung.cn/image-20230324002554707.png" alt="image-20230324002554707" style="zoom:33%;" />

为什么？

#### Gauss 消元法

<img src="http://img.reedyoung.cn/image-20230324003235147.png" alt="image-20230324003235147" style="zoom:33%;" />

线性方程组有解/无解的充要条件：

<img src="http://img.reedyoung.cn/image-20230324003624303.png" alt="image-20230324003624303" style="zoom:33%;" />

自由变量

#### 齐次方程组解的结构

解空间$N(A)$

解空间是一个向量空间

解空间的基称为方程组$AX=0$的基础解系

<img src="http://img.reedyoung.cn/image-20230324005518582.png" alt="image-20230324005518582" style="zoom:33%;" />

解空间的维数：

<img src="http://img.reedyoung.cn/image-20230324005926277.png" alt="image-20230324005926277" style="zoom:33%;" />

基础解系的求法：

<img src="http://img.reedyoung.cn/image-20230324010808390.png" alt="image-20230324010808390" style="zoom:33%;" />

在秩不等式中的应用：

<img src="http://img.reedyoung.cn/image-20230324012927795.png" alt="image-20230324012927795" style="zoom:33%;" />

#### 非齐次方程组解的结构

<img src="http://img.reedyoung.cn/image-20230324090329595.png" alt="image-20230324012927795" style="zoom:33%;" />

非齐次解相减即为齐次解

### Ch5 相似矩阵

本章讨论都是方阵

#### 特征向量与特征值

<img src="http://img.reedyoung.cn/image-20230324095224314.png" alt="image-20230324095224314" style="zoom:33%;" />

特征值 特征向量 *矩阵的特征值等于逆矩阵特征值的倒数,反过来也一样*

<img src="http://img.reedyoung.cn/image-20230324100408412.png" alt="image-20230324100408412" style="zoom:33%;" />
$$
如果λ是A的一个特征值，对应的特征向量为v，则f(λ)是f(A)的一个特征值，对应的特征向量仍为v。
$$
特征多项式：

<img src="http://img.reedyoung.cn/image-20230324100424325.png" alt="image-20230324100424325" style="zoom:33%;" />

特征值：

<img src="http://img.reedyoung.cn/image-20230324101747513.png" alt="image-20230324101747513" style="zoom: 33%;" />

迹：

<img src="http://img.reedyoung.cn/image-20230324101824037.png" alt="image-20230324101824037" style="zoom: 33%;" />

特征值和特征向量的求法：

<img src="http://img.reedyoung.cn/image-20230324102245525.png" alt="image-20230324102245525" style="zoom:33%;" />

$g(\lambda)$是$g(A)$的特征值：

<img src="http://img.reedyoung.cn/image-20230324105659443.png" alt="image-20230324105659443" style="zoom:50%;" />

#### 特征向量的性质

特征向量的线性无关性：简言之，同一个特征值对应的所有特征向量都是线性相关的，不同特征值的特征向量之间一定线性无关

​				***实对称*不同特征值对应的特征向量  $ightarrow$ 彼此正交**

重数：

<img src="http://img.reedyoung.cn/image-20230324114243028.png" alt="image-20230324114243028" style="zoom:33%;" />

#### 相似矩阵对角化

相似矩阵：

<img src="http://img.reedyoung.cn/image-20230324114539783.png" alt="image-20230324114539783" style="zoom:33%;" />

<img src="http://img.reedyoung.cn/image-20230324114606259.png" alt="image-20230324114606259" style="zoom:33%;" />

对角化：

<img src="http://img.reedyoung.cn/image-20230324114811245.png" alt="image-20230324114811245" style="zoom:33%;" />

可逆矩阵$P$的n个列向量$X_1,X_2,...,X_n$分别是$A$对应于$\lambda_1,...,\lambda_n$的特征向量：

<img src="http://img.reedyoung.cn/image-20230324115020053.png" alt="image-20230324115020053" style="zoom:33%;" />

可对角化条件：

<img src="http://img.reedyoung.cn/image-20230324115108157.png" alt="image-20230324115108157" style="zoom:33%;" />

<img src="http://img.reedyoung.cn/image-20230324120147016.png" alt="image-20230324120147016" style="zoom:33%;" />

<img src="http://img.reedyoung.cn/image-20230324121031919.png" alt="image-20230324121031919" style="zoom:33%;" />

<img src="http://img.reedyoung.cn/image-20230324121104198.png" alt="image-20230324121104198" style="zoom:33%;" />



#### 应用：一阶齐次线性常系数微分方程组

### Ch6 二次型

#### 二次型及其矩阵表示

关于对称矩阵：以主对角线为轴，各元素对应相等

要求二次型为、、、、、、、、、、、、、、、、、矩阵！！！

<img src="http://img.reedyoung.cn/image-20230324134127094.png" alt="image-20230324134127094" style="zoom: 50%;" />

<img src="http://img.reedyoung.cn/image-20230324134217572.png" alt="image-20230324134217572" style="zoom:33%;" />

线性变换：

<img src="http://img.reedyoung.cn/image-20230324134403432.png" alt="image-20230324134403432" style="zoom:33%;" />

<img src="http://img.reedyoung.cn/image-20230324134421748.png" alt="image-20230324134421748" style="zoom:33%;" />

#### 标准形、规范形

<img src="http://img.reedyoung.cn/image-20230324142452438.png" alt="image-20230324142452438" style="zoom:33%;" />

<img src="http://img.reedyoung.cn/image-20230324142518699.png" alt="image-20230324142518699" style="zoom:33%;" />

二次型的基本问题：

<img src="http://img.reedyoung.cn/image-20230324142544875.png" alt="image-20230324142544875" style="zoom:33%;" />

#### 矩阵合同

<img src="http://img.reedyoung.cn/image-20230324142806566.png" alt="image-20230324142806566" style="zoom:33%;" />

<img src="http://img.reedyoung.cn/image-20230324142857983.png" alt="image-20230324142857983" style="zoom:33%;" />

矩阵间的三种关系

<img src="http://img.reedyoung.cn/image-20230324142922849.png" alt="image-20230324142922849" style="zoom:33%;" />

#### 正交变换法化二次型为标准形

正交矩阵

<img src="http://img.reedyoung.cn/image-20230324143032924.png" alt="image-20230324143032924" style="zoom:33%;" />

正交变换

<img src="http://img.reedyoung.cn/image-20230324143049802.png" alt="image-20230324143049802" style="zoom:33%;" />

用正交矩阵得到的矩阵合同同时也是矩阵的相似

<img src="http://img.reedyoung.cn/image-20230324144057629.png" alt="image-20230324144057629" style="zoom:33%;" />

主轴定理

<img src="http://img.reedyoung.cn/image-20230324161927033.png" alt="image-20230324161927033" style="zoom:33%;" />

用正交变换化二次型为标准形的步骤：

<img src="http://img.reedyoung.cn/image-20230324161942551.png" alt="image-20230324161942551" style="zoom:33%;" />

#### 几何意义

<img src="http://img.reedyoung.cn/image-20230324164134085.png" alt="image-20230324164134085" style="zoom:33%;" />

#### 二次型的正定性

惯性定理：

<img src="http://img.reedyoung.cn/image-20230324172259180.png" alt="image-20230324172259180" style="zoom:33%;" />

惯性指数：

<img src="http://img.reedyoung.cn/image-20230324172433827.png" alt="image-20230324172433827" style="zoom:33%;" />

规范形：

<img src="http://img.reedyoung.cn/image-20230324172525616.png" alt="image-20230324172525616" style="zoom:33%;" />

对称矩阵合同：

<img src="http://img.reedyoung.cn/image-20230324172752971.png" alt="image-20230324172752971" style="zoom:33%;" />

正定二次型：

<img src="http://img.reedyoung.cn/image-20230324172849159.png" alt="image-20230324172849159" style="zoom:33%;" />

判断准则：实对称矩阵正定的充要条件是特征值全正

<img src="http://img.reedyoung.cn/image-20230324173144646.png" alt="image-20230324173144646" style="zoom:33%;" />

#### Sylvester定理

<img src="http://img.reedyoung.cn/image-20230324174142725.png" alt="image-20230324174142725" style="zoom:33%;" />

正定性判断的几种方式：

<img src="http://img.reedyoung.cn/image-20230324174221945.png" alt="image-20230324174221945" style="zoom:33%;" />

正定矩阵主对角元素恒正：

<img src="http://img.reedyoung.cn/image-20230324174458557.png" alt="image-20230324174458557" style="zoom:33%;" />

正定矩阵的乘积(也正定)：

<img src="http://img.reedyoung.cn/image-20230324174702323.png" alt="image-20230324174702323" style="zoom:33%;" />
