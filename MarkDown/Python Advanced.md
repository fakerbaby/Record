[toc]

### 遍历技巧

在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来：

```python
>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k, v in knights.items():
...     print(k, v)
...
gallahad the pure
robin the brave
```

在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到：

```python
>>> for i, v in enumerate(['tic', 'tac', 'toe']):
...     print(i, v)
...
0 tic
1 tac
2 toe
```

同时遍历两个或更多的序列，可以使用 zip() 组合：

```python
>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
...     print('What is your {0}?  It is {1}.'.format(q, a))
...
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.
```

要反向遍历一个序列，首先指定这个序列，然后调用 reversesd() 函数：

```python
>>> for i in reversed(range(1, 10, 2)):
...     print(i)
...
9
7
5
3
1
```

要按顺序遍历一个序列，使用 sorted() 函数返回一个已排序的序列，并不修改原值：

```python
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for f in sorted(set(basket)):
...     print(f)
...
apple
banana
orange
pear
```







## *args & *kwagrs

这里的不定的意思是：预先并不知道, 函数使用者会传递多少个参数给你, 所以在这个场景下使用这两个关键字。 `*args` 是用来发送一个非键值对的可变数量的参数列表给一个函数.

`**kwargs` 允许你将不定长度的**键值对**, 作为参数传递给一个函数。 如果你想要在一个函数里处理**带名字的参数**, 你应该使用`**kwargs`。

那么如果你想在函数里同时使用所有这三种参数， 顺序是这样的：

```python
some_func(fargs, *args, **kwargs)
```



# 调试（Debugging)

```bash
python -m pdb my_script.py
```

这会触发debugger在脚本第一行指令处停止执行。这在脚本很短时会很有帮助。你可以通过(Pdb)模式接着查看变量信息，并且逐行调试

### 从脚本内部运行

同时，你也可以在脚本内部设置断点，这样就可以在某些特定点查看变量信息和各种执行时信息了。这里将使用`pdb.set_trace()`方法来实现。举个例子：

```python
import pdb

def make_bread():
    pdb.set_trace()
    return "I don't have time"

print(make_bread())
```

试下保存上面的脚本后运行之。你会在运行时马上进入debugger模式。现在是时候了解下debugger模式下的一些命令了。

##### 命令列表：

- `c`: 继续执行
- `w`: 显示当前正在执行的代码行的上下文信息
- `a`: 打印当前函数的参数列表
- `s`: 执行当前代码行，并停在第一个能停的地方（相当于单步进入）
- `n`: 继续执行到当前函数的下一行，或者当前行直接返回（单步跳过）

单步跳过（`n`ext）和单步进入（`s`tep）的区别在于， 单步进入会进入当前行调用的函数内部并停在里面， 而单步跳过会（几乎）全速执行完当前行调用的函数，并停在当前函数的下一行。





# Generator

首先我们要理解迭代器(iterators)。根据维基百科，迭代器是一个让程序员可以遍历一个容器（特别是列表）的对象。然而，一个迭代器在遍历并读取一个容器的数据元素时，并不会执行一个迭代。你可能有点晕了，那我们来个慢动作。换句话说这里有三个部分：

- 可迭代对象(Iterable)
- 迭代器(Iterator)
- 迭代(Iteration)

上面这些部分互相联系。我们会先各个击破来讨论他们，然后再讨论生成器(generators).

# 可迭代对象(Iterable)

Python中任意的对象，只要它定义了可以返回一个迭代器的`__iter__`方法，或者定义了可以支持下标索引的`__getitem__`方法(这些双下划线方法会在其他章节中全面解释)，那么它就是一个可迭代对象。简单说，可迭代对象就是能提供迭代器的任意对象。那迭代器又是什么呢？



# 迭代器(Iterator)

任意对象，只要定义了`next`(Python2) 或者`__next__`方法，它就是一个迭代器。就这么简单。现在我们来理解迭代(iteration)

# 迭代(Iteration)

用简单的话讲，它就是从某个地方（比如一个列表）取出一个元素的过程。当我们使用一个循环来遍历某个东西时，这个过程本身就叫迭代。现在既然我们有了这些术语的基本理解，那我们开始理解生成器吧。

# 生成器(Generators)

生成器也是一种迭代器，但是你只能对其迭代一次。这是因为它们并没有把所有的值存在内存中，而是在运行时生成值。你通过遍历来使用它们，要么用一个“for”循环，要么将它们传递给任意可以进行迭代的函数和结构。大多数时候生成器是以函数来实现的。然而，它们并不返回一个值，而是`yield`(暂且译作“生出”)一个值。这里有个生成器函数的简单例子：

```python
def generator_function():
    for i in range(10):
        yield i

for item in generator_function():
    print(item)

# Output: 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
```

这个案例并不是非常实用。生成器最佳应用场景是：你不想同一时间将所有计算出来的大量结果集分配到内存当中，特别是结果集里还包含循环。

> 译者注：这样做会消耗大量资源 

许多Python 2里的标准库函数都会返回列表，而Python 3都修改成了返回生成器，因为生成器占用更少的资源。 

下面是一个计算斐波那契数列的生成器：

```python
# generator version
def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b
```

函数使用方法如下：

```
for x in fibon(1000000):
    print(x)
```

用这种方式，我们可以不用担心它会使用大量资源。然而，之前如果我们这样来实现的话：

```python
def fibon(n):
    a = b = 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result
```

这也许会在计算很大的输入参数时，用尽所有的资源。我们已经讨论过生成器使用一次迭代，但我们并没有测试过。在测试前你需要再知道一个Python内置函数：`next()`。它允许我们获取一个序列的下一个元素。那我们来验证下我们的理解：

```python
def generator_function():
    for i in range(3):
        yield i

gen = generator_function()
print(next(gen))
# Output: 0
print(next(gen))
# Output: 1
print(next(gen))
# Output: 2
print(next(gen))
# Output: Traceback (most recent call last):
#            File "<stdin>", line 1, in <module>
#         StopIteration
```

我们可以看到，在`yield`掉所有的值后，`next()`触发了一个`StopIteration`的异常。基本上这个异常告诉我们，所有的值都已经被`yield`完了。你也许会奇怪，为什么我们在使用`for`循环时没有这个异常呢？啊哈，答案很简单。`for`循环会自动捕捉到这个异常并停止调用`next()`。你知不知道Python中一些内置数据类型也支持迭代哦？我们这就去看看：

