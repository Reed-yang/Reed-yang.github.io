---
title: "Latex Syntax"
date: 2022-05-30T16:21:56+00:00
tags: ['uncategorized']
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
  \newline %新建页
  \newpage %新建行
  ```

### 文档元素

- 章节和目录：

  - 章节标题：通过不同的命令分割为章、节、小节。三个标准文档类 article、report 和 book提供了划分章节的命令：

    ```latex
    \chapter{⟨title⟩} \section{⟨title⟩} \subsection{⟨title⟩}
    \subsubsection{⟨title⟩} \paragraph{⟨title⟩} \subparagraph{⟨title⟩}
    ```

  - 目录：在$\LaTeX$中生成目录很容易，只需在合适的位置使用命令`\tableofcontents`指令即可

-  标题页：$\LaTeX$支持生成简单的标题页，首先需给定标题和作者等信息：`\title{⟨title⟩} \author{⟨author⟩} \date{⟨date⟩}`信息给定之后，就可以用`\maketitle`命令生成简单的标题页

- 特殊环境：

  - 列表
  - 对齐环境
  - 引用环境
  - 代码环境
  - 引用环境

- 表格

- 图片

- 浮动体

  - 内容丰富的文章或者书籍往往包含许多图片和表格等内容。这些内容的尺寸往往太大，导致分页困难。LATEX 为此引入了浮动体的机制，令大块的内容可以脱离上下文，放置在合适的位置。

    LATEX 预定义了两类浮动体环境 figure 和 table。习惯上 figure 里放图片，table 里放 表格，但并没有严格限制，可以在任何一个浮动体里放置文字、公式、表格、图片等等任意内容。

    以 table 环境的用法举例，figure 同理：

    ```latex
    \begin{table}[⟨placement⟩]
    …
    \end{table}
    ```

    ![image-20220530181803172](https://s2.loli.net/2022/05/30/M6BUNgfbZwDFvjW.png)
