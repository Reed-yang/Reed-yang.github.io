---
title: "Modern CMake"
date: 2022-05-03T17:52:30+00:00
tags: ['uncategorized']
---
# Modern CMake

form 上海交通大学[IPADS新人培训](https://www.bilibili.com/video/BV14h41187FZ?spm_id_from=333.999.0.0)，代码源自其[github](https://github.com/richardchien/modern-cmake-by-example).

### Intro

- 什么是Makefile

  GNU工具集中的一个工具为Make，其配置文件Makefile，可以通过一些语法来描述规则去编译某个程序项目

  使用CMake的一些语法，帮助编译为不同文件系统的Makefile文件

  CMake通常用于管理开发项目

### Step_0

```makefile
hello: main.cpp
	$(CXX) -o hello main.cpp
	echo "OK"
```

首行，冒号前为*目标target*，即想要编译成为的可执行文件；冒号后是*依赖dependency*，即目标所依赖的main.cpp

之后用Tab缩进的语句为编译的*Command*，示例中有两行命令。

​	line_1括号内CXX是Make默认的变量，它的值是系统的C++编译器，其后是编译指令

​	line_2输出一个OK

构建 & 运行命令：

```shell
$ make hello
$ ./hello
```

如上简单介绍了CMake的语法，实际项目中按此书写代码必然显得臃肿。

### Step_1

```makefile
#
# := 用于给变量赋值，除此之外还有 =、?=、+= 等不同的赋值方式。
#
# 一般全大写变量用来表示允许调用 make 的时候传入的变量，
# 全小写变量表示仅内部使用的变量。
#
# 这里 CC 和 CXX 指定了要使用的 C 和 C++ 编译器。
#
CC := clang
CXX := clang++

#
# Makefile 中的核心概念是 target（目标），定义 target 的基本
# 格式是（注意每一行 command 是必须用 tab 缩进的）：
#
#   name: dependencies
#   	commands
#
# 要构建某个 target 时，使用如下命令：
#
#   make target_name
#
# 下面 all 是一个 target，它依赖另一个 target：hello，
# 意味着要构建 all，首先需要构建 hello。而 all 的 commands
# 部分为空，表示构建 all 不需要额外命令。
#
# .PHONY 表示 all 不是一个真实会生成的文件，而是一个“伪目标”。
#
.PHONY: all
all: hello

#
# 由于后面需要多次使用 main.o 等目标文件列表，这里赋值给变量
# objects。
#
objects := main.o

#
# hello 是我们最终要生成的可执行文件名，它依赖 objects 中的
# 所有目标文件。
#
# 它的 commands 部分使用 CXX 指定的编译器将所有目标文件链接
# 成 hello 可执行文件。
#
hello: $(objects)
	$(CXX) -o $@ $(objects)

# main.o 目标文件依赖 main.cpp 源文件。
main.o: main.cpp
	$(CXX) -c main.cpp

#
# clean 用于清除构建生成的临时文件、目标文件和可执行文件。
# 和 all 类似，它是一个“伪目标”。
#
.PHONY: clean
clean:
	rm -f hello $(objects)

```

### Step_4

开始介绍CMake

```cmake
cmake_minimum_required(VERSION 3.9)
project(answer)

add_executable(answer main.cpp answer.cpp)
```

经典三行，第一行指定CMake的最低版本，第二行指定project的名字，第三行添加一个executable可执行文件add_executable(answer[^ 可执行文件名] main.cpp answer.cpp[^ 依赖的两个cpp文件])

生成 & 构建 & 运行命令：

```shell
cmake -B build      # 生成构建目录，-B 指定生成的构建系统代码放在 build 目录
cmake --build build # 执行构建
./build/answer      # 运行 answer 程序
```