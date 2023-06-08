---
title: "MIT6.031 Software Construction"
---
[TOC]

## Before Start

This notes is based on the MIT course [6.031](https://web.mit.edu/6.031/www/sp21/), but the video materials are from former version 6.005(2016sp) at edx, moreover, the original videos on edx has been lost, nevertheless [there](https://www.bilibili.com/video/BV1Tp4y197XX) it is on bilibili.

**NOTICE** that the lated 6.031 from sp22 has chosen TypeScript as the progamming language, since the writer wanted wanted to learn OOP in JAVA in the beginning, so just choose the older version.

**NOTICE** that (states from prof. Robert Miller) the reading materials and the videos has same information, and in videos professer basicly just read the materials, you can ignore the viedeos and just learn from text, if you want.

## Getting Started

关于多版本JDK，[多版本](https://blog.csdn.net/HeyVIrBbox/article/details/125635535)与[新版Path变化](https://blog.csdn.net/qq_43501219/article/details/128398256)

run into errors when installing eclipse for 6.031, choose basic version from Internet instead

## [From Python to Java](http://kennethalambert.com/pythontojava/)

### Program Structure and Execution

#### Hello World!

The simplest version of this program defines a **main** method within a class:

 ```java
 public class HelloWorld{
 
    static public void main(String[] args){
      System.out.println("Hello world!");
   }
 }
 ```

The source code defines but does not call this method. At program startup, the compiled class **HelloWorld** is loaded into the JVM. The JVM then calls **main**, which is a class method in **HelloWorld**.

A Java application must include at least one class that defines a **main** method. The byte code file for this class is the entry point for program execution.

### Data Types and Expressions

#### Value types vs. Reference types

In programming languages, there are two main types of data: value types and reference types. Understanding reference types is essential because they behave differently from value types and can lead to unexpected behavior if not used correctly.

#### Type Conversion

The simplest way to convert any value to a string is to concatenate it to an empty string, as follows:

```java
"" + 3.14

"" + 45
```

### Terminal Input and Output

#### Terminal Input

The **Scanner** class is used for the input of text and numeric data from the keyboard. The programmer instantiates a **Scanner** and uses the appropriate methods for each type of data being input.

Create a **Scanner** object attached to the keyboard:

```java
Scanner keyboard = new Scanner(System.in);
```

Input a line of text as a string:

```java
String s = keyboard.nextLine("Enter your name: ");
```

Input an integer:

```java
int i = keyboard.nextInt("Enter your age: ");
```

Input a double:

```java
double d = keyboard.nextDouble("Enter your wage: ");
```

*Caution*: using the same scanner to input strings *after* numbers can result in logic errors. Thus, it is best to use separate scanner objects for numbers and text.

### **for** Loops

Two types:

1. 

```java
        for (<type> <variable> : <iterable>){
            <statement>
            …
            <statement>
        }
```

​			exp:

```java
        for (String s : aListOfStrings){
            System.out.println(s);
        }
```

2. 

```java
        for (<initializer>; <continuation>; <update>){
            <statement>
            …
            <statement>
        }
```

​			exp:

```java
        for (int i = 1; i <= 10; i++){
            System.out.println(i);
        }
```

### Interface

注解：Java中的接口是一个与实现无关的定义。它只定义了必须实现的方法集合，而没有提供实现细节。一个类实现接口时，必须提供接口中定义的所有方法的具体实现。因此，接口可以用于在多个类之间定义共同行为的规范，同时保持类的独立性。

### Collections

#### Map

key / value 集合映射

#### Iterators

An iterator is an object that supports the traversal of a collection. The compiler generates code that uses an iterator whenever it sees an enhanced **for** loop.

All collections implement the **Iterable** interface. This interface includes a single method, **iterator()**, which returns an iterator object.

An iterator object implements the **Iterator** interface. This interface includes the methods **next()**, **hastNext()**, and **remove()**.

Like collections, iterators can be generic. Thus, the generic collection’s element type must be specified when a variable of type **Iterator** is declared.

Example use:

```java
# Create a list of strings
List<String> lyst = new ArrayList<String>();

# Add some strings to lyst
    
# Open an iterator on lyst
Iterator<String> i = lyst.iterator();

# Print all the strings in lyst using the iterator
while (i.hasNext()){
    String s = i.next();
    System.out.println(s);
} 
```

### Defining Classes



##  [Reading 1: Static Checking](http://web.mit.edu/6.031/www/sp21/classes/01-static-checking)

statically-typed language

Static checking: find errors & bugs before running

### Types

**primitive types**, among them:

- `int` (for integers like 5 and -200, but limited to the range about ± 231, or roughly ± 2 billion)
- `long` (for larger integers up to about ± 263)
- `boolean` (for true or false)
- `double` (for floating-point numbers, which represent a subset of the real numbers)
- `char` (for single characters like `'A'` and `'$'`)

**object types**, for example:

- `String` represents a sequence of characters, like a Python string.
- `BigInteger` represents an integer of arbitrary size, so it acts like a Python integer.

Mainly to discriminate that **lowercase** like `int` is primitive, while **uppercase** like `String` is object

### Arrays and collections

`List` type: 

```java
List<Integer> list = new ArrayList<Integer>();
```

And here are some of its operations:

- indexing: `list.get(2)`
- assignment: `list.set(2, 0)`
- length: `list.size()`

`List` is an **interface **(a type that can’t be constructed directly); `ArrayList` is a **class**, a concrete type that provides implementations of those operations.

Why `List<Integer>` and not `List<int>`? Unfortunately, we can’t write `List<int>`. Lists only know how to deal with object types, not primitive types. Each primitive type has an equivalent object type: e.g. `int` and `Integer`, `long` and `Long`, `float` and `Float`, `double` and `Double`.

### Iterating

A `for` loop steps through the elements of an array or a `List`, just as in Python, though the syntax looks a little different. For example:

```java
// find the maximum point of a hailstone sequence stored in list
int max = 0;
for (int x : list) {
    max = Math.max(x, max);
}
```

### Methods

In Java, statements generally have to be inside a method, and every method has to be in a class

`public` means that any code, anywhere in your program, can refer to the class or method

`static` means that the method is a function that doesn’t take a `self` parameter (which in Java is called `this`, and is passed implicitly, so you won’t ever see it as an explicit method parameter). Static methods aren’t called on an **object**. Contrast that with the `List` `add()` method or the `String` `length()` method, for example, which require an object to come first. Instead, the right way to call a static method uses the class name instead of an object reference: `Hailstone.hailstoneSequence(83)`.

### Goal of 6.031

- **Safe from bugs**. Correctness (correct behavior right now) and defensiveness (correct behavior in the future) are required in any software we build.
- **Easy to understand**. The code has to communicate to future programmers who need to understand it and make changes in it (fixing bugs or adding new features). That future programmer might be you, months or years from now. You’ll be surprised how much you forget if you don’t write it down, and how much it helps your own future self to have a good design.
- **Ready for change**. Software always changes. Some designs make it easy to make changes; others require throwing away and rewriting a lot of code.



## Reading 2: Basic Java

Java compiler must also be certain that every variable has been assigned a value before we attempt to access its value.

### Mutable vs. Immutable

#### immutable values

```java
String s = "a";
s = s + "b";
```

`String` is an example of an *immutable* type, thus:

<img src="http://img.reedyoung.cn/image-20230414161258274.png" alt="image-20230414161258274" style="zoom:50%;" />

By contrast, [`StringBuilder`](http://docs.oracle.com/en/java/javase/15/docs/api/java.base/java/lang/StringBuilder.html) (another built-in Java class) is a *mutable* object

#### Unreassignable references

keyword `final`

### ==

But the other mistake, using `==` to compare object values for equality, is much more painful, because `==` is overloaded in Java. When used on object types, `==` tests whether the two expressions refer to the same object in memory. In terms of the snapshot diagrams we’ve been drawing, two references are `==` if their arrows point to the same object bubble. In Python, this operator is called `is`.

### Java Collections

#### Array vs. ArrayList

view [this](https://blog.csdn.net/senxu_/article/details/126272908)

## Reading 3: Testing

- Systematic Testing

  Test suite properties:

  - Correct

  - Thorough

  - Small

- Choosing test cases by partitioning

- JUnit

  - `@Test`

  - `assertEquals`, `assertTrue`, and `assertFalse`
