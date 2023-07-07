---
title: "The missing semester"
date: 2022-05-03T17:52:34+00:00
tags: ['uncategorized']
---
# The missing semester

## Lecture 1 The Shell

### shell 是什么？

广泛使用的文字接口。

课程使用Bourne Again Shell, 简称 “bash” 。 是最广泛使用的一种shell。

在输入指令前需要打开*终端*（通常内置）。

### 使用shell

- 当打开一个*Terminal*时会显示如

  ```
  [jon@xpanse missing-semester]$ 
  ```

  分别表示 用户名 @ 机器名 当前所在路径。

- 用空格来分隔程序的不同参数，若想输入含空格的字符串作为参数，可以使用“Hello world”，也可以使用Hello\ world转义空格。

- shell实际上类似于一种编程语言，不仅仅能执行特定的程序或转递参数，甚至可以执行while loop、conditional(条件)等语句，可以定义函数，可以设置变量等等（后续课程将会详细介绍）。

- *environment variable环境变量*	shell运行前内置的参数

- PATH (路径变量) 调用指令echo $PATH实例：

  ```
  missing:~$ /bin/echo $PATH
  /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
  ```

- which指令

- 绝对路径/相对路径

  以 `/` 开头，那么它是一个 *绝对路径*，其他的都是 *相对路径* 。

  路径中，`.` 表示的是当前目录，而 `..` 表示上级目录。

- pwd print working directory

- cd change directory

- dot means current directory/dot dot means parent directory

- ls list the files in the current directory

- tilde `~` always expands to the home directory

- `CD -`回到上次的地址

- `ls --help`显示help菜单，call anything doesn't take a value a flag, anything that does take a value an option.

