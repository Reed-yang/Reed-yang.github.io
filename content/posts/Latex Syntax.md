---
title: "Latex Syntax"
---
### 文件用途一览

![image-20220530171500962](https://s2.loli.net/2022/05/30/kBfx8MWZbC7Kinv.png)

### 文字与字符

- 换行与空格：*行末单个换行*或者*连续的若干空白符*视为一个空格，符两个换行符输出一个空行，多个空行被视为一个空行

- 注释：%之后后直到行末，都视为注释、

- 转义字符与特殊符号：

  ![image-20220530163305457](https://s2.loli.net/2022/05/30/Ej3eNwDnkCRhoPU.png)

- 手动断行，断页：

  ```latex
  
ewline %新建页
  
ewpage %新建行
  ```



### 文档元素

- 章节和目录：

  - 章节标题：通过不同的命令分割为章、节、小节。三个标准文档类 article、report 和 book提供了划分章节的命令：

    ```latex
    