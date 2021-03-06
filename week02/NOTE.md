学习笔记

### Fake Useragent

#### 安装

```bash
pip install fake-useragent
```

#### 例子

```python
from fake_useragent import UserAgent
# 不验证ssl使请求返回的更加快速
ua = UserAgent(verify=False)

# 模拟不同浏览器
print(f'Chrome: {ua.chrome}')
# 随机返回头部信息，推荐使用
print(f'随机浏览器：{ua.random}')
```

有的网站可能会验证Referer，当前页面是从什么页面跳转而来

比较基本的头部信息：User Agent，Cookies，Referer

#### httpbin

https://www.httpbin.org/是一个专门进行HTTP的学习和调试的网站，它会把请求的头信息在网页上展示出来

### MySQL

#### 安装

https://blog.csdn.net/SPRATAD/article/details/107270840

安装报错：由于找不到VCRUNTIME140_1.dll，无法继续执行代码。重新安装程序可能会解决此问题

https://www.cnblogs.com/zyt6688/p/12601002.html

#### 启动

```bash
# 启动服务
net start mysql
# 进入mysql交互
mysql -u root -p
# 停止服务
net stop mysql
```

#### 安装pymysql

```bash
pip install pymysql
```

#### 例子

```python
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='user',
                             password='passwd',
                             db='db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()
```

### WebDriver

Python第三方库，模拟浏览器操作

#### Windows的安装

下载相对应的chromedriver驱动

国内镜像：http://npm.taobao.org/mirrors/chromedriver/

下载完成后解压，获取*chromedriver.exe*文件，将这个文件复制到所用的python环境下的**Scripts**文件夹下。

##### 测试代码

```python
from selenium import webdriver

brower = webdriver.Chrome()
```

如果跳出Chrome显示如下，说明已经成功安装chromedriver

<img src="https://img2018.cnblogs.com/blog/1185301/201903/1185301-20190315104214208-456362436.png" style="zoom: 150%;" /> 