- `ls -l`use a long list format，例如：

	```shell
  missing:~$ ls -l /home
  drwxr-xr-x 1 missing  users  4096 Jun 15  2019 missing
	```

	这个参数可以打印出更加详细地列出目录下文件或文件夹的信息。首先，本行第一个字符 `d` 表示 `missing` 是一个目录。然后接下来的九个字符，每三个字符构成一组。 （`rwx`）. 它们分别代表了文件所有者（`missing`），用户组（`users`） 以及其他所有人具有的权限。其中 `-` 表示该用户不具备相应的权限。从上面的信息来看，只有文件所有者可以修改（`w`），`missing` 文件夹 （例如，添加或删除文件夹中的文件）。为了进入某个文件夹，用户需要具备该文件夹以及其父文件夹的“搜索”权限（“可执行`execute`”：`x`）权限表示。为了列出它的包含的内容，用户必须对该文件夹具备读权限（`r`）。对于文件来说，权限的意义也是类似的。注意，`/bin` 目录下的程序在最后一组，即表示所有人的用户组中，均包含 `x` 权限，也就是说任何人都可以执行这些程序。[`ls -l`指令详解](https://blog.csdn.net/sjzs5590/article/details/8254527)

- 几个常用命令是，例如 `mv`（`move`用于重命名或移动文件）、 `cp`（`copy`拷贝文件）以及 `mkdir`（`make directory`新建文件夹），`rm`（删除文件）。

- `mv`

- `cp`

- `rm`指令*rm*在*linux*中不具有递归性，即只删除文件而不能删除目录

  `rmdir`*remove directory*只能删除空文件夹

- `man`程序，对某个程序使用*man*将展示该程序的manual(类似于--help，一般可读性更强)

- `Ctrl + L`指令将一键clear the terminal

### 在程序间创建连接

- `stream`流

  `input stream`输入流

  ​	默认输入流是键盘在终端的输入

  `output stream`输出流

  ​	默认的输出流是程序在终端的输出

  `重定向`

  ​	最简单的重定向是 `< file` 和 `> file`。这两个命令可以将程序的输入输出流分别重定向到文件：

  ```shell
  missing:~$ echo hello > hello.txt
  missing:~$ cat hello.txt
  hello
  //cat(concatenate)
  missing:~$ cat < hello.txt
  hello
  missing:~$ cat < hello.txt > hello2.txt
  missing:~$ cat hello2.txt
  hello
  ```

  还可以使用 `>>` 来向一个文件追加内容。使用管道（*pipes*），能够更好的利用文件重定向。 `|` 操作符允许将一个程序的输出和另外一个程序的输入连接起来：

  ```shell
  missing:~$ cat < hello.txt >> hello2.txt
  hello
  hello
  //`>>`向 hello2.txt 后追加 hello.txt 的内容
  missing:~$ ls -l / | tail -n1
  drwxr-xr-x 1 root  root  4096 Jun 20  2019 var
  missing:~$ curl --head --silent google.com | grep --ignore-case content-length | cut --delimiter=' ' -f2
  219
  ```
  会在数据清理一章中更加详细的探讨如何更好的利用管道。

### root user

根用户是拥有最高（任意）权限的用户。通常并不会以根用户的身份直接登录系统，因为可能会造成某些错误而破坏系统。 取而代之的是使用 `sudo` 命令，以 su（super user 或 root 的简写）的身份执行一些操作。 当遇到拒绝访问（permission denied）的错误时，通常是因为此时必须是根用户才能操作。

向 `sysfs` 文件写入内容必须以根用户身份才能进行。系统被挂载在 `/sys` 下，`sysfs` 文件则暴露了一些内核（kernel）参数。 因此，不需要借助任何专用的工具，就可以轻松地在运行期间配置系统内核。**注意 Windows 和 macOS 没有这个文件**

例如，笔记本电脑的屏幕亮度写在 `brightness` 文件中，它位于

```
/sys/class/backlight
```

通过将数值写入该文件，我们可以改变屏幕的亮度。现在，可能发生的是：

```
$ sudo find -L /sys/class/backlight -maxdepth 2 -name '*brightness*'
/sys/class/backlight/thinkpad_screen/brightness
$ cd /sys/class/backlight/thinkpad_screen
$ sudo echo 3 > brightness
An error occurred while redirecting file 'brightness'
open: Permission denied
```

然而，还是得到了一个错误信息。但已经使用了 `sudo` 命令！关于 shell，有件事必须要知道。**`|`、`>`、和 `<` 是通过 shell 执行的，而不是被各个程序单独执行。 `echo` 等程序并不知道 `|` 的存在，它们只知道从自己的输入输出流中进行读写。 对于上面这种情况， *shell* (权限为您的当前用户) 在设置 `sudo echo` 前尝试打开 brightness 文件并写入，但是系统拒绝了 shell 的操作因为此时 shell 不是根用户。**

明白这一点后，可以这样操作：

```
$ echo 3 | sudo tee brightness
```

因为打开 `/sys` 文件的是 `tee` 这个程序，并且该程序以 `root` 权限在运行，因此操作可以进行。 这样您就可以在 `/sys` 中愉快地玩耍了，例如修改系统中各种LED的状态（路径可能会有所不同）：

```
$ echo 1 | sudo tee /sys/class/leds/input6::scrolllock/brightness
```

### Assignment Ⅰ

>[习题解答](https://missing-semester-cn.github.io/missing-notes-and-solutions/2020/solutions//course-shell-solution) 本课程中的每节课都包含一系列练习题。有些题目是有明确目的的，另外一些则是开放题，例如“尝试使用 X 和 Y”，我们强烈建议您一定要动手实践，用于尝试这些内容。 此外，我们没有为这些练习题提供答案。如果有任何困难，您可以发送邮件给我们并描述你已经做出的尝试，我们会设法帮您解答。
>
>1. 本课程需要使用类Unix shell，例如 Bash 或 ZSH。如果您在 Linux 或者 MacOS 上面完成本课程的练习，则不需要做任何特殊的操作。如果您使用的是 Windows，则您不应该使用 cmd 或是 Powershell；您可以使用[Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/)或者是 Linux 虚拟机。使用`echo $SHELL`命令可以查看您的 shell 是否满足要求。如果打印结果为`/bin/bash`或`/usr/bin/zsh`则是可以的。
>
>2. 在 `/tmp` 下新建一个名为 `missing` 的文件夹。
>
>3. 用 `man` 查看程序 `touch` 的使用手册。
>
>4. 用 `touch` 在 `missing` 文件夹中新建一个叫 `semester` 的文件。
>
>5. 将以下内容一行一行地写入
>
>   ```plaintext
>   semester
>   ```
>
>   文件：
>
>   ```
>    #!/bin/sh
>    curl --head --silent https://missing.csail.mit.edu
>   ```
>
>   第一行可能有点棘手， `#` 在Bash中表示注释，而 `!` 即使被双引号（`"`）包裹也具有特殊的含义。 单引号（`'`）则不一样，此处利用这一点解决输入问题。更多信息请参考 [Bash quoting 手册](https://www.gnu.org/software/bash/manual/html_node/Quoting.html)
>
>6. 尝试执行这个文件。例如，将该脚本的路径（`./semester`）输入到您的shell中并回车。如果程序无法执行，请使用 `ls` 命令来获取信息并理解其不能执行的原因。
>
>7. 查看 `chmod` 的手册(例如，使用 `man chmod` 命令)
>
>8. 使用 `chmod` 命令改变权限，使 `./semester` 能够成功执行，不要使用 `sh semester` 来执行该程序。您的 shell 是如何知晓这个文件需要使用 `sh` 来解析呢？更多信息请参考：[shebang](https://en.wikipedia.org/wiki/Shebang_(Unix))
>
>9. 使用 `|` 和 `>` ，将 `semester` 文件输出的最后更改日期信息，写入主目录下的 `last-modified.txt` 的文件中
>
>10. 写一段命令来从 `/sys` 中获取笔记本的电量信息，或者台式机 CPU 的温度。注意：macOS 并没有 sysfs，所以 Mac 用户可以跳过这一题。

作业笔记

- `touch`修改文件或目录的时间属性，若该文件不存在，将新建一个文件。

  *`symbolic link 软连接`*

  *`Timestamp 时间戳`*
