---
title: "Computer Organization & Architecture_HUST"
date: 2023-04-19T09:32:45+00:00
tags: ['LectureNotes']
---
@全体成员 不考内容
2.2.4 十进制编码 
2.4.4 循环冗余校验码
3.4 定点除法运算
4.2 半导体存储器
5.7 指令系统举例
7 指令流水线
8 总线系统
9.7 通道方式
9.8 常见IO设备

七道大题，数据表示与运算两题，存储 2 题，指令系统一题，cpu 设计一题，io 一题，请关注下 mips 指令格式和常见五条指令数据通路

## Ch2 计算机数据表示

- 进制转换

### 数值数据的表示方法

- 数的机器码表示

  - 真值：书写用

  - 机器码：原码 反码 补码 移码

    - 原码：最高位增加了符号位；有两个0

    - 反码：正数的反码=原码，负数的反码=符号位+原码各位取反；也有两个0

    - 补码：正=原码；当X为负数时，补码等于反码末位加1，即原码取反加1

      - 计算补码的数值：<img src="http://img.reedyoung.cn/image-20230601143453027.png" alt="image-20230601143453027" style="zoom: 33%;margin: 0 auto;" />
      - 唯一的0
      - 负数比正数多一个

    - 移码：即把补码的符号位取反

      <img src="http://img.reedyoung.cn/image-20230601144726890.png" alt="image-20230601144726890" style="zoom: 33%;margin: 0 auto;" />

- 定点数：前面都是定点数

- 浮点数：IEEE754

  - <img src="http://img.reedyoung.cn/image-20230601224024548.png" alt="image-20230601224024548" style="zoom:33%;margin: 0 auto;" />

  - 注意：阶码是用移码表示的，若想求其值，需减去偏移量

  - <img src="http://img.reedyoung.cn/image-20230601224233310.png" alt="image-20230601224233310" style="zoom: 50%;margin: 0 auto;" />

  - 注意规格化数和非规格化数

    - 浮点编码与真值的转化流程：

      <img src="http://img.reedyoung.cn/image-20230601224355807.png" alt="image-20230601224355807" style="zoom:33%;margin: 0 auto;" />

  - 浮点数存在两个0

- 数据类型：没什么东西

### 非数值数据的表示法

- 字符表示 ASCII：使用7bit表示128个字符， MSB=0
- 汉字编码：
  - GB2312机内码 = 区位码+0xA0A0
  - 与ASCII字符的区别，最高有效位MSB=1

### 数据信息的校验

- 码距与校验
  - 码距：码字之间的距离定义为两个码字之间不同位的数量。例如，对于两个4位的二进制码字"0101"和"0110"，它们之间的距离是2，因为它们有两个不同的位。
  -  
- 奇偶校验
  - 一维很简单， 只能检错，无法纠错
  - 二维：三位错可检
- 海明校验
  - 
- 

## Ch3 运算方法与运算器

- 计算机中的运算

### 定点加减法运算

- 补码加减法

  <img src="http://img.reedyoung.cn/image-20230601160149432.png" alt="image-20230601160149432" style="zoom: 33%;margin: 0 auto;" />

- 溢出及检测

  - **溢出逻辑：** **正正得负 负负得正**
  -  <img src="http://img.reedyoung.cn/image-20230601162115210.png" alt="image-20230601162115210" style="zoom:25%;margin: 0 auto;" />符号位进位Cf，数值最高位进位Cn

- 加减法的逻辑实现

  - 带进位链的一位全加器

    <img src="http://img.reedyoung.cn/image-20230601162302874.png" alt="image-20230601162302874" style="zoom:33%;margin: 0 auto;" />

  - n位加法器: 直接串联

    <img src="http://img.reedyoung.cn/image-20230601162417843.png" alt="image-20230601162417843" style="zoom: 33%;margin: 0 auto;" />

  - 单符号补码加法器: 无符号有符号加法器实际没区别

    <img src="http://img.reedyoung.cn/image-20230601162605669.png" alt="image-20230601162605669" style="zoom:33%;margin: 0 auto;" />

    ​	无符号加法器的溢出检测：加法变小，减法变大

  - 可控加减法电路：

    <img src="http://img.reedyoung.cn/image-20230601162945298.png" alt="image-20230601162945298" style="zoom: 33%;margin: 0 auto;" />

  - 串行加法器时延的分析：注意片内并行，每次只等待上一级的Ci输入，而Ci->Ci+1只需2T(源自逻辑图)

    <img src="http://img.reedyoung.cn/image-20230601163214195.png" alt="image-20230601163214195" style="zoom: 50%;margin: 0 auto;" />

  - 快速加法器：

    去掉进位依赖：能否提前产生各位的进位输入

    各位加法并行：可提高多位加法器的速度

    - <img src="http://img.reedyoung.cn/image-20230601170234614.png" alt="image-20230601170234614" style="zoom: 33%;margin: 0 auto;" />
    - G，P的输出与C0进位无关，可以并行，注意分析时延性质

