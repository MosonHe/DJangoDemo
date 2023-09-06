from django.shortcuts import render, redirect
from manageweb import models

# Create your views here.

def depart_info(request):
    # 返回的是queryset对象列表
    obj_list = models.Department.objects.all()
    return render(request, 'depart_info.html', {'obj_list':obj_list})

def depart_add(request):
    if request.method == 'GET':
        return render(request, 'depart_add.html')
    title = request.POST.get('title')
    depart_id = request.POST.get('depart_id')
    desc = request.POST.get('desc')
    result = models.Department.objects.create(title = title, depart_id = depart_id, desc = desc)
    return redirect('/depart/info/')

def depart_delete(request):
    # 获取nid
    nid = request.GET.get('nid')
    # 删除
    models.Department.objects.filter(id = nid).delete()
    return redirect('/depart/info/')


def depart_edit(request, nid):
    if request.method == 'GET':
        first_obj = models.Department.objects.filter(id = nid).first()
        return render(request, 'depart_edit.html', {'first_obj':first_obj})
    title = request.POST.get('title')
    depart_id = request.POST.get('depart_id')
    desc = request.POST.get('desc')
    models.Department.objects.filter(id = nid).update(title = title, depart_id=depart_id, desc=desc)
    return redirect('/depart/info/')

def user_info(request):
    # 返回的是一个queryset对象列表，需要用循环的方式获取。
    obj_list = models.UserInfo.objects.all()
    for obj in obj_list:
        # 在Python中获取时间字符，对datetime类型进行字符串格式化
        create_time = obj.crate_time.strftime("%Y-%m-%d")
        # 这样子获取性别，获取到的是gender在数据库中的值，实际为1和2，不明显
        # gender = obj.gender
        # 在定义模型类的时候,加入了gedner_choices元组做约束，想要获取键的详细值可以使用如下方法
        gender = obj.get_gender_display()
        # 在模型类中定义了外键ForeignKey（或者OneToOneField）
        # 可以直接获取外键depart_id在主表中的详细信息，可以使用如下方法
        '''
        例：在数据库中depart存储时候是默认加上了_id后缀的，在数据库存储的表字段为depart_id，
        在使用的时候，如果直接用定义的字段名称depart，就可以直接做到连表查询的效果,获取到主表的表结构信息
        '''
        depart_id = obj.depart.title
        print(create_time, gender, depart_id)

    
    return render(request, 'user_info.html', {'obj_list':obj_list})