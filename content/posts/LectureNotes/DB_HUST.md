---
title: "DB_HUST"
---
[TOC]



## I	关系代数

交、并、差

广义笛卡尔积 $ 	imes $

选择运算 $\sigma$

投影 $ \Pi $

连接：$ \mathop{\Join} \limits_{A 	heta B} $ 从两个关系的广义笛卡尔积中选取给定属性间满足一定条件的元组

自然连接：$ \Join $ 从两个关系的广义笛卡儿积中选取在相同属性列上取值相等的元组，并去掉重复的列

## II	SQL

<img src="http://img.reedyoung.cn/image-20230417090912383.png" alt="image-20230417090912383" style="zoom:33%;" />

- 基本表的定义：

  ```sql
  CREATE TABLE C (
    C# CHAR(4),
    CNAME CHAR(10) NOT NULL,
    TEACHER CHAR(8),
    PRIMARY KEY (C#)
  );
  ```

  

  
