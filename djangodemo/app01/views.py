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
    return render(request, 'tmp.html', {'n1': name, 'n2': l, 'n3':dic})