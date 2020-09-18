学习笔记

axis参数使用'index'或者'columns'可以提升代码的阅读性

> **axis{0/’index’, 1/’columns’}, default 0**
> The axis to concatenate along.

```
axis=1 -> axis='columns'
axis=0 -> axis='index'
```

使用布尔索引时需注意加括号

不加括号 ```df['A'] > 2 & df['B'] < 3``` 会被Python程序表达为 *```df['A'] > (2 & df['B']) < 3```*, 实际正确的写法为 ```(df['A'] > 2) & (df['B'] < 3)```.

作业参考：https://www.jianshu.com/p/c1e44c6f461b