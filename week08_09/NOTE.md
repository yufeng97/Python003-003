学习笔记

## 变量作用域  

Python 作用域遵循 LEGB 规则，从左到右依次查找。
LEGB 含义解释：

- **Local**(function)；函数内的名字空间
- **Enclosing** function locals；外部嵌套函数的名字空间（例如closure）
- **Global**(module)；函数定义所在模块（文件）的名字空间
- **Builtin**(Python)；Python 内置模块的名字空间  

## 装饰器

- 增强而不改变原有函数
- 装饰器强调函数的定义态而不是运行态  

```python
# 实现一个叫做 log 的装饰器
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
```

### 装饰器的使用

```python
@log
def func():
	print("hello")
	
# 上面代码等价于
def func():
	print("hello")
func = log(func)	# 重新定义 function
```

### 装饰器对函数的影响

当一个函数在定义的时候被装饰过, 它就不是原来的函数了

```python
# 被装饰前
def function():
    """我是干净的, 没有被装饰过"""
    pass

function.__name__  # 查看 function 的名字, 输出: 'function'
function.__doc__  # 查看 function 的注释文档, 输出: '我是干净的, 没有被装饰过'

# 被装饰后
@decorator
def function():
    """我不干净了, 被装饰过了"""
    pass

function.__name__  # 输出: 'wrapper'
function.__doc__  # 输出为空
```

为了解决这个问题, python 提供了一个简单的函数 functools.wraps

```python
from functools import wraps

def decorator(func):
    @wraps(func)  # 在装饰器函数里加上这样一行代码, 使 func 结构不变
    def wrapper():
        func()
    return wrapper

@decorator
def function():
    """虽然不干净了, 被装饰过了, 但, 我还是原来的我"""
    pass

function.__name__  # 输出: 'function'
function.__doc__  # 输出: '虽然不干净了, 被装饰过了, 但, 我还是原来的我'
```

### 装饰器高级用法

#### 装饰器带参数

想给装饰器添加参数, 只要在原来的装饰器外嵌一层函数即可

```python
def decorator_with_arg(fargs):  # 带参数的装饰器
    def decorator(func):  # 原来的装饰器
        def wrapper():
            func()
            print(fargs)
        return wrapper
    return decorator
```

#### 装饰器堆叠

有时候想给函数带上多个装饰器, 要注意装饰器堆叠的顺序

```python
@decorator1  # decorator1 装饰 装饰了 function 的 decorater2
@decorator2  # decorator2 装饰 function
def function():
    pass
```

#### 装饰类

```python
  
# 装饰类
def decorator(aClass):
    class newClass(object):
        def __init__(self, args):
            self.times = 0
            self.wrapped = aClass(args)
            
        def display(self):
            # 将runtimes()替换为display()
            self.times += 1
            print("run times", self.times)
            self.wrapped.display()
    return newClass

@decorator
class MyClass(object):
    def __init__(self, number):
        self.number = number
    # 重写display
    def display(self):
        print("number is",self.number)

six = MyClass(6)
for i in range(5):
    six.display()
```

## 装饰器常用应用

### lru_cache()

LRU 缓存机制, 适合用于装饰一些递归函数, 从而大幅提升程序性能, 如 Fibonacci 数列

```python
from functools import lru_cache

@lru_cache()  # 注意要带括号
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

if __name__=='__main__':
    import timeit
    print(timeit.timeit("fibonacci(6)", setup="from __main__ import fibonacci"))

# 可以对比使用 lru_cache() 前后要花多久
```

### 授权

装饰器能有助于检查某个人是否被授权去使用一个 web 应用的端点(endpoint), 它们被大量使用于 Flask 和 Django web框架中

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

### 日志功能

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
```

### 添加属性

```python
def attrs(**kwds):
    def decorate(f):
        for k in kwds:
            setattr(f, k, kwds[k])
        return f
    return decorate

@attrs(versionadded="2.2", author="Guido van Rossum")
def mymethod(f):
    pass
```

### 函数参数观察(方便调试)

```python
import functools

def trace(f):
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        print(f, args, kwargs)
        result = f(*args, **kwargs)
        print(result)
    return decorated_function

@trace
def greet(greeting, name):
    return '{}, {}!'.format(greeting, name)

greet('better','me')
```

参考/Reference：@**[LRal](https://github.com/LRal)** https://github.com/LRal/Python003-003/blob/master/week08/NOTE.md

## 迭代器和生成器

### 迭代器与可迭代的区别

#### Iterable 可迭代对象

包含 `__getitem__()` 或 `__iter__()` 方法的容器对象。

大部分对象都是可迭代，只要实现了`__iter__()`方法的对象就是可迭代的。`__iter__()`方法会返回迭代器（iterator）本身。

#### Iterator 迭代器

包含 `next()` 和 `__iter__()` 方法。

具有`next()`方法的对象都是迭代器。在调用`next()`方法时，迭代器会返回它的下一个值。如果`next()`方法被调用，但迭代器没有值可以返回，就会引发一个`StopIteration`异常。

#### Generator 生成器 

包含 `yield` 语句的函数  

- 任何包含yield语句的函数都称为生成器。
- 生成器都是一个迭代器，但迭代器不一定是生成器

当调用生成器函数时，每次执行到`yield`语句，生成器的状态将被冻结起来，并将结果返回`__next__()`调用者。冻结意思是局部的状态都会被保存起来，包括局部变量绑定、指令指针。确保下一次调用时能从上一次的状态继续。

参考/Reference：https://www.cnblogs.com/weiman3389/p/6044963.html



yield from 是表达式，对 yield 进行了扩展。

yield from后面加上可迭代对象，他可以把可迭代对象里的每个元素一个一个的yield出来，对比yield来说代码更加简洁，结构更加清晰。

```python
# 字符串
astr='ABC'
# 列表
alist=[1,2,3]
# 字典
adict={"name":"wangbm","age":18}
# 生成器
agen=(i for i in range(4,8))

def gen(*args, **kw):
    for item in args:
        for i in item:
            yield i
# gen function 可以简化为gen2 使用yield from
def gen2(*args, **kw):
    for item in args:
        yield from item

new_list=gen(astr, alist, adict， agen)
print(list(new_list))
# ['A', 'B', 'C', 1, 2, 3, 'name', 'age', 4, 5, 6, 7]
```

## 异步编程

### await

python3.5 版本引入了 await 取代 yield from 方式

```python
import asyncio
async def py35_coro():
	await stuff()
```

注意： await 接收的对象必须是 awaitable 对象
awaitable 对象定义了 `__await__()` 方法
awaitable 对象有三类：

1. 协程 coroutine
2. 任务 Task
3. 未来对象 Future  

### aiohttp

aiohttp 异步的 HTTP 客户端和服务端  

```python
from aiohttp import web

# views
async def index(request):
	return web.Response(text='hello aiohttp')

# routes
def setup_routes(app):
	app.router.add_get('/', index)
    
# app
app = web.Application()
setup_routes(app)
web.run_app(app, host='127.0.0.1', port=8080)
```

Example

```python
import aiohttp
import asyncio

urls = [
    'http://httpbin.org',
    'http://httpbin.org/get',
    'http://httpbin.org/ip',
    'http://httpbin.org/headers'
]

async def  crawler():
    async with aiohttp.ClientSession() as session:
        futures = map(asyncio.ensure_future, map(session.get, urls))
        for task in asyncio.as_completed(futures):
            print(await task)

if __name__ == "__main__":
    ioloop = asyncio.get_event_loop()
    ioloop.run_until_complete(asyncio.ensure_future(crawler()))
```