```python
my_string = "Yasoob"
next(my_string)
# Output: Traceback (most recent call last):
#      File "<stdin>", line 1, in <module>
#    TypeError: str object is not an iterator
```

好吧，这不是我们预期的。这个异常说那个`str`对象不是一个迭代器。对，就是这样！它是一个可迭代对象，而不是一个迭代器。这意味着它支持迭代，但我们不能直接对其进行迭代操作。那我们怎样才能对它实施迭代呢？是时候学习下另一个内置函数，`iter`。它将根据一个可迭代对象返回一个迭代器对象。这里是我们如何使用它：

```python
my_string = "Yasoob"
my_iter = iter(my_string)
next(my_iter)
# Output: 'Y'
```

现在好多啦。我肯定你已经爱上了学习生成器。一定要记住，想要完全掌握这个概念，你只有使用它。确保你按照这个模式，并在生成器对你有意义的任何时候都使用它。你绝对不会失望的！



# Map，Filter 和 Reduce

Map，Filter 和 Reduce 三个函数能为函数式编程提供便利。我们会通过实例一个一个讨论并理解它们。



### Map

`Map`会将一个函数映射到一个输入列表的所有元素上。这是它的规范：

**规范**

```python
map(function_to_apply, list_of_inputs)
```

大多数时候，我们要把列表中所有元素一个个地传递给一个函数，并收集输出。比方说：

```python
items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**2)
```

`Map`可以让我们用一种简单而漂亮得多的方式来实现。就是这样：

```python
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
```

大多数时候，我们使用匿名函数(lambdas)来配合`map`, 所以我在上面也是这么做的。 不仅用于一列表的输入， 我们甚至可以用于一列表的函数！

```python
def multiply(x):
        return (x*x)
def add(x):
        return (x+x)

funcs = [multiply, add]
for i in range(5):
    value = map(lambda x: x(i), funcs)
    print(list(value))
    # 译者注：上面print时，加了list转换，是为了python2/3的兼容性
    #        在python2中map直接返回列表，但在python3中返回迭代器
    #        因此为了兼容python3, 需要list转换一下

# Output:
# [0, 0]
# [1, 2]
# [4, 4]
# [9, 6]
# [16, 8]
```



### Filter

顾名思义，`filter`过滤列表中的元素，并且返回一个由所有符合要求的元素所构成的列表，`符合要求`即函数映射到该元素时返回值为True. 这里是一个简短的例子：

```python
number_list = range(-5, 5)
less_than_zero = filter(lambda x: x < 0, number_list)
print(list(less_than_zero))  
# 译者注：上面print时，加了list转换，是为了python2/3的兼容性
#        在python2中filter直接返回列表，但在python3中返回迭代器
#        因此为了兼容python3, 需要list转换一下

# Output: [-5, -4, -3, -2, -1]
```

这个`filter`类似于一个`for`循环，但它是一个内置函数，并且更快。

注意：如果`map`和`filter`对你来说看起来并不优雅的话，那么你可以看看另外一章：列表/字典/元组推导式。

> 译者注：大部分情况下推导式的可读性更好



### Reduce

当需要对一个列表进行一些计算并返回结果时，`Reduce` 是个非常有用的函数。举个例子，当你需要计算一个整数列表的乘积时。

通常在 python 中你可能会使用基本的 for 循环来完成这个任务。

现在我们来试试 reduce：

```python
from functools import reduce
product = reduce( (lambda x, y: x * y), [1, 2, 3, 4] )

# Output: 24
```

# `set`(集合)数据结构

`set`(集合)是一个非常有用的数据结构。它与列表(`list`)的行为类似，区别在于`set`不能包含重复的值。
这在很多情况下非常有用。例如你可能想检查列表中是否包含重复的元素，你有两个选择，第一个需要使用`for`循环，就像这样：

```python
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)
### 输出: ['b', 'n']
```

但还有一种更简单更优雅的解决方案，那就是使用`集合(sets)`，你直接这样做：

```python
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = set([x for x in some_list if some_list.count(x) > 1])
print(duplicates)
### 输出: set(['b', 'n'])
```

集合还有一些其它方法，下面我们介绍其中一部分。

### 交集

你可以对比两个集合的交集（两个集合中都有的数据），如下：

```python
valid = set(['yellow', 'red', 'blue', 'green', 'black'])
input_set = set(['red', 'brown'])
print(input_set.intersection(valid))
### 输出: set(['red'])
```

### 差集

你可以用差集(difference)找出无效的数据，相当于用一个集合减去另一个集合的数据，例如：

```python
valid = set(['yellow', 'red', 'blue', 'green', 'black'])
input_set = set(['red', 'brown'])
print(input_set.difference(valid))
### 输出: set(['brown'])
```

你也可以用`{}`符号来创建集合，如：

```python
a_set = {'red', 'blue', 'green'}
print(type(a_set))
### 输出: <type 'set'>
```

集合还有一些其它方法，我会建议访问官方文档并做个快速阅读。





# 三元运算符

三元运算符通常在Python里被称为条件表达式，这些表达式基于真(true)/假(false)的条件判断，在Python 2.4以上才有了三元操作。

下面是一个伪代码和例子：

**伪代码:**

```python
#如果条件为真，返回真 否则返回假
condition_is_true if condition else condition_is_false
```

**例子:**

```python
is_fat = True
state = "fat" if is_fat else "not fat"
```

它允许用简单的一行快速判断，而不是使用复杂的多行`if`语句。 这在大多数时候非常有用，而且可以使代码简单可维护。



# `**装饰器**`

## 前置知识***闭包**

下面的代码介绍闭包的概念：

```python
 def outer():
     x = 1
     def inner():
          print(x)
     return inner
 
 foo = outer()
 foo()
 print(foo.__closure__)
 # 打印结果为
 # 1
 # (<cell at 0x00000000004AF2E8: int object at 0x000000006F14B440>,)
```

从作用域的角度，`foo()`实际上是调用了内嵌函数`inner()`，当执行到`inner()`中的`print(x)`语句时，在`inner()`中没有搜寻到`x`，然后会在`outer()`的命名空间中搜寻，找到`x`后进行打印。

但从生命周期的角度，`foo`的值为`outer()`函数的返回值，当执行`foo()`时，`outer()`函数已经执行完毕了，此时其作用域内定义的变量`x`也应该已经销毁，因此执行`foo()`时，当执行到`pirnt(x)`语句应该会出错。但实际执行过程中却没有。

