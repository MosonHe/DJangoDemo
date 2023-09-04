from django.shortcuts import render, HttpResponse, redirect
from app01.models import UserInfo, Department


# Create your views here.
def index(request):
    return render(request=request, template_name='index.html')

def test(request):
    return HttpResponse('Hello World')

def tmp(request):
    name = 'xiaoming'
    l = ['上午', '中午', '下午']
    dic = {'姓名':'小明', '年龄':17, '性别':'男'}
    import requests
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62',
        'Referer': 'http://www.chinaunicom.com.cn/news/list202308.html'
    }
    try:
        rs = requests.get('http://www.chinaunicom.com.cn/api/article/NewsByIndex/2/2023/08/news', headers=headers)
        data_dict = rs.json()
    except Exception as ex:
        print(ex)
    return render(request, 'tmp.html', {'n1': name, 'n2': l, 'n3': dic, 'data_list': data_dict})

def req_resp(request):
    #  请求
    # 1、接收如request.method（返回request请求的方法）
    # print(request.method)
    # 2、接收GET请求，附带的参数信息，同理，接收POST方法的参数信息为request.POST
    # arg = request.GET
    # print(arg)
    # return HttpResponse(arg)
    #  响应
    # 3、返回 HttpResponse 对象中的content字符串信息
    # return HttpResponse('Hello World')
    # 4、返回render对象，首先读取HTML网页内容->将模板字符串替换，渲染页面->完成渲染之后，以字符串的方式返回给用户浏览器
    #  其中可以传递参数，常见数据类型都可以传递
    # return render(request, 'tmp.html', {'n1': name, 'n2': l, 'n3': dic, 'data_list': data_dict})
    # 5、返回redirect对象，让浏览器重定向到其他网页
    # return redirect('https://www.baidu.com')
    pass

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

def orm(request):
    # 使用DJango的ORM框架对数据做基本的增删改查操作。
    # 1、新建 使用模型类名.objects.create(**kwargs)来新增记录
    # Department.objects.create(title = '销售部')
    # Department.objects.create(title = 'IT部')
    # Department.objects.create(title = '运营部')

    # UserInfo.objects.create(name = 'hexs', password = '123', age = '18')
    # UserInfo.objects.create(name = 'zhangsan', password = '123', age = '28')
    # UserInfo.objects.create(name = 'lisi', password = '123', age = '38')

    # 2、删除 .filter()方法可以做条件过滤，然后再使用delete()方法删除。
    # UserInfo.objects.filter(id = 3).delete()

    # all()方法表示选择全部
    # Department.objects.all().delete()

    # 3、获取数据 模型类名.objects.all()或者模型类名.objects.filter()  
    # 返回的是一个QuerySet对象列表，可以通过.属性的方式去获取表字段属性
    # data_list = UserInfo.objects.all()
    # print(type(data_list), data_list)
    # for obj in data_list:
    #     print(obj.name, obj.password, obj.age)

    # data_list = UserInfo.objects.filter(id = 1)
    # print(data_list)
    # # 注意，返回的是一个QuerySet对象列表，如果要以这种方式获取，必须要通过切片的方式去使用
    # obj = data_list[0]
    # print(obj.id, obj.name, obj.password,  obj.age)
    
    # 如果知道获取的数据只有一行，则可以使用.first()方法直接获取到QuerySet对象，也就是取查询返回的QuerySet对象列表中的第一个元素
    # obj = UserInfo.objects.filter(id = 1).first()
    # print(obj.id, obj.name, obj.password,  obj.age)

    # 4、更新数据 先做条件过滤，再做更新数据的update操作。
    # UserInfo.objects.all().update(age = 20)
    # UserInfo.objects.filter(id = 1).update(password = 1234)


    return HttpResponse('执行成功')

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