学习笔记
## Python环境配置
### 替换pip源地址

##### 常用 pip 源地址

* 豆瓣： https://pypi.doubanio.com/simple/
* 清华： https://mirrors.tuna.tsinghua.edu.cn/help/pypi/
* 中科大： https://pypi.mirrors.ustc.edu.cn/simple/
* 阿里云： https://mirrors.aliyun.com/pypi/simple/ 

##### 临时替换

```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
```

##### 永久替换（先升级 pip：pip install pip -U ）

```bash
pip install pip -U
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

### 配置venv虚拟环境

#### Windows环境

```bash
# create environment
python -m venv project-venv
# activate
project-venv\Scripts\activate

# exit
deactivate
```

#### Unix/MacOS环境

```bash
python -m venv project-venv
source project-venv/bin/activate
```

## Beautiful Soup

### 简单例子

```python
# 使用BeautifulSoup解析网页

import requests
from bs4 import BeautifulSoup as bs
# bs4是第三方库需要使用pip命令安装


user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

header = {'user-agent':user_agent}

myurl = 'https://movie.douban.com/top250'

response = requests.get(myurl,headers=header)

bs_info = bs(response.text, 'html.parser')

# Python 中使用 for in 形式的循环,Python使用缩进来做语句块分隔
for tags in bs_info.find_all('div', attrs={'class': 'hd'}):
    for atag in tags.find_all('a'):
        print(atag.get('href'))
        # 获取所有链接
        print(atag.find('span').text)
        # 获取电影名字
```

## Scrapy

#### 框架架构

![img](https://docs.scrapy.org/en/latest/_images/scrapy_architecture_02.png)

#### 安装

```bash
pip install scrapy
```

#### 创建项目

```bash
scrapy startproject spiders
cd spiders
scrapy genspider movies douban.com
```

#### Item Pipeline

spider `parse`函数每yield一个item就会调用一次`process_item`函数，想要持续地将数据写入一个文件中，就需要用到`open_spider`，`close_spider`函数，在spider启动和关闭时，分别创建和关闭文件。

```python
import json

from itemadapter import ItemAdapter

class JsonWriterPipeline:

    def open_spider(self, spider):
        self.file = open('items.jl', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(ItemAdapter(item).asdict()) + "\n"
        self.file.write(line)
        return item
```