这其实是Python支持的函数**闭包**的特性，在上面的例子中可以作这样的理解：在非全局作用域定义的`inner()`函数在定义时会记住外层命名空间，此时`inner()`函数包含了外层作用域变量`x`。`function`对象的`__closure__`属性指示了该函数对象是否是闭包函数，若不是闭包函数，则该属性值为`None`，否则为一个非空元组。









装饰器(Decorators)是Python的一个重要部分。简单地说：他们是修改其他函数的功能的函数。他们有助于让我们的代码更简短，也更Pythonic（Python范儿）。大多数初学者不知道在哪儿使用它们，所以我将要分享下，哪些区域里装饰器可以让你的代码更简洁。

首先，让我们讨论下如何写你自己的装饰器。

这可能是最难掌握的概念之一。我们会每次只讨论一个步骤，这样你能完全理解它。

### 一切皆对象

首先我们来理解下Python中的函数

```python
def hi(name="yasoob"):
    return "hi " + name

print(hi())
# output: 'hi yasoob'

# 我们甚至可以将一个函数赋值给一个变量，比如
greet = hi
# 我们这里没有在使用小括号，因为我们并不是在调用hi函数
# 而是在将它放在greet变量里头。我们尝试运行下这个

print(greet())
# output: 'hi yasoob'

# 如果我们删掉旧的hi函数，看看会发生什么！
del hi
print(hi())
#outputs: NameError

print(greet())
#outputs: 'hi yasoob'
```



### 在函数中定义函数

刚才那些就是函数的基本知识了。我们来让你的知识更进一步。在Python中我们可以在一个函数中定义另一个函数：

```python
def hi(name="yasoob"):
    print("now you are inside the hi() function")

    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    print(greet())
    print(welcome())
    print("now you are back in the hi() function")

hi()
#output:now you are inside the hi() function
#       now you are in the greet() function
#       now you are in the welcome() function
#       now you are back in the hi() function

# 上面展示了无论何时你调用hi(), greet()和welcome()将会同时被调用。
# 然后greet()和welcome()函数在hi()函数之外是不能访问的，比如：

greet()
#outputs: NameError: name 'greet' is not defined
```

那现在我们知道了可以在函数中定义另外的函数。也就是说：我们可以创建嵌套的函数。现在你需要再多学一点，就是函数也能返回函数。

### 从函数中返回函数

其实并不需要在一个函数里去执行另一个函数，我们也可以将其作为输出返回出来：

```python
def hi(name="yasoob"):
    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    if name == "yasoob":
        return greet
    else:
        return welcome

a = hi()
print(a)
#outputs: <function greet at 0x7f2143c01500>

#上面清晰地展示了`a`现在指向到hi()函数中的greet()函数
#现在试试这个

print(a())
#outputs: now you are in the greet() function
```

再次看看这个代码。在`if/else`语句中我们返回`greet`和`welcome`，而不是`greet()`和`welcome()`。为什么那样？这是因为当你把一对小括号放在后面，这个函数就会执行；然而如果你不放括号在它后面，那它可以被到处传递，并且可以赋值给别的变量而不去执行它。

你明白了吗？让我再稍微多解释点细节。

当我们写下`a = hi()`，`hi()`会被执行，而由于`name`参数默认是*yasoob*，所以函数`greet`被返回了。如果我们把语句改为`a = hi(name = "ali")`，那么`welcome`函数将被返回。我们还可以打印出`hi()()`，这会输出*now you are in the greet() function*。

### 将函数作为参数传给另一个函数

```python
def hi():
    return "hi yasoob!"

def doSomethingBeforeHi(func):
    print("I am doing some boring work before executing hi()")
    print(func())

doSomethingBeforeHi(hi)
#outputs:I am doing some boring work before executing hi()
#        hi yasoob!
```

现在你已经具备所有必需知识，来进一步学习装饰器真正是什么了。装饰器让你在一个函数的前后去执行代码。

### 你的第一个装饰器

在上一个例子里，其实我们已经创建了一个装饰器！现在我们修改下上一个装饰器，并编写一个稍微更有用点的程序：

```python
def a_new_decorator(a_func):

    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")

        a_func()

        print("I am doing some boring work after executing a_func()")

    return wrapTheFunction

def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove my foul smell")

a_function_requiring_decoration()
#outputs: "I am the function which needs some decoration to remove my foul smell"

a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
#now a_function_requiring_decoration is wrapped by wrapTheFunction()

a_function_requiring_decoration()
#outputs:I am doing some boring work before executing a_func()
#        I am the function which needs some decoration to remove my foul smell
#        I am doing some boring work after executing a_func()
```



## **函数装饰器@符号的应用**

Python 2.4通过在函数定义前添加一个装饰器名和`@`符号，来实现对函数的包装。在上面代码示例中，用了一个包装的函数来替换包含函数的变量来实现了装饰函数。

```python
 add = wrapper(add)
```

这种模式可以随时用来包装任意函数。但是如果定义了一个函数，可以用`@`符号来装饰函数，如下：

```python
 @wrapper
 def add(a, b):
     return Coordinate(a.x + b.x, a.y + b.y)
```

值得注意的是，这种方式和简单的使用`wrapper()`函数的返回值来替换原始变量的做法没有什么不同—— Python只是添加了一些语法糖来使之看起来更加明确。

使用装饰器很简单！虽说写类似`staticmethod`或者`classmethod`的实用装饰器比较难，但用起来仅仅需要在函数前添加`@装饰器名`即可。

```python
 @myDecorator
 def aFunction():
     # 。。。
```

等价于

```python
 def aFunction():
     # 。。。
     
 aFunction = myDecorator(aFunction)
```

因此被装饰后的函数`aFunction()`实际上已经是类`myDecorator`的对象。当再调用`aFunction()`函数时，实际上就是调用类`myDecorator`的对象，因此会调用到类`myDecorator`的`__call__()`方法。

因此使用类作为装饰器装饰函数来对函数添加一些额外的属性或功能时，一般会在类的`__init__()`方法中记录传入的函数，再在`__call__()`调用修饰的函数及其它额外处理。





