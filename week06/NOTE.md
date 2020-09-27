学习笔记

## MTV 框架模式

- 模型（Model）
- 模板（Template）
- 视图（Views）  

![MTV框架](MTV框架.png)

## 安装 Django

在虚拟环境中

```bash
python -m pip install Django
```

指定安装版本

```bash
pip install --upgrade django==2.2.13  
```

查看版本

```
>>> import django
>>> django.__version__
'2.2.13'  
```

## 创建 Django 项目  

```bash
django-admin startproject mysite  
```

⽬录结构如下：  

```
mysite/
    manage.py				命令⾏⼯具
    mysite/
        __init__.py
        settings.py			项⽬的配置⽂件
        urls.py
        asgi.py
        wsgi.py
```

## 启动服务器

```bash
python manage.py runserver
```

**更换端口**

```
python manage.py runserver 8080
```