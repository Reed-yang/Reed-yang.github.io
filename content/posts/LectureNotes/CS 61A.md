---
title: "CS 61A"
date: 2022-05-06T20:20:39+00:00
tags: ['LectureNotes']
---
### Lecture 1 Intro

### Lecture 2 Function

- 函数签名Function ***signature***

<img src="https://s2.loli.net/2022/05/03/DycwasqbxNHL6Sd.png" alt="image-20220430112729904" style="zoom:50%;margin: 0 auto;" />

- 函数体Function ***body***

  <img src="https://s2.loli.net/2022/05/03/vd5c264TnPFsOYp.png" alt="image-20220430113537980" style="zoom:50%;margin: 0 auto;" />

- ***Frame***

  *scope*-作用域

  *frame*-[栈帧](https://blog.csdn.net/zhuguiqin1/article/details/79290244)

  - 表示程序运行时函数调用栈

### Lecture 3 Control & Iteration

***lamda*** 匿名函数

另一种条件句形式

<img src="https://s2.loli.net/2022/08/07/7Gp1l8uFBItCEy4.png" alt="image-20220807102142758" style="zoom:50%;margin: 0 auto;" />

函数print的返回值是None

### Lecture 4 Higher-Order Functions

***Higher-Order Functions*** 高阶函数

<img src="https://s2.loli.net/2022/08/08/zXP7OJ9bRspDVQk.png" alt="image-20220808095919018" style="zoom: 33%;margin: 0 auto;" />

***currying*** 柯里化 把多参数函数化为单一参数高阶函数

### Lecture 5 Environments

***Decorator*** 装饰器

<img src="https://s2.loli.net/2022/08/10/VNkBCZciPmUMXr1.png" alt="image-20220810112607368" style="zoom: 50%;margin: 0 auto;" />

### Midterm

This expression/Evaluates to/Interactive Output

- ```python
  def delay(arg)
  	print('delayed')
      def g():
          return arg
      return g

  delay(delay)()(6)()
  """">>>
  	delayed
  	delayed
  	6
  """
  ```

### Lecture 6 Recurion

**Verifying Recurion Function**

1. Verify the base case
2. Treat *fact* as a functional abstration
3. Assume that *fact*(n-1) is correct
4. Verify that fact(n) is correct, assuming that fact(n-1) is correct

**Mutual Recurion** 相互递归

```python
def luhn_sum(n):
	if n < 10:
        return n
    else:
		all_but_last, last = split(n)
        return luhn_sum_double(all_but_last) + last

def luhn_sum_double(n):
	all_but_last, last = split(n)
    luhn_digit = sum_digits(2 * last)
    if n < 10:
		return luhn_digit
    else:
        return luhn_sum(all_but_last) + luhn_digit
```

### Lecture 7 Tree Recursion

Tree-shaped processes arise whenever executing the body of a recursive function makes more than one call to that function.

### Lecture 8 Sequences & Data Abstraction

- ***Lists*** 列表

<img src="https://s2.loli.net/2022/08/11/ICmJcj3xkzur9Ob.png" alt="image-20220811155619280" style="zoom:50%;margin: 0 auto;" />

- **for** statement - sequence unpacking

<img src="https://s2.loli.net/2022/08/11/gL9FOtGyBATosR6.png" alt="image-20220811164407829" style="zoom: 50%;margin: 0 auto;" />

- **range** 注意序列值域，左包括，右不包括

<img src="https://s2.loli.net/2022/08/13/6XGUmaKZkyMgBch.png" alt="image-20220813111931270" style="zoom:56%;margin: 0 auto;" />

- **List comprehension** 列表推导式

语法规范：

```python
 out_list = [out_express for out_express in input_list if out_express_condition] 
```

其中的 ` if ` 条件判断根据需要可有可无。

<img src="https://s2.loli.net/2022/08/13/CAe1hXuGNYjOxSL.png" alt="image-20220813113038765" style="zoom:50%;margin: 0 auto;" />

- ***Abstraction barrier*** 以有理数的抽象为例

<img src="https://s2.loli.net/2022/08/13/RCMevfTV9dEFjAo.png" alt="image-20220813170621055" style="zoom: 67%;margin: 0 auto;" />

违反抽象界限的例子：

<img src="https://s2.loli.net/2022/08/13/jMaQFkWRyrlJtqS.png" alt="image-20220813170836217" style="zoom:50%;margin: 0 auto;" />

- Data Abstraction 只关心通过数据“行为”进行的表示，而不关心具体实现——即通过数据使用的行为可定义数据的表示。

例：使用函数而非列表构造的有理数Data Implementation

<img src="https://s2.loli.net/2022/08/13/N4jy8EweI23dpzC.png" alt="image-20220813182732822" style="zoom:67%;margin: 0 auto;" />

- **Dictionary** 字典 a congregation of key-value pairs 键值对的集合

- Lists的复杂操作：

### Lecture 9 Functional Decomposition & Debugging

关于python编程应对错误的几个特性

reduce try 

### Lecture 10 Tree

- Slicing

切片，会创建新的list

![image-20220818225817223](https://s2.loli.net/2022/08/20/liDACzQK4YtESm7.png)