你看明白了吗？我们刚刚应用了之前学习到的原理。这正是python中装饰器做的事情！它们封装一个函数，并且用这样或者那样的方式来修改它的行为。现在你也许疑惑，我们在代码里并没有使用@符号？那只是一个简短的方式来生成一个被装饰的函数。这里是我们如何使用@来运行之前的代码：

```python
@a_new_decorator
def a_function_requiring_decoration():
    """Hey you! Decorate me!"""
    print("I am the function which needs some decoration to "
          "remove my foul smell")

a_function_requiring_decoration()
#outputs: I am doing some boring work before executing a_func()
#         I am the function which needs some decoration to remove my foul smell
#         I am doing some boring work after executing a_func()

#the @a_new_decorator is just a short way of saying:
a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
```

希望你现在对Python装饰器的工作原理有一个基本的理解。如果我们运行如下代码会存在一个问题：

```python
print(a_function_requiring_decoration.__name__)
# Output: wrapTheFunction
```

这并不是我们想要的！Ouput输出应该是“a_function_requiring_decoration”。这里的函数被warpTheFunction替代了。它重写了我们函数的名字和注释文档(docstring)。幸运的是Python提供给我们一个简单的函数来解决这个问题，那就是functools.wraps。我们修改上一个例子来使用functools.wraps：

```python
from functools import wraps

def a_new_decorator(a_func):
    @wraps(a_func)
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")
        a_func()
        print("I am doing some boring work after executing a_func()")
    return wrapTheFunction

@a_new_decorator
def a_function_requiring_decoration():
    """Hey yo! Decorate me!"""
    print("I am the function which needs some decoration to "
          "remove my foul smell")

print(a_function_requiring_decoration.__name__)
# Output: a_function_requiring_decoration
```

现在好多了。我们接下来学习装饰器的一些常用场景。

蓝本规范:

```python
from functools import wraps
def decorator_name(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not can_run:
            return "Function will not run"
        return f(*args, **kwargs)
    return decorated

@decorator_name
def func():
    return("Function is running")

can_run = True
print(func())
# Output: Function is running

can_run = False
print(func())
# Output: Function will not run
```

注意：@wraps接受一个函数来进行装饰，并加入了复制函数名称、注释文档、参数列表等等的功能。这可以让我们在装饰器里面访问在装饰之前的函数的属性。



### 装饰器的应用

#### 授权(Authorization)

装饰器能有助于检查某个人是否被授权去使用一个web应用的端点(endpoint)。它们被大量使用于Flask和Django web框架中。这里是一个例子来使用基于装饰器的授权：

```python
from functools import wraps

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            authenticate()
        return f(*args, **kwargs)
    return decorated
```

#### 日志(Logging)

日志是装饰器运用的另一个亮点。这是个例子：

```python
from functools import wraps

def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging

@logit
def addition_func(x):
   """Do some math."""
   return x + x


result = addition_func(4)
# Output: addition_func was called
```

我敢肯定你已经在思考装饰器的一个其他聪明用法了

## 带参数的装饰器

来想想这个问题，难道`@wraps`不也是个装饰器吗？但是，它接收一个参数，就像任何普通的函数能做的那样。那么，为什么我们不也那样做呢？

这是因为，当你使用`@my_decorator`语法时，你是在应用一个以单个函数作为参数的一个包裹函数。记住，Python里每个东西都是一个对象，而且这包括函数！记住了这些，我们可以编写一下能返回一个包裹函数的函数。



# 在函数中嵌入装饰器

我们回到日志的例子，并创建一个包裹函数，能让我们指定一个用于输出的日志文件。

```python
from functools import wraps

def logit(logfile='out.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # 打开logfile，并写入内容
            with open(logfile, 'a') as opened_file:
                # 现在将日志打到指定的logfile
                opened_file.write(log_string + '\n')
            return func(*args, **kwargs)
        return wrapped_function
    return logging_decorator

@logit()
def myfunc1():
    pass

myfunc1()
# Output: myfunc1 was called
# 现在一个叫做 out.log 的文件出现了，里面的内容就是上面的字符串

@logit(logfile='func2.log')
def myfunc2():
    pass

myfunc2()
# Output: myfunc2 was called
# 现在一个叫做 func2.log 的文件出现了，里面的内容就是上面的字符串
```



# 装饰器类

现在我们有了能用于正式环境的`logit`装饰器，但当我们的应用的某些部分还比较脆弱时，异常也许是需要更紧急关注的事情。比方说有时你只想打日志到一个文件。而有时你想把引起你注意的问题发送到一个email，同时也保留日志，留个记录。这是一个使用继承的场景，但目前为止我们只看到过用来构建装饰器的函数。

幸运的是，类也可以用来构建装饰器。那我们现在以一个类而不是一个函数的方式，来重新构建`logit`。

```python
from functools import wraps

class logit(object):
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # 打开logfile并写入
            with open(self.logfile, 'a') as opened_file:
                # 现在将日志打到指定的文件
                opened_file.write(log_string + '\n')
            # 现在，发送一个通知
            self.notify()
            return func(*args, **kwargs)
        return wrapped_function

    def notify(self):
        # logit只打日志，不做别的
        pass
```

这个实现有一个附加优势，在于比嵌套函数的方式更加整洁，而且包裹一个函数还是使用跟以前一样的语法：

```python
@logit()
def myfunc1():
    pass
```

现在，我们给`logit`创建子类，来添加email的功能(虽然email这个话题不会在这里展开)。

```python
class email_logit(logit):
    '''
    一个logit的实现版本，可以在函数调用时发送email给管理员
    '''
    def __init__(self, email='admin@myproject.com', *args, **kwargs):
        self.email = email
        super(email_logit, self).__init__(*args, **kwargs)

    def notify(self):
        # 发送一封email到self.email
        # 这里就不做实现了
        pass
```

从现在起，`@email_logit`将会和`@logit`产生同样的效果，但是在打日志的基础上，还会多发送一封邮件给管理员。













# `**各种推导式(comprehensions)**`

推导式（又称解析式）是Python的一种独有特性，如果我被迫离开了它，我会非常想念。推导式是可以从一个数据序列构建另一个新的数据序列的结构体。 共有三种推导，在Python2和3中都有支持：

- 列表(`list`)推导式
- 字典(`dict`)推导式
- 集合(`set`)推导式

我们将一一进行讨论。一旦你知道了使用列表推导式的诀窍，你就能轻易使用任意一种推导式了。

### 列表推导式（`list` comprehensions）

