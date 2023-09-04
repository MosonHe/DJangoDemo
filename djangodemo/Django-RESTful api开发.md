# RESTful API开发

# Django基础知识

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
djangodemo/djangodemo/settings.py -- 项目配置文件、绑定App、保存数据库连接信息等（常用）
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

简单的案例：通过接收处理请求，做到不同的响应，做一个简易的用户登录界面。

1. 在urls.py中添加路由绑定关系

``` python
from django.contrib import admin
from django.urls import path
#  从创建的App中导入视图模块
from app01 import views

urlpatterns = [
    path('login/', views.login)
]
```

2. 在templates目录下面，新增一个登录的HTML页面

```python
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8" />
    <title>login</title>
</head>
<body>
    <!-- 表单提交方法为post，提交的路由是login -->
    <form method="post" action="/login/">
        <!-- 如果使用DJango中的模板，在表单请求的时候，必须设置一个{% csrf_token %}语法，否则会报错403，此方法的作用是为了校验请求方的真实性 -->
        {% csrf_token %}
        <input type="text" name="user" placeholder="用户名">
        <input type="password" name="pwd" placeholder="密码">
        <input type="submit" value="提交">
        <span>{{ error_msg }}</span>
    </form>
</body>
</html>
```



3. 在views函数中，编写登录的方法

```python
def login(request):
    # 如果请求方法是GET，那么则返回一个render对象，将login登录页面返回。
    if request.method == 'GET':
        return render(request, 'login.html')
    # 如果请求方法是POST，则取到表单提交的信息，做判断
    username = request.POST.get('user')
    password = request.POST.get('pwd')
    if username == 'admin' and password == '123':
        return redirect('https://www.baidu.com')
    # 当账号密码错误的时候，返回一个render，将提示以变量的方式传递到HTML页面进行渲染
    return render(request, 'login.html', {'error_msg':'账号或者密码错误'})
```

## 七、 DJango中的数据库操作（ORM框架）

> ORM（Object Relation Mapping），对象关系映射，面向对象操作数据库

### 1.创建数据库

DJango无法帮助我们创建数据库，所以需要手动去创建。

### 2.连接数据库

在settings.py文件中，配置需要连接的远端数据库信息，默认是本地数据库sqlite3

```python
DATABASES = {
    'default': {
        # 数据库链接引擎，使用不同的数据库链接类型不一样，下面是连接不同数据库所需要的参数
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': '数据库的名称',
        'USER': '连接数据库的用户名',
        'PASSWORD': '连接数据库的密码',
        'HOST': '数据库的ip地址',
        'PORT': 3306
    }
}
```

### 3.在对应的App中，修改models.py，创建模型类

```python
from django.db import models

# Create your models here.
# 创建模型类，继承models.Model
class UserInfo(models.Model):
    # 类属性，对应着数据库中每一个字段的具体数据类型
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField()
```

### 4.在控制台中执行DJango命令，开始创建表结构

```python
python manage.py makemigrations
python manage.py migrate
```

注意，关于创建表和修改表结构有如下事项：

1. App需要提前注册，这里面除开自己创建的表之外，会创建多张表的原因是DJango自己默认注册了很多App，都会去创建数据表；
2. DJango后续自动创建数据表的时候，会自动添加一个主键为`id` BIGINT(19) NOT NULL AUTO_INCREMENT, PRIMARY KEY (`id`) USING BTREE；
3. 表的命名规则是App名称小写_模型类名小写。

![image-20230903174521834](F:\DjangoSite\DJangoDemo\djangodemo\Django-RESTful api开发.assets\image-20230903174521834.png)

4. 【**重点**】在后续的开发中，如果要对数据库表结构进行调整，只需要在models.py文件中操作类（新增，注释），再执行命令即可

   ```python
   python manage.py makemigrations
   python manage.py migrate
   ```

   - 如果需要删除字段，只需要将字段注释掉即可

   - 如果需要新增字段，由于已存在列中可能已有数据，所以新增列必须要制定新增列对应的数据，有如下几种方式。

     - 手动输入一个值；
     - 在类中定义类属性的时候，设置一个默认值

     ```python
         age = models.IntegerField(defaullt=1)
     ```

     - 在类中定义类属性的时候，允许字段为空

     ```python
         age = models.IntegerField(null=True, blank=True)

### 5.ORM框架中基本的增删改查操作

方法定义在views.py中

``` python
def orm(request):
    from app01.models import UserInfo, Department
    # 使用DJango的ORM框架对数据做基本的增删改查操作。
    # 1、新建 使用模型类名.objects.create(**kwargs)来新增记录
    Department.objects.create(title = '销售部')
    Department.objects.create(title = 'IT部')
    Department.objects.create(title = '运营部')

    UserInfo.objects.create(name = 'hexs', password = '123', age = '18')
    UserInfo.objects.create(name = 'zhangsan', password = '123', age = '28')
    UserInfo.objects.create(name = 'lisi', password = '123', age = '38')

    # 2、删除 .filter()方法可以做条件过滤，然后再使用delete()方法删除。
    UserInfo.objects.filter(id = 3).delete()

    # all()方法表示选择全部
    Department.objects.all().delete()

    # 3、获取数据 模型类名.objects.all()或者模型类名.objects.filter()  
    # 返回的是一个QuerySet对象列表，可以通过.属性的方式去获取表字段属性
    data_list = UserInfo.objects.all()
    print(type(data_list), data_list)
    for obj in data_list:
        print(obj.name, obj.password, obj.age)

    data_list = UserInfo.objects.filter(id = 1)
    print(data_list)
    # # 注意，返回的是一个QuerySet对象列表，如果要以这种方式获取，必须要通过索引的方式去使用
    obj = data_list[0]
    print(obj.id, obj.name, obj.password,  obj.age)
    
    # 如果知道获取的数据只有一行，则可以使用.first()方法直接获取到QuerySet对象，也就是取查询返回的QuerySet对象列表中的第一个元素
    obj = UserInfo.objects.filter(id = 1).first()
    print(obj.id, obj.name, obj.password,  obj.age)

    # 4、更新数据 先做条件过滤，再做更新数据的update操作。
    UserInfo.objects.all().update(age = 20)
    UserInfo.objects.filter(id = 1).update(password = 1234)


    return HttpResponse('执行成功')
