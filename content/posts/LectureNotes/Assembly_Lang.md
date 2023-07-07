---
title: "Assembly_Lang"
date: 2023-03-26T09:00:35+00:00
tags: ['LectureNotes']
---
### 寻址方式

寻址方式一共有6种：

#### 立即寻址

：操作数可以是立即数，也可以是一串未完成的加减乘除运算（但是算式中不能含有未知数）。立即寻址时，操作数就在操作指令的后面跟着。

#### 寄存器寻址

：寄存器本质上，是为CPU中的存储单元一个助记符名，方便调用。其类型为dword，32位。寄存器寻址时，操作数就在CPU中存储，且这个存储单元有固定的名称（即为“寄存器”）。

add eax, ebx

--- **以下寻址方式的操作数在存储器(内存)中**

#### 直接寻址(存储器寻址)

：操作数在内存中存放。操作数的偏移地址紧跟指令操作码，构成指令操作码的一部分。

#### 寄存器间接寻址

：操作数在存储器中，其全部的偏移地址在寄存器中。

#### 变址寻址

：操作数在存储器中，偏移地址的个数在寄存器中，使用时需要乘比例因子F（1，2，4，8），再与给定的起始地址相加。

#### 基址加变址寻址

### 指令

#### 移位指令 shl&shr sar&sal rol&ror rcl&rcr

- Shift Logical Left or Right 
- Shift Arithmatic Left or Right 

SHL逻辑左移；左移，最低位补0，最高位进入CF。

SHR逻辑右移；右移，最高位补0，最低位进入CF。

SAL算术左移；左移，与SHL功能相同。

SAR算术右移；右移，最高位不变(符号位，若为负，则进1），最低位进入CF。

- ror rol

  xu

#### 数据传输指令 movsx movzx xchg xlat

- movsx：有符号数扩展

- movzx：无符号数扩展

  扩展传送，将数据从较少位寄存器/内存单元，拷贝至较多位寄存器，根据有/无符号，将扩展位填1/0

- xchg：数据交换，且两个数据不能同时为存储器寻址

- xlat：查表(translate)转换指令。其中，`[ebx + al] -> al`

  该指令会查询 在ebx表首地址中al偏移的值，并把该值传给al

#### 堆栈操作指令 push pop lea

**堆栈存储方式：从高字节向低字节存储，存储一个字或者双字**

#### 逻辑运算指令

and 逻辑乘，即按位与

AND 指令 与 标志位AND指令影响标志位PF、SF、ZF,使CF=0、OF=0

.例如,在同一个通用寄存器自身相与时,操作数虽不变,但使CF置零.

#### 分支循环指令

转移的范围在-128~+127之间。

- loop: ecx/cx - 1 -> ecx/cx，若不为0，转移到标志位继续。但注意：ecx倒计数不影响标志位
- loope(==loopz)：ecx/cx != 0 & ZF = 1，转到标号进行。否则终止。（也就是说，ZF要一直为1）
- loopne：ecx/cx != 0 & ZF = 0，转到标号进行。否则终止。（ZF == 0）
- jcxz: ecx/cx的值为0时，转到标号进行。否则终止。

#### 指令转移 jmp: jmp short / near ptr / far ptr / word ptr / dword ptr

#### 检测比较结果的条件转移指令 j+e ne b nb a na

e: equal

ne: not equal

b: below

nb: not below

a: above

na: not 

### 子程序

函数结束ret，相当于pop 断点

ret

### 中断

实方式 和 保护模式 中断矢量表有区别

先IP后CS

**标志寄存器**

符号标志为 SF Sign Flag

运算结果最高位为1，则SF=1，否则SF=0

**保护模式和实模式，物理地址的获取方式**

实模式：直接运算；保护模式：寄存器所引到段描述符表，再获取地址

MUL 的乘积结果在 DX、AX中

---

**Question？**

1. 怎么调用*QueryPerformanceFrequency*
2. 怎么定义LOCAL