列表推导式（又称列表解析式）提供了一种简明扼要的方法来创建列表。
它的结构是在一个中括号里包含一个表达式，然后是一个`for`语句，然后是0个或多个`for`或者`if`语句。那个表达式可以是任意的，意思是你可以在列表中放入任意类型的对象。返回结果将是一个新的列表，在这个以`if`和`for`语句为上下文的表达式运行完成之后产生。

### 规范

```python
variable = [out_exp for out_exp in input_list if out_exp == 2]
```

这里是另外一个简明例子:

```python
multiples = [i for i in range(30) if i % 3 is 0]
print(multiples)
# Output: [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
```

这将对快速生成列表非常有用。
有些人甚至更喜欢使用它而不是`filter`函数。
列表推导式在有些情况下超赞，特别是当你需要使用`for`循环来生成一个新列表。举个例子，你通常会这样做：

```python
squared = []
for x in range(10):
    squared.append(x**2)
```

你可以使用列表推导式来简化它，就像这样：

```python
squared = [x**2 for x in range(10)]
```

### 字典推导式（`dict` comprehensions）

字典推导和列表推导的使用方法是类似的。这里有个我最近发现的例子：

```python
mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}

mcase_frequency = {
    k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0)
    for k in mcase.keys()
}

# mcase_frequency == {'a': 17, 'z': 3, 'b': 34}
```

在上面的例子中我们把同一个字母但不同大小写的值合并起来了。

就我个人来说没有大量使用字典推导式。

你还可以快速对换一个字典的键和值：

```python
{v: k for k, v in some_dict.items()}
```



### 集合推导式（`set` comprehensions）

它们跟列表推导式也是类似的。 唯一的区别在于它们使用大括号`{}`。 举个例子：

```python
squared = {x**2 for x in [1, 1, 2]}
print(squared)
# Output: {1, 4}
```







# 对象变动(Mutation)

Python中可变(**mutable**)与不可变(**immutable**)的数据类型让新手很是头痛。简单的说，可变(mutable)意味着"可以被改动"，而不可变(immutable)的意思是“常量(constant)”。想把脑筋转动起来吗？考虑下这个例子：

```python
foo = ['hi']
print(foo)
# Output: ['hi']

bar = foo
bar += ['bye']
print(foo)
# Output: ['hi', 'bye']
```

刚刚发生了什么？我们预期的不是那样！我们期望看到是这样的：

```python
foo = ['hi']
print(foo)
# Output: ['hi']

bar = foo
bar += ['bye']

print(foo)
# Output: ['hi']

print(bar)
# Output: ['hi', 'bye']
```

这不是一个bug。这是对象可变性(**mutability**)在作怪。每当你将一个变量赋值为另一个可变类型的变量时，对这个数据的任意改动会同时反映到这两个变量上去。新变量只不过是老变量的一个别名而已。这个情况只是针对可变数据类型。下面的函数和可变数据类型让你一下就明白了：

```python
def add_to(num, target=[]):
    target.append(num)
    return target

add_to(1)
# Output: [1]

add_to(2)
# Output: [1, 2]

add_to(3)
# Output: [1, 2, 3]
```

你可能预期它表现的不是这样子。你可能希望，当你调用`add_to`时，有一个新的列表被创建，就像这样：

```python
def add_to(num, target=[]):
    target.append(num)
    return target

add_to(1)
# Output: [1]

add_to(2)
# Output: [2]

add_to(3)
# Output: [3]
```

啊哈！这次又没有达到预期，是列表的可变性在作怪。在Python中当函数被定义时，默认参数只会运算一次，而不是每次被调用时都会重新运算。你应该永远不要定义可变类型的默认参数，除非你知道你正在做什么。你应该像这样做：

```python
def add_to(element, target=None):
    if target is None:
        target = []
    target.append(element)
    return target
```

现在每当你在调用这个函数不传入`target`参数的时候，一个新的列表会被创建。举个例子：

```python
add_to(42)
# Output: [42]

add_to(42)
# Output: [42]

add_to(42)
# Output: [42]
```



# 异常

异常处理是一种艺术，一旦你掌握，会授予你无穷的力量。我将要向你展示我们能处理异常的一些方式。

最基本的术语里我们知道了`try/except`从句。可能触发异常产生的代码会放到`try`语句块里，而处理异常的代码会在`except`语句块里实现。这是一个简单的例子：

```python
try:
    file = open('test.txt', 'rb')
except IOError as e:
    print('An IOError occurred. {}'.format(e.args[-1]))
```

上面的例子里，我们仅仅在处理一个`IOError`的异常。大部分初学者还不知道的是，我们可以处理多个异常。











# `__slots__`魔法

在Python中，每个类都有实例属性。默认情况下Python用一个字典来保存一个对象的实例属性。这非常有用，因为它允许我们在运行时去设置任意的新属性。

然而，对于有着已知属性的小类来说，它可能是个瓶颈。这个字典浪费了很多内存。Python不能在对象创建时直接分配一个固定量的内存来保存所有的属性。因此如果你创建许多对象（我指的是成千上万个），它会消耗掉很多内存。
不过还是有一个方法来规避这个问题。这个方法需要使用`__slots__`来告诉Python不要使用字典，而且只给一个固定集合的属性分配空间。

这里是一个使用与不使用`__slots__`的例子：

- 不使用 `__slots__`:

  ```python
  class MyClass(object):
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
        self.set_up()
    # ...
  ```

- 使用 `__slots__`:

  ```python
  class MyClass(object):
    __slots__ = ['name', 'identifier']
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
        self.set_up()
    # ...
  ```

第二段代码会为你的内存减轻负担。通过这个技巧，有些人已经看到内存占用率几乎40%~50%的减少。





# 枚举

枚举(`enumerate`)是Python内置函数。它的用处很难在简单的一行中说明，但是大多数的新人，甚至一些高级程序员都没有意识到它。

它允许我们遍历数据并自动计数，

下面是一个例子：

```python
for counter, value in enumerate(some_list):
    print(counter, value)
```

不只如此，`enumerate`也接受一些可选参数，这使它更有用。

```python
my_list = ['apple', 'banana', 'grapes', 'pear']
for c, value in enumerate(my_list, 1):
    print(c, value)

# 输出:
(1, 'apple')
(2, 'banana')
(3, 'grapes')
(4, 'pear')
```

