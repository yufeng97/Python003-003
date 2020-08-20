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

## Scrapy

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

