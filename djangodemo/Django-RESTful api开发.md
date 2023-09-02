# RESTful API开发

# Django

## 一、安装Django

```python
pip3 install Django
```

会安装在Python的默认安装路径`C:\Users\14584\AppData\Local\Programs\Python\Python311\Scripts`，源码路径在 `C:\Users\14584\AppData\Local\Programs\Python\Python311\Lib\site-packages`

---

## 二、创建Django项目的方式

1. 使用命令行的方式

`django-admin startproject 自定义项目名称` 

> 若未添加安装路径`C:\Users\14584\AppData\Local\Programs\Python\Python311\Scripts`在环境变量，需要使用绝对路径执行

---

创建好项目之后，默认文件如下

```python
djangodemo为项目名称，会默认在项目创建一个manage.py文件和一个和项目名称相同的文件夹
djangodemo/djangodemo/__init__.py
djangodemo/djangodemo/asgi.py -- 接收网络请求（异步）
djangodemo/djangodemo/settings.py -- 项目配置文件、保存数据库连接信息等（常用）
djangodemo/djangodemo/urls.py -- 保存路由和函数的对应关系（常用）
djangodemo/djangodemo/wsgi.py -- 接收网络请求（同步）
djangodemo/manage.py -- 项目的管理、启动项目、创建APP、数据管理（基本不会动）

```

---

## 三、创建APP

DJango中的APP是指一个可以提供独立功能的应用

使用`python manage.py startapp 自定义APP的名称`来创建

```python
# python manage.py startapp app01 创建一个app名为app01
- app01
	- migrations # 【固定不动】数据库变更记录
	  - __init__.py
	- admin.py # 【固定不动】DJango默认提供的admin后台管理
	- apps.py # 【固定不动】App启动类
	- models.py # 常用，对数据库进行操作
	- tests.py # 单元测试
	- views.py # 常用，视图函数的编写，和项目中的urls.py密切相关
	- __init__.py
```

## 四、快速上手 运行demo程序 

1. 首先需要将新建的App应用添加到setting.py配置文件中

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app01.apps.App01Config' # 这是新添加的App
]
```

2. 修改url.py文件，将URL路由和函数关系配置

```python
from django.contrib import admin
from django.urls import path
#  从创建的App中导入视图模块
from app01 import views

urlpatterns = [
    # 绑定路由index/和视图中函数index
    path('index/', views.index)
]
```

3. 编写views.py，创建自己的函数`注意：request是必须要传递的参数`

```python
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello World')
```

4.运行项目

```python
python manage.py runserver ip 端口（默认是127.0.0.1:8000）
```

---



## 五、模板templates

### 1.模板基础使用

1. 在App目录下创建templates目录，将需要使用的HTML静态页面放在下面
2. 编写views中需要定义的函数

```python
from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request=request, template_name='index.html')
```

`注意；默认情况下，会按照App注册的顺序，逐一在App对应的目录下查找templates目录下的HTML页面，如果在settings.py配置文件中，对TEMPLATES参数做了配置，则优先去项目下的templates查找`

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #此处配置之后，会优先去项目下的templates目录中查找HTML页面
        'DIRS': [os.path.join(BASE_DIR, `templates`)], 
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

### 2.静态文件

静态文件包括：

- 图片
- CSS
- JavaScript
- 其他工具plugins

以上类型的文件都会被当做静态文件处理，具体使用方法如下

1. 在App目录下面创建一个static的文件夹，可以继续分层的创建具体的静态资源文件夹，如img、css等

![image-20230901141822680](F:\DjangoSite\djangodemo\assets\image-20230901141822680.png)

2. 在需要使用静态文件的HTML页面中使用

```python
# DJango模板语法，表示引入静态文件目录
{% load static %}
<head>
    <title>这是标题内容</title>
    <body>
        <h1>这是H1格式的标题</h1>
        # 替换传统的URL值为相对或者绝对位置，改为{% static '这里面是static目录下静态资源的位置' %}
        <img src="{% static 'img/image-20230901140621817.png' %}" alt="">
    </body>
</head>
```

### 3.DJango的模板语法

1. 变量、列表和字典在HTML传值的用法

```python
1.先在views中定义对应的函数和方法
2.在HTML中使用标准的格式引用
```

**重点**:使用for循环或者if等条件语句，需要使用`{% %}`将条件语句`for...in..., if...elif...else...等`包裹起来，使用变量需要使用`{{  }}`将变量包裹起来，使用获取字典的value，需要使用`.`的方式去获取value，不能使用`dict['key']`的方式。

​	views函数的编写：

```python
def tmp(request):
    name = 'xiaoming'
    l = ['上午', '中午', '下午']
    dic = {'姓名':'小明', '年龄':17, '性别':'男'}
    # 传递需要的参数，以字典的方式
    return render(request, 'tmp.html', {'n1': name, 'n2': l, 'n3':dic})
```

​	模板HTML的编写：

```python
<body>
    <!-- 直接读取变量或者获取列表中的值用法 -->
    <div>{{ n1 }}</div>
    <div>{{n2}}</div>
    <div>{{n2.0}}</div>
    <div>{{n2.1}}</div>
    <div>{{n2.2}}</div>
    {% for item in n2 %}
    <span>{{ item }}</span>
    {% endfor %}
    <hr>
    <!-- 获取字典值中的用法 -->
    <div>
        {% for k, v in n3.items %}
        <li>字典的key为: {{k}}, value为: {{v}}</li>
        {% endfor %}
    </div>
    <hr>
    <!-- 在模板中也可以使用判断语句 -->
    <div>
        {% if n1 == 'xiaoming' %}
        <h2>aaaa</h2>
        {% elif n1 == 'xiaoli' %}
        <h2>bbbb</h2>
        {% else %}
        <h2>ccc</h2>
        {% endif %}
    </div>
        <hr>
    <div>
        <h3>新闻内容</h3>
        {%for item in data_list%}
        <!-- 注意，获取字典信息，需要使用.模式来获取，不能使用dict['key']的方式获取 -->
        <li>新闻标题：{{item.news_title}}, 新闻发布时间{{item.post_time}}</li>
        {%endfor%}
    </div>
</body>
```

DJango中templates处理含模板语法的HTM流程

![image-20230902234023252](F:\DjangoSite\djangodemo\assets\image-20230902234023252.png)

## 六、 请求与响应

注意：

1. DJango中的请求和views函数中的`request`对象息息相关，其属性和方法可以获取所有浏览器请求传递的request信息。
2. 响应中的redirect函数，是将重定向的地址返还给浏览器，由浏览器自己发起请求，请求数据不会由DJango中转。

```python
解释DJango中常见请求与响应工作的伪代码

def req_resp(request):
    #  请求
    # 1、接收如request.method（返回request请求的方法）
    print(request.method)
    # 2、接收GET请求，附带的参数信息，同理，接收POST方法的参数信息为request.POST,此时返回的是一个字典
    arg = request.GET
    print(arg)
    return HttpResponse(arg)
    #  响应
    # 3、返回 HttpResponse 对象中的content字符串信息
    return HttpResponse('Hello World')
    # 4、返回render对象，首先读取HTML网页内容->将模板字符串替换，渲染页面->完成渲染之后，以字符串的方式返回给用户浏览器
    #  其中可以传递参数，常见数据类型都可以传递
    return render(request, 'tmp.html', {'n1': name, 'n2': l, 'n3': dic, 'data_list': data_dict})
    # 5、返回redirect对象，让浏览器重定向到其他网页
    return redirect('https://www.baidu.com')
```