上面这个可选参数允许我们定制从哪个数字开始枚举。
你还可以用来创建包含索引的元组列表， 例如：

```python
my_list = ['apple', 'banana', 'grapes', 'pear']
counter_list = list(enumerate(my_list, 1))
print(counter_list)
# 输出: [(1, 'apple'), (2, 'banana'), (3, 'grapes'), (4, 'pear')]
```



# 对象自省

自省(introspection)，在计算机编程领域里，是指在运行时来判断一个对象的类型的能力。它是Python的强项之一。Python中所有一切都是一个对象，而且我们可以仔细勘察那些对象。Python还包含了许多内置函数和模块来帮助我们。



# `dir`

在这个小节里我们会学习到`dir`以及它在自省方面如何给我们提供便利。

它是用于自省的最重要的函数之一。它返回一个列表，列出了一个对象所拥有的属性和方法。这里是一个例子：

```python
my_list = [1, 2, 3]
dir(my_list)
# Output: ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__',
# '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
# '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__',
# '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__',
# '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__',
# '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__',
# '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop',
# 'remove', 'reverse', 'sort']
```

上面的自省给了我们一个列表对象的所有方法的名字。当你没法回忆起一个方法的名字，这会非常有帮助。如果我们运行`dir()`而不传入参数，那么它会返回当前作用域的所有名字。

# `type`和`id`

`type`函数返回一个对象的类型。举个例子：

```python
print(type(''))
# Output: <type 'str'>

print(type([]))
# Output: <type 'list'>

print(type({}))
# Output: <type 'dict'>

print(type(dict))
# Output: <type 'type'>

print(type(3))
# Output: <type 'int'>
```

`id()`函数返回任意不同种类对象的唯一ID，举个例子：

```python
name = "Yasoob"
print(id(name))
# Output: 139972439030304
```

# `inspect`模块

`inspect`模块也提供了许多有用的函数，来获取活跃对象的信息。比方说，你可以查看一个对象的成员，只需运行：

```python
import inspect
print(inspect.getmembers(str))
# Output: [('__add__', <slot wrapper '__add__' of ... ...
```

还有好多个其他方法也能有助于自省。如果你愿意，你可以去探索它们。



# `else`从句

`for`循环还有一个`else`从句，我们大多数人并不熟悉。这个`else`从句会在循环正常结束时执行。这意味着，循环没有遇到任何`break`. 一旦你掌握了何时何地使用它，它真的会非常有用。我自己对它真是相见恨晚。

有个常见的构造是跑一个循环，并查找一个元素。如果这个元素被找到了，我们使用`break`来中断这个循环。有两个场景会让循环停下来。

- 第一个是当一个元素被找到，`break`被触发。
- 第二个场景是循环结束。

现在我们也许想知道其中哪一个，才是导致循环完成的原因。一个方法是先设置一个标记，然后在循环结束时打上标记。另一个是使用`else`从句。

这就是`for/else`循环的基本结构：

```python
for item in container:
    if search_something(item):
        # Found it!
        process(item)
        break
else:
    # Didn't find anything..
    not_found_in_container()
```

考虑下这个简单的案例，它是我从官方文档里拿来的：

```python
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n / x)
            break
```

它会找出2到10之间的数字的因子。现在是趣味环节了。我们可以加上一个附加的else语句块，来抓住质数，并且告诉我们：

```python
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n / x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
```







# 使用C扩展

CPython还为开发者实现了一个有趣的特性，使用Python可以轻松调用C代码

开发者有三种方法可以在自己的Python代码中来调用C编写的函数-`ctypes`，`SWIG`，`Python/C API`。每种方式也都有各自的利弊。

首先，我们要明确为什么要在Python中调用C？

常见原因如下：

- 你要提升代码的运行速度，而且你知道C要比Python快50倍以上
- C语言中有很多传统类库，而且有些正是你想要的，但你又不想用Python去重写它们
- 想对从内存到文件接口这样的底层资源进行访问
- 不需要理由，就是想这样做

# Python/C API

