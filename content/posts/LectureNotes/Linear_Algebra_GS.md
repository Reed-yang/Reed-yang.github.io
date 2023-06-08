---
title: "Linear_Algebra_GS"
---
### Chapter 2

> Didn't follow up a textbook actually

转置运算性质：$(AB)^T=B^TA^T$



$AA^{-1} = I$

$\Rightarrow \left( AA^{-1} ight)^{T} = I^T$

$\Rightarrow(A^{-1})^{T}A^T=I$

$\Rightarrow(A^{-1})^T=(A^T)^{-1}$ 对于单个矩阵，转置和求逆可以交换顺序



$A=LU$



**置换矩阵**（行交换），n阶矩阵的$P$有$n！$的种，且有性质：$P^{-1}=P^T \Leftrightarrow P^TP=I$



$R^TR$ is always symetric

### Chapter 3 空间

向量空间：

​	$R^2$ = 所有二维实向量

​	$R^3$ = 所有三维实向量，比如$egin{bmatrix} 2 \ 3 \ 0nd{bmatrix}$ 在$R^3$中，而非$R^2$中



子空间（subspace）：在某一向量空间内的一个范围，符合一些性质（比如，零向量在其中；封闭性：向量的任意线性组合在其中（*其实封闭性的要求确定了零向量必在子空间中*）），称为向量空间的一个子空间



列空间：列向量的所有线性组合构成的子空间

​	若有矩阵$A=egin{bmatrix} 1 & 1 & 2 \ 2 & 1 & 3 \ 3 & 1 & 4 \ 4 & 1 & 5 nd{bmatrix}$,其列向量构成的子空间记为$C(A)$

$Ax=b$ 有解，当且仅当$b$在A的列空间中



零空间：Nullspace记为$N(A)$

​	$Ax=egin{bmatrix} 1 & 1 & 2 \ 2 & 1 & 3 \ 3 & 1 & 4 \ 4 & 1 & 5 nd{bmatrix}egin{bmatrix} x_1 \ x_2 \ x_3 nd{bmatrix} = egin{bmatrix} 0 \ 0 \ 0 \ 0 nd{bmatrix} = 0$ 的解$x$构成一个子空间，称之为零空间.例中的零空间为$cegin{bmatrix} 1 \ 1 \ -1 nd{bmatrix}$ in $R^3$ 的一条直线.

​	称为零空间，因为易整所有的解$x$具有封闭性.



求解$Ax=0$：

- 方程组的解不随消元改变，即消元不改变矩阵零空间（改变列空间）

- 矩阵的秩(rank)：主变量的个数

- 自由变量：不做主变量，即为自由变量，指无论取何值都能得到解$x$的变量

- $A ightarrow U$ 阶梯矩阵 $ ightarrow R$ 简化行阶梯矩阵

  $egin{bmatrix} 1&2&2&2\2&4&6&8\3&6&8&10 nd{bmatrix} ightarrow egin{bmatrix} \underline{1}&2&2&2\0&0&\underline{2}&4\0&0&0&0 nd{bmatrix} ightarrow egin{bmatrix} 1&2&0&-2\0&0&1&2\0&0&0&0 nd{bmatrix}$

- $R$可以表示为$egin{bmatrix} I & F\0&0nd{bmatrix}$即重排为两个部分，单位矩阵和自由列，可以得到$\overline{x} = egin{bmatrix}-F\Ind{bmatrix}$矩阵中的每一列是$x$的特解，对特解线性组合可得零空间

- 矩阵和他的转置的秩相等

