---
title: "C++ Primer"
---
# C++ Primer

## 第一章 开始

### 1.1

- `类型Type`

- 从命令行运行编译器

  ```bash
  $ CC prog1.cc
  ```

  $是系统提示符，CC是编译器程序的名字。编译器生成一个可执行文件，Win会将该文件命名为prog1.exe，UNIX系统中的编译器通常命名为a.out。

### 1.2 初识输入输出

**iostream**标准库，包含两个基础类型**istream**和**ostream**（输入流和输出流）。一个流就是一个字符序列，从设备读出或写入。

- 标准IO对象

  cin是istream类型的对象，也成为标准输入standard input。

  类似的有cout。

- 向流写入数据

  **输出运算符(<<)**在标准输出上打印信息

  ```cpp
  std::cout << "Enter two numbers:" << std::endl;
  ```

  **<<**接受两个运算对象，左侧必须是一个ostream对象，右侧是要打印的值。**<<**的运算结果是其左值，本例中即仍是std::cout，故可将输出请求连接起来。等价于：

  ```cpp
  std::cout << "Enter two numbers:";
  std::cout << std::endl;
  ```

- endl是被称为操作符(manipulator)的特殊值。写入的效果是结束当前行，并将于设备关联的缓冲区(buffer)中的内容刷新到设备中，保证目前为止程序所产生的所有输出都真正写入输出流中去，而不仅仅停留在内存中等待写入。

- 前缀**std::**指出定义在**std**的**命名空间(namespace)**中的。

  **作用域运算符::**