[Python/C API](https://docs.python.org/2/c-api/)可能是被最广泛使用的方法。它不仅简单，而且可以在C代码中操作你的Python对象。

这种方法需要以特定的方式来编写C代码以供Python去调用它。所有的Python对象都被表示为一种叫做PyObject的结构体，并且`Python.h`头文件中提供了各种操作它的函数。例如，如果PyObject表示为PyListType(列表类型)时，那么我们便可以使用`PyList_Size()`函数来获取该结构的长度，类似Python中的`len(list)`函数。大部分对Python原生对象的基础函数和操作在`Python.h`头文件中都能找到。

示例

编写一个C扩展，添加所有元素到一个Python列表(所有元素都是数字)

来看一下我们要实现的效果，这里演示了用Python调用C扩展的代码

```Python
#Though it looks like an ordinary python import, the addList module is implemented in C
import addList

l = [1,2,3,4,5]
print "Sum of List - " + str(l) + " = " +  str(addList.add(l))
```

上面的代码和普通的Python文件并没有什么分别，导入并使用了另一个叫做`addList`的Python模块。唯一差别就是这个模块并不是用Python编写的，而是C。

接下来我们看看如何用C编写`addList`模块，这可能看起来有点让人难以接受，但是一旦你了解了这之中的各种组成，你就可以一往无前了。

```C
//Python.h has all the required function definitions to manipulate the Python objects
#include <Python.h>

//This is the function that is called from your python code
static PyObject* addList_add(PyObject* self, PyObject* args){

    PyObject * listObj;

    //The input arguments come as a tuple, we parse the args to get the various variables
    //In this case it's only one list variable, which will now be referenced by listObj
    if (! PyArg_ParseTuple( args, "O", &listObj ))
        return NULL;

    //length of the list
    long length = PyList_Size(listObj);

    //iterate over all the elements
    int i, sum =0;
    for (i = 0; i < length; i++) {
        //get an element out of the list - the element is also a python objects
        PyObject* temp = PyList_GetItem(listObj, i);
        //we know that object represents an integer - so convert it into C long
        long elem = PyInt_AsLong(temp);
        sum += elem;
    }

    //value returned back to python code - another python object
    //build value here converts the C long to a python integer
    return Py_BuildValue("i", sum);

}

//This is the docstring that corresponds to our 'add' function.
static char addList_docs[] =
"add(  ): add all elements of the list\n";

/* This table contains the relavent info mapping -
   <function-name in python module>, <actual-function>,
   <type-of-args the function expects>, <docstring associated with the function>
 */
static PyMethodDef addList_funcs[] = {
    {"add", (PyCFunction)addList_add, METH_VARARGS, addList_docs},
    {NULL, NULL, 0, NULL}

};

/*
   addList is the module name, and this is the initialization block of the module.
   <desired module name>, <the-info-table>, <module's-docstring>
 */
PyMODINIT_FUNC initaddList(void){
    Py_InitModule3("addList", addList_funcs,
            "Add all ze lists");

}
```

逐步解释

- `Python.h`头文件中包含了所有需要的类型(Python对象类型的表示)和函数定义(对Python对象的操作)
- 接下来我们编写将要在Python调用的函数, 函数传统的命名方式由{模块名}_{函数名}组成，所以我们将其命名为`addList_add`
- 然后填写想在模块内实现函数的相关信息表，每行一个函数，以空行作为结束
- 最后的模块初始化块签名为`PyMODINIT_FUNC init{模块名}`。

函数`addList_add`接受的参数类型为PyObject类型结构(同时也表示为元组类型，因为Python中万物皆为对象，所以我们先用PyObject来定义)。传入的参数则通过`PyArg_ParseTuple()`来解析。第一个参数是被解析的参数变量。第二个参数是一个字符串，告诉我们如何去解析元组中每一个元素。字符串的第n个字母正是代表着元组中第n个参数的类型。例如，"i"代表整形，"s"代表字符串类型, "O"则代表一个Python对象。接下来的参数都是你想要通过`PyArg_ParseTuple()`函数解析并保存的元素。这样参数的数量和模块中函数期待得到的参数数量就可以保持一致，并保证了位置的完整性。例如，我们想传入一个字符串，一个整数和一个Python列表，可以这样去写

```C
int n;
char *s;
PyObject* list;
PyArg_ParseTuple(args, "siO", &n, &s, &list);
```

在这种情况下，我们只需要提取一个列表对象，并将它存储在`listObj`变量中。然后用列表对象中的`PyList_Size()`函数来获取它的长度。就像Python中调用`len(list)`。

现在我们通过循环列表，使用`PyList_GetItem(list, index)`函数来获取每个元素。这将返回一个`PyObject*`对象。既然Python对象也能表示`PyIntType`，我们只要使用`PyInt_AsLong(PyObj *)`函数便可获得我们所需要的值。我们对每个元素都这样处理，最后再得到它们的总和。

总和将被转化为一个Python对象并通过`Py_BuildValue()`返回给Python代码，这里的i表示我们要返回一个Python整形对象。

现在我们已经编写完C模块了。将下列代码保存为`setup.py`

```Python
#build the modules

from distutils.core import setup, Extension

setup(name='addList', version='1.0',  \
      ext_modules=[Extension('addList', ['adder.c'])])
```

并且运行

```Shell
python setup.py install
```

现在应该已经将我们的C文件编译安装到我们的Python模块中了。

在一番辛苦后，让我们来验证下我们的模块是否有效

```Python
#module that talks to the C code
import addList

l = [1,2,3,4,5]
print "Sum of List - " + str(l) + " = " +  str(addList.add(l))
```

输出结果如下

```
Sum of List - [1, 2, 3, 4, 5] = 15
```

如你所见，我们已经使用Python.h API成功开发出了我们第一个Python C扩展。这种方法看似复杂，但你一旦习惯，它将变的非常有效。

Python调用C代码的另一种方式便是使用[Cython](http://cython.org/)让Python编译的更快。但是Cython和传统的Python比起来可以将它理解为另一种语言，所以我们就不在这里过多描述了。





# `open`函数

[open](http://docs.python.org/dev/library/functions.html#open) 函数可以打开一个文件。超级简单吧？大多数时候，我们看到它这样被使用：

```python
f = open('photo.jpg', 'r+')
jpgdata = f.read()
f.close()
```

我现在写这篇文章的原因，是大部分时间我看到`open`被这样使用。有**三个**错误存在于上面的代码中。你能把它们全指出来吗？如不能，请读下去。在这篇文章的结尾，你会知道上面的代码错在哪里，而且，更重要的是，你能在自己的代码里避免这些错误。现在我们从基础开始：

`open`的返回值是一个文件句柄，从操作系统托付给你的Python程序。一旦你处理完文件，你会想要归还这个文件句柄，只有这样你的程序不会超出一次能打开的文件句柄的数量上限。

显式地调用`close`关闭了这个文件句柄，但前提是只有在read成功的情况下。如果有任意异常正好在`f = open(...)`之后产生，`f.close()`将不会被调用（取决于Python解释器的做法，文件句柄可能还是会被归还，但那是另外的话题了）。为了确保不管异常是否触发，文件都能关闭，我们将其包裹成一个`with`语句:

```python
with open('photo.jpg', 'r+') as f:
    jpgdata = f.read()
```

`open`的第一个参数是文件名。第二个(`mode` 打开模式)决定了这个文件如何被打开。

- 如果你想读取文件，传入`r`
- 如果你想读取并写入文件，传入`r+`
- 如果你想覆盖写入文件，传入`w`
- 如果你想在文件末尾附加内容，传入`a`

虽然有若干个其他的有效的`mode`字符串，但有可能你将永远不会使用它们。`mode`很重要，不仅因为它改变了行为，而且它可能导致权限错误。举个例子，我们要是在一个写保护的目录里打开一个jpg文件， `open(.., 'r+')`就失败了。`mode`可能包含一个扩展字符；让我们还可以以二进制方式打开文件(你将得到字节串)或者文本模式(字符串)

一般来说，如果文件格式是由人写的，那么它更可能是文本模式。jpg图像文件一般不是人写的（而且其实不是人直接可读的），因此你应该以二进制模式来打开它们，方法是在`mode`字符串后加一个`b`(你可以看看开头的例子里，正确的方式应该是`rb`)。
如果你以文本模式打开一些东西（比如，加一个`t`,或者就用`r/r+/w/a`），你还必须知道要使用哪种编码。对于计算机来说，所有的文件都是字节，而不是字符。

可惜，在Pyhon 2.x版本里，`open`不支持显示地指定编码。然而，[io.open](http://docs.python.org/2/library/io.html#io.open)函数在Python 2.x中和3.x(其中它是`open`的别名)中都有提供，它能做正确的事。你可以传入`encoding`这个关键字参数来传入编码。
如果你不传入任意编码，一个系统 - 以及Python -指定的默认选项将被选中。你也许被诱惑去依赖这个默认选项，但这个默认选项经常是错误的，或者默认编码实际上不能表达文件里的所有字符（这将经常发生在Python 2.x和/或Windows）。
所以去挑选一个编码吧。`utf-8`是一个非常好的编码。当你写入一个文件，你可以选一个你喜欢的编码（或者最终读你文件的程序所喜欢的编码）。

那你怎么找出正在读的文件是用哪种编码写的呢？好吧，不幸的是，并没有一个十分简单的方式来检测编码。在不同的编码中，同样的字节可以表示不同，但同样有效的字符。因此，你必须依赖一个元数据（比如，在HTTP头信息里）来找出编码。越来越多的是，文件格式将编码定义成`UTF-8`。

有了这些基础知识，我们来写一个程序，读取一个文件，检测它是否是JPG（提示：这些文件头部以字节`FF D8`开始），把对输入文件的描述写入一个文本文件。

```python
import io

with open('photo.jpg', 'rb') as inf:
    jpgdata = inf.read()

if jpgdata.startswith(b'\xff\xd8'):
    text = u'This is a JPEG file (%d bytes long)\n'
else:
    text = u'This is a random file (%d bytes long)\n'

with io.open('summary.txt', 'w', encoding='utf-8') as outf:
    outf.write(text % len(jpgdata))
```

我敢肯定，现在你会正确地使用`open`啦！





# 22. 目标Python2+3

很多时候你可能希望你开发的程序能够同时兼容Python2+和Python3+。

试想你有一个非常出名的Python模块被很多开发者使用着，但并不是所有人都只使用Python2或者Python3。这时候你有两个办法。第一个办法是开发两个模块，针对Python2一个，针对Python3一个。还有一个办法就是调整你现在的代码使其同时兼容Python2和Python3。

本节中，我将介绍一些技巧，让你的脚本同时兼容Python2和Python3。

**Future模块导入**

第一种也是最重要的方法，就是导入`__future__`模块。它可以帮你在Python2中导入Python3的功能。这有一组例子：

上下文管理器是Python2.6+引入的新特性，如果你想在Python2.5中使用它可以这样做：

```python
from __future__ import with_statement
```

在Python3中`print`已经变为一个函数。如果你想在Python2中使用它可以通过`__future__`导入：

```python
print
# Output:

from __future__ import print_function
print(print)
# Output: <built-in function print>
```

**模块重命名**

首先，告诉我你是如何在你的脚本中导入模块的。大多时候我们会这样做：

```python
import foo 
# or
from foo import bar
```

你知道么，其实你也可以这样做：

```python
import foo as foo
```

这样做可以起到和上面代码同样的功能，但最重要的是它能让你的脚本同时兼容Python2和Python3。现在我们来看下面的代码：

```python
try:
    import urllib.request as urllib_request  # for Python 3
except ImportError:
    import urllib2 as urllib_request  # for Python 2
```

让我来稍微解释一下上面的代码。
我们将模块导入代码包装在`try/except`语句中。我们是这样做是因为在Python 2中并没有`urllib.request`模块。这将引起一个`ImportError`异常。而在Python2中`urllib.request`的功能则是由`urllib2`提供的。所以,当我们试图在Python2中导入`urllib.request`模块的时候，一旦我们捕获到`ImportError`我们将通过导入`urllib2`模块来代替它。

最后，你要了解`as`关键字的作用。它将导入的模块映射到`urllib.request`，所以我们通过`urllib_request`这个别名就可以使用`urllib2`中的所有类和方法了。

**过期的Python2内置功能**

另一个需要了解的事情就是Python2中有12个内置功能在Python3中已经被移除了。要确保在Python2代码中不要出现这些功能来保证对Python3的兼容。这有一个强制让你放弃12内置功能的方法：

```python
from future.builtins.disabled import *
```

现在，只要你尝试在Python3中使用这些被遗弃的模块时，就会抛出一个`NameError`异常如下：

```python
from future.builtins.disabled import *

apply()
# Output: NameError: obsolete Python 2 builtin apply is disabled
```

**标准库向下兼容的外部支持**

有一些包在非官方的支持下为Python2提供了Python3的功能。例如，我们有：

- enum `pip install enum34`
- singledispatch `pip install singledispatch`
- pathlib `pip install pathlib`

想更多了解，在Python文档中有一个[全面的指南](https://docs.python.org/3/howto/pyporting.html)可以帮助你让你的代码同时兼容Python2和Python3。





# 23. 协程

Python中的协程和生成器很相似但又稍有不同。主要区别在于：

- 生成器是数据的生产者
- 协程则是数据的消费者

首先我们先来回顾下生成器的创建过程。我们可以这样去创建一个生成器:

```python
    def fib():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a+b
```

然后我们经常在`for`循环中这样使用它:

```python
    for i in fib():
        print i
```

这样做不仅快而且不会给内存带来压力，因为我们所需要的值都是动态生成的而不是将他们存储在一个列表中。更概括的说如果现在我们在上面的例子中使用`yield`便可获得了一个协程。协程会消费掉发送给它的值。Python实现的`grep`就是个很好的例子：

```python
    def grep(pattern):
        print("Searching for", pattern)
        while True:
            line = (yield)
            if pattern in line:
                print(line)
```

等等！`yield`返回了什么？啊哈，我们已经把它变成了一个协程。它将不再包含任何初始值，相反要从外部传值给它。我们可以通过`send()`方法向它传值。这有个例子：

```python
    search = grep('coroutine')
    next(search)
    #output: Searching for coroutine
    search.send("I love you")
    search.send("Don't you love me?")
    search.send("I love coroutine instead!")
    #output: I love coroutine instead!
```

发送的值会被`yield`接收。我们为什么要运行`next()`方法呢？这样做正是为了启动一个协程。就像协程中包含的生成器并不是立刻执行，而是通过`next()`方法来响应`send()`方法。因此，你必须通过`next()`方法来执行`yield`表达式。

我们可以通过调用`close()`方法来关闭一个协程。像这样：

```python
    search = grep('coroutine')
    search.close()
```

更多协程相关知识的学习大家可以参考David Beazley的这份[精彩演讲](http://www.dabeaz.com/coroutines/Coroutines.pdf)。