- [关于自由变量选取和其在求解零空间过程中的意义](https://zhuanlan.zhihu.com/p/444184363)



求解$Ax=b$：

- Solvability Condition on b.可解性条件，b满足什么条件才能让$Ax=b$总有解？

   在消元后，零行对应的右侧分量满足：经过相同消元过程为零。

- $x_{complete} = x_p + x_{nullspace}$

  令所有自由变量为零，解方程组可得一个特解$x_{particular} \ aka. \ x_p$



$Ax=b$解的结构：对于$A_{m 	imes n}$ ,其秩为r

- 列满秩：r=n

  每一列都有主元，无自由变量

  $N(A)$为零向量（因为无自由变量可赋值），故：若$Ax=b$有解，那么解唯一（$x_p$）

- 行满秩：r=m

  每一行都有主元，没有消元后没有零行，有n-r个自由变量，$R=egin{bmatrix}I&Fnd{bmatrix}$

  由于没有零行，因此对任意的右侧向量$b$，$Ax=b$都有解，即：必有解

  由于$x_{complete} = x_p + x_{nullspace}$，$x$一定有无穷个解(因为至少有零空间内的无穷个解)

- r=m=n

  $A$一定是可逆矩阵

  其行最简形式$R=I$

  一定有且一定仅有一个解

- r<m,r<n

  $$R=egin{bmatrix}I&F\0&0nd{bmatrix}$$

  0 or $\infin$ 个解



四个基本子空间(4 subspaces): $A_{m 	imes n}$，$rank(A) = r$

​	columnspace: $C(A)$ in $R^m$ (注意：这里不是说$C(A)$是m维的，而是说它在m维实空间中，故，看每列的元素数即可)

​	nullspace: $N(A)$ in $R^n$

​	rowspace: $C(A^T)$ in $R^n$

​	nullspace of $A^T$/ left nullspace: $N(A^T)$ in $R^m$

- 列空间和行空间的维数相同，$dimC(A)=dimC(A^T)=r$
- 零空间维数：$dimN(A)=n-r$，左零空间维数：$dimN(A^T)=m-r$
- 初等行变换不改变矩阵的行空间，因此，**行空间的基**即为$A$的$R$中的前r行.
- **左零空间的基**：$E \left[ egin{array}{c:c} egin{matrix} And{matrix}&egin{matrix} Ind{matrix} nd{array} ight] = \left[ egin{array}{c:c} egin{matrix} Rnd{matrix}&egin{matrix} E nd{matrix} nd{array} ight]$ 左零空间的基为$R$中全零行所在行的$E$的行向量



秩1矩阵：秩1矩阵可以表示为一列向量乘一行向量、秩为r的矩阵可以表示为r个秩1矩阵的和



**矩阵空间**：

​	使用对向量相同的加法和数乘定义，一组矩阵的线性组合构成一个矩阵空间

**函数空间**

![[公式]](https://www.zhihu.com/equation?tex=y%5E%7B%27%27%7D%3D0) 的解构成了一个函数矢量空间，因为任何两个满足方程的函数的线性组合依然是方程的解，满足了闭合性。我们需要回忆一点点微积分知识来求得这个二阶常微分方程的解是 ![[公式]](https://www.zhihu.com/equation?tex=y%3Dcx%2Bd) ，它的一组基是 ![[公式]](https://www.zhihu.com/equation?tex=1) 和 ![[公式]](https://www.zhihu.com/equation?tex=x) ，它的维度是 ![[公式]](https://www.zhihu.com/equation?tex=2) 。

![[公式]](https://www.zhihu.com/equation?tex=y%5E%7B%27%27%7D%3D-y) 的解空间也是矢量空间。方程的解为 ![[公式]](https://www.zhihu.com/equation?tex=y%3Dcsinx%2Bdcosx) ，或用复指数的形式写成 ![[公式]](https://www.zhihu.com/equation?tex=y%3Dce%5E%7Bix%7D%2Bde%5E%7B-ix%7D+) 。它的一组基是 ![[公式]](https://www.zhihu.com/equation?tex=sinx%2Ccosx) ，也可以选![[公式]](https://www.zhihu.com/equation?tex=e%5E%7Bix%7D%2Ce%5E%7B-ix%7D) 作为基，这个函数空间的维度也是 ![[公式]](https://www.zhihu.com/equation?tex=2) 。

![[公式]](https://www.zhihu.com/equation?tex=y%5E%7B%27%27%7D%3Dy) 的解为 ![[公式]](https://www.zhihu.com/equation?tex=y%3Dce%5E%7Bx%7D%2Bde%5E%7B-x%7D) ，解空间也是矢量空间，它的一组基是 ![[公式]](https://www.zhihu.com/equation?tex=e%5E%7Bx%7D) 和 ![[公式]](https://www.zhihu.com/equation?tex=e%5E%7B-x%7D) ，它的维度和之前的 ![[公式]](https://www.zhihu.com/equation?tex=2) 个二阶常微分方程一样，也是 ![[公式]](https://www.zhihu.com/equation?tex=2) 。

但是 ![[公式]](https://www.zhihu.com/equation?tex=y%5E%7B%27%27%7D%3D2) 的解就不能构成矢量空间了，读者可以验证一下。这个方程的一个特解是 ![[公式]](https://www.zhihu.com/equation?tex=y%3Dx%5E%7B2%7D) ，它的完整解是 ![[公式]](https://www.zhihu.com/equation?tex=y%3Dx%5E%7B2%7D%2Bcx%2Bd) ，其中 ![[公式]](https://www.zhihu.com/equation?tex=cx%2Bd) 是 ![[公式]](https://www.zhihu.com/equation?tex=y%5E%7B%27%27%7D%3D0) 的解，完整解的形式是特解加上零空间的矢量。读到这里你是不是联想到了我们之前学习的 ![[公式]](https://www.zhihu.com/equation?tex=Ax%3Db) 的解，这个方程的解也不是矢量空间，它的完整解也是由特解和零空间的矢量构成。



线性代数(线性变换)的应用：基尔霍夫定律、图论、平衡方程



### Chapter 4 正交性

正交、矢量正交、子空间正交: 两个子空间正交意味着某子空间内的任意适量和另一子空间内的任意适量正交



两个正交子空间的交点只能是零矢量



$N(A^TA)=N(A)$、rank of $A^TA$ = rank of $A$



投影矩阵$P = A(A^TA)^{-1}A^T$

- $P^T=P$
- $P^2=P$



投影矩阵应用：最小二乘法拟合直线(最小二乘法优化线性回归)

​	求解正规方程：$A^TA\hat{x}=A^Tb$



如果$A$各列独立，则$A^TA$可逆

---

[投影与最小二乘法](https://zhuanlan.zhihu.com/p/355019543)

---

标准正交基$q$与正交矩阵$Q$



Gram-Schmidt正交化

​	经过正交化可以记为$A=QR$，$R$是一个上三角矩阵，是一个描述了正交化变换过程的矩阵

---

[标准正交基，Gram-Schmidt与QR分解](https://zhuanlan.zhihu.com/p/357077465)

---

### Chapter 5 
