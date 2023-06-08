---
title: "Markdown 语法"
---
# Markdown语法及Typora输入

## 标题

通过输入“# text”创建标题

可以使用

​	#

​	至

​	######

创建一级到六级的标题

## 引用

Markdown 使用电子邮件样式>字符进行块引用。它们表示为：

> 这是一个引用
>
> > 引用的级别




## 水平线

---

输入---或***，按换行键将绘制一条水平线

---

## 代码块

快捷键 Ctrl + Shift + K 生成一个代码块

键入```也会生成代码块

```
text文本
```

```c
选择语言
C代码
	printf("hello,world!");
```

## 表格

输入 `| First Header | Second Header |` 并按下 `return` 键将创建一个包含两列的表。

| First Header | Second Header |
| :----------: | :-----------: |
|  这是第一行  |  这是第二列   |

创建表后，焦点在该表上将弹出一个表格工具栏，您可以在其中调整表格，对齐或删除表格。可以使用上下文菜单来复制和添加/删除列/行。

在 markdown 源代码中，它们看起来像这样：

```
| First Header  | Second Header |
| ------------- | ------------- |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |
```

您还可以在表格中包括内联 Markdown 语法，例如链接，粗体，斜体或删除线。

最后，通过在标题行中包含冒号：您可以将文本定义为左对齐，右对齐或居中对齐：

```
| Left-Aligned  | Center Aligned  | Right Aligned |
| :------------ |:---------------:| -----:|
| col 3 is      | some wordy text | $1600 |
| col 2 is      | centered        |   $12 |
| zebra stripes | are neat        |    $1 |
```

最左侧的冒号表示左对齐的列; 最右侧的冒号表示右对齐的列; 两侧的冒号表示中心对齐的列。

## 脚注

`像这样创建脚注[^footnote].`

`[^footnote]:Here is the *text* of the **footnote**.`

效果类似于[^1]  

[^1]:内容

## 链接

Markdown 支持两种类型的链接：内联和引用。

在这两种样式中，链接文本都写在[方括号]内。

要创建内联链接，请在链接文本的结束方括号后立即使用一组常规括号。在常规括号内，输入URL地址，以及可选的用引号括起来的链接标题。



### 参考链接

```
This is [an example][id] reference-style link.

然后，在文档中的任何位置，您可以单独定义链接标签，如下所示：

[id]: http://example.com/  "Optional Title Here"
```

在typora中，它们将呈现为：

This is [an example][id] reference-style link.

然后，在文档中的任何位置，您可以单独定义链接标签，如下所示：

[id]: http://example.com/  "Optional Title Here"



```
This is [an example][id] reference-style link.

然后，在文档中的任何位置，您可以单独定义链接标签，如下所示：

[id]: http://example.com/  "Optional Title Here"
```





## 更改字体、大小、颜色

```
<font face="黑体">我是黑体字</font>
<font face="微软雅黑">我是微软雅黑</font>
<font face="STCAIYUN">我是华文彩云</font>
<font color=red>我是红色</font>
<font color=#008000>我是绿色</font>
<font color=Blue>我是蓝色</font>
<font size=5>我是尺寸</font>
<font face="黑体" color=green size=5>我是黑体，绿色，尺寸为5</font>
```

<font face="黑体">我是黑体字</font>
<font face="微软雅黑">我是微软雅黑</font>
<font face="STCAIYUN">我是华文彩云</font>
<font color=red>我是红色</font>
<font color=#008000>我是绿色</font>
<font color=Blue>我是蓝色</font>
<font size=5>我是尺寸</font>
<font face="黑体" color=green size=5>我是黑体，绿色，尺寸为5</font>

## 列表

Markdown 支持有序列表和无序列表。无序列表使用星号`*`、加号`+`或是减号`-`作为列表标记 ；如果希望是有序列表，在文字前加上`1.2.3.`即可。

注：`-`、`1.`和文字间要保留一个字符的空格。

**无序列表 示例：**

```undefined
* 第一项
* 第二项
* 第三项

+ 第一项
+ 第二项
+ 第三项


- 第一项
- 第二项
- 第三项
```

效果如下：

* 第一项
* 第二项
* 第三项

+ 第一项
+ 第二项
+ 第三项


- 第一项

- 第二项

- 第三项

  `三种列表形式效果相同`

------

**有序列表 示例：**

```undefined
1. 第一项
2. 第二项
3. 第三项
```

效果如下：

1. 第一项
2. 第二项
3. 第三项

------

**列表嵌套 示例：**
 列表嵌套只需在子列表中的选项前面添加四个空格即可

```undefined
1. 第一项：
    - 第一项嵌套的第一个元素
    - 第一项嵌套的第二个元素
2. 第二项：
    - 第二项嵌套的第一个元素
    - 第二项嵌套的第二个元素
```

效果如下：

1. 第一项：
   - 第一项嵌套的第一个元素
   - 第一项嵌套的第二个元素
2. 第二项：
   - 第二项嵌套的第一个元素
   - 第二项嵌套的第二个元素

- 第零层列表嵌套
  - 第一层列表嵌套
    - 第二层列表嵌套
      - 之后的嵌套与第二层样式相同

> Blocks quote from quote.
>
> and I can make sub quotes
>
> > right
> >
> > and there is chart in the quotes
> >
> > - there it is!
> >   - and there is sub chart!
> >     - haha it's fun isn't it?
> >       - sad! There is no more sub charts
> >   - you can use Shift+Tab to return to last level of chart
>
> you can use ***Enter*** to cancel the nearest quote