### 定点乘法运算

- 原码一位乘法

  - 循环累加，累加后逻辑右移(遇Yn=0直接右移)
  - 连同**进位位一起右移（逻辑）**
  - **可能溢出**，移位后正常

- 补码一位乘法

  -  拆解为如下公式：<img src="http://img.reedyoung.cn/image-20230601212509749.png" alt="image-20230601212509749" style="zoom:33%;margin: 0 auto;" />(计算时取Yn+1=0,即增加一个末位0)
  - 注意是算术右移，如果需要，要补1

- 阵列乘法器：串行和斜向

- 补码阵列：先求补，用阵列算积绝对值，再对结果判断求补

  <img src="http://img.reedyoung.cn/image-20230601215618835.png" alt="image-20230601215618835" style="zoom: 50%;margin: 0 auto;" />

### 浮点运算

- 对阶: 小阶对大阶  尾数右移

- 尾数求和

- 规格化（左规，右规）：(规格化时注意阶码同步改变)

  <img src="http://img.reedyoung.cn/image-20230601225521985.png" alt="image-20230601225521985" style="zoom:33%;margin: 0 auto;" />

- 溢出判断

- 舍入（截去、0舍1入、偶数舍入）

### 运算器

不知道怎么考

## Ch4 存储系统

### 主存的组织以及与CPU的连接

- 地址线 数据线 控制线

   ![image-20230602010219798](http://img.reedyoung.cn/image-20230602010219798.png)

  A 对应 地址线

  D 对应 数据总线

- 字长扩展：数据总线扩展

- 字数扩展：地址总线扩展

### 并行主存系统

- 双端口存储器

- 多模块存储器
- 单体多字存储器
- 多通道内存
  - 两种多通道模式：
    - 单体多字
    - 多体多字
- 多体单词存储器(多体交叉存储器)
  - 多模块顺序：存储扩展
  - 多模块交叉

### Cache

- cache 工作原理

- 程序局部性

- cache关键技术

  - 数据查找(是否在cache中)：相联存储器

    <img src="http://img.reedyoung.cn/image-20230602012032885.png" alt="image-20230602012032885" style="zoom:25%;margin: 0 auto;" />

    <img src="http://img.reedyoung.cn/image-20230602012135034.png" alt="image-20230602012135034" style="zoom:25%;margin: 0 auto;" />

    <img src="http://img.reedyoung.cn/image-20230602012146687.png" alt="image-20230602012146687" style="zoom:25%;margin: 0 auto;" />

  - 地址映射：

    - 全相联
    - 直接相连
    - 组相联

  - 替换策略(Cache满后如何处理)：

    - FIFO
    - LFU
    - LRU

  - 写入策略(如何保证cache与memory的一致性)

### 虚拟存储器

- 虚拟内存
- 现代PC的CPU地址都是虚地址
- 

- 虚拟内存与Cache差异：

  <img src="http://img.reedyoung.cn/image-20230602011104209.png" alt="image-20230602011104209" style="zoom: 33%;margin: 0 auto;" />

- 页式虚拟内存
- TLB：缓存页表中经常被访问的表项
- 

## Ch5 指令系统

### MIPS

### 指令格式

<img src="http://img.reedyoung.cn/image-20230602104744822.png" alt="image-20230602104744822" style="zoom:33%;margin: 0 auto;" />

### 寻址方式

<img src="http://img.reedyoung.cn/image-20230602110024601.png" alt="image-20230602110024601" style="zoom: 33%;margin: 0 auto;" />

### 指令类型

分类

### 指令格式设计

1. 根据指令规模及是否支持操作码扩展，确定操作码字段长度
2. 根据对操作数的要求确定地址码字段的个数
3. 根据寻址方式的要求，为各地址码字段确定寻址方式字段长度
4. 定长还是变长

## Ch6 中央处理器

概述：

<img src="http://img.reedyoung.cn/image-20230602114315509.png" alt="image-20230602114315509" style="zoom:33%;margin: 0 auto;" />

### 指令周期

### 硬布线控制器

单总线：CPU<img src="http://img.reedyoung.cn/image-20230602145541943.png" alt="image-20230602145541943" style="zoom: 33%;margin: 0 auto;" />

### 微程序控制器

## Ch9 IO系统

### 中断

### DMA

---

## 问题

1. 怎么证明的，为什么mod2，为什么[y]补=2+y

   ![image-20230601161446380](http://img.reedyoung.cn/image-20230601161446380.png)

2. 
