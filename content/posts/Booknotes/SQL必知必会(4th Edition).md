---
title: "SQL必知必会(4th Edition)"
date: 2023-04-17T10:12:21+00:00
tags: ['Booknotes']
---

#### SELECT, FROM, ORDER BY

```sql
SELECT prod_id, prod_price, prod_name 
FROM Products 
ORDER BY 2, 3; 
```

关键字一般大写

`ORDER BY 2, 3; `可以按照所选取列进行排序

#### WHERE

```SQL
SELECT prod_name, prod_price 
FROM Products 
WHERE prod_price = 3.49; 
```

tip: 同时使用WHERE和ORDER BY, 应让ORDER BY 在WHERE 之后

<img src="http://img.reedyoung.cn/image-20230417101907765.png" alt="image-20230417101907765" style="zoom: 67%;margin: 0 auto;" />

#### 范围查询BETWEEN AND

```SQL
SELECT prod_name, prod_price 
FROM Products 
WHERE prod_price BETWEEN 5 AND 10; 
```

#### 与WHERE组合: AND, OR, IN, NOT

以IN为例: 

```SQL
SELECT prod_name, prod_price 
FROM Products 
WHERE vend_id IN ( 'DLL01', 'BRS01' ) 
ORDER BY prod_name; 
```

实际上，IN与OR功能一致，但更清晰

#### 通配符

- LIKE: 匹配操作符，后跟格式字符串

- %: 表示任何字符出现任意次 数

  ```sql
  SELECT prod_id, prod_name 
  FROM Products 
  WHERE prod_name LIKE 'Fish%'; 
  ```

  输出：

  ```SQL
  prod_id 	prod_name 
  ------- 	------------------ 
  BNBG01  	Fish bean bag toy
  ```

- _: 只匹配单个字符

- []: 指定一个字符集, 匹配方括号中任意一个字符，它也只能匹配单个字符。

  ```sql
  SELECT cust_contact 
  FROM Customers 
  WHERE cust_contact LIKE '[JM]%' 
  ORDER BY cust_contact; 
  ```

  输出▼

  ---

  ```bash
  cust_contact 
  ----------------- 
  Jim Jones 
  John Smith 
  Michelle Green 
  ```

#### 计算字段
