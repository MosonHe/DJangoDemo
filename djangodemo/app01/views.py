from django.shortcuts import render, HttpResponse

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