```

### 6.用户管理案例

1. 在view.py中定义增删查方法

   ```python
   def user_list(request):
       # 查询获取数据库中的全部信息
       data_obj = UserInfo.objects.all()
       return render(request, 'user_list.html', {'data_obj':data_obj})
   
   def user_add(request):
       # 添加一个用户
       if request.method == 'GET':
           return render(request, 'user_add.html')
       # request.POST返回的是一个QueryDict对象，可以使用字典的方法
       name = request.POST.get('user')
       password = request.POST.get('pwd')
       age = request.POST.get('age')
       UserInfo.objects.create(name=name, password=password, age=age)
       return redirect('/user/list')
   
   def user_delete(request):
       # 删除用户
       uid = request.GET.get('uid')
       UserInfo.objects.filter(id = uid).delete()
       return redirect('/user/list/')
   ```

2. 在url中绑定和views.py的路由关系

   ```python
       # 用户管理案例
       path('user/list/', views.user_list),
       path('user/add/', views.user_add),
       path('user/delete/', views.user_delete)
   ```

3. 在templates目录下编写HTML页面

   ```python
   # 1、用户列表
   <body>
       <h1>用户列表</h1>
       <a href="/user/add/">添加用户</a>
       <table border="1">
           <thead>
               <tr>
                   <th>ID</th>
                   <th>姓名</th>
                   <th>密码</th>
                   <th>年龄</th>
                   <th>操作</th>
               </tr>
           </thead>
           <tbody>
               {% for obj in data_obj %}
                   <tr>
                       <th>{{ obj.id }}</th>
                       <th>{{ obj.name }}</th>
                       <th>{{ obj.password }}</th>
                       <th>{{ obj.age }}</th>
                       <!-- 通过定义一个删除按钮，通过get方法传参id，以id的方式删除用户信息 -->
                       <th><a href="/user/delete/?uid={{ obj.id }}">删除</a></th>
                   </tr>
               {% endfor %}
           </tbody>
       </table>
   </body>
   
   # 2、新增用户
   <body>
       <h1>添加用户</h1>
       <form method="post">
           <!-- 必须要写 {% csrf_token %} 否则会报错-->
           {% csrf_token %}
           <input type="text" name="user" placeholder="用户名">
           <input type="password" name="pwd" placeholder="密码">
           <input type="text" name="age" placeholder="年龄">
           <input type="submit" placeholder="提交">
       </form>
   </body>
   ```



---



# Django实战项目案例

## 一、创建项目及App

```python
# 创建项目
django-admin.exe startproject usermanagementsystem
# 创建App
python.exe manage.py startapp manageweb
```

创建完成之后，将App绑定到settings.py

## 二、修改models.py，创建模型映射

以下列举了常见数据类型model映射的创建方法，其中包括了外键创建方法

```python
from django.db import models

# Create your models here.
class Department(models.Model):
    '''部门表'''
    title = models.CharField(verbose_name='部门名称', max_length='32')
    depart_id = models.SmallIntegerField(verbose_name='部门ID')


class UserInfo(models.Model):
    '''用户信息表'''
    name = models.CharField(verbose_name='姓名', max_length='16')
    password = models.CharField(verbose_name='密码', max_length='64')
    age = models.SmallIntegerField(verbose_name='年龄')
    # 定义一个元组，存储gender性别的对应关系，这个是DJango中的约束，和数据库无关
    gedner_choices = (
        (1, '男'),
        (2, '女')
    )
    gender = models.SmallIntegerField(verbose_name='性别', choices= gedner_choices)
    # decimal准确的小数值，max_digits代表数字总个数（负号不算），decimal_places是小数点后个数。（max_digits最大值为65，decimal_places最大值为30）
    account = models.DecimalField(verbose_name='账户余额', max_digits=10, decimal_places=2, default=0)
    crate_time = models.DateTimeField(verbose_name='入职时间')
    # 外键创建
    # 这样去创建depart_id列是没有约束的
    # depart_id = models.BigIntegerField(verbose_name='部门ID')
    # 1.有约束、带外键的创建方法
    #  - to表示与哪一张表关联
    #  - to_field表示与表中的那一列关联
    # models.ForeignKey（to="Department", to_field="depart_id"）
    # 2.DJango会自动将depart转换为depart_id，生成数据列`name`_id，_id是固定的增加的
    # depart = models.ForeignKey（to="Department", to_field="depart_id"）创建的列名为depart_id
    # 3.当外键关联的父类表格（列）被删除了，有多种处理方式,例如:
    #  - 级联删除子表格中所有数据
    # depart = models.ForeignKey(to="Department", to_field="depart_id", on_delete=models.CASCADE)
    #  - 在允许列为空的条件下，将子表中数据置空
    # depart = models.ForeignKey(to="Department", to_field="depart_id", null=True, blank=True, on_delete=models.SET_NULL)
    #  - 在有默认值的情况下，设置被删除的值为默认值
    depart = models.ForeignKey(to="Department", to_field="depart_id", default= 10, on_delete=models.SET_DEFAULT)
```



