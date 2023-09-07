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
    # for obj in obj_list:
    #     # 在Python中获取时间字符，对datetime类型进行字符串格式化
    #     create_time = obj.create_time.strftime("%Y-%m-%d")
    #     # 这样子获取性别，获取到的是gender在数据库中的值，实际为1和2，不明显
    #     # gender = obj.gender
    #     # 在定义模型类的时候,加入了gedner_choices元组做约束，想要获取键的详细值可以使用如下方法
    #     gender = obj.get_gender_display()
    #     # 在模型类中定义了外键ForeignKey（或者OneToOneField）
    #     # 可以直接获取外键depart_id在主表中的详细信息，可以使用如下方法
    #     '''
    #     例：在数据库中depart存储时候是默认加上了_id后缀的，在数据库存储的表字段为depart_id，
    #     在使用的时候，如果直接用定义的字段名称depart，就可以直接做到连表查询的效果,获取到主表的表结构信息
    #     '''
    #     depart_id = obj.depart.title
    #     print(create_time, gender, depart_id)    
    return render(request, 'user_info.html', {'obj_list':obj_list})

# 导入forms模块
from django import forms
# 定义模型类继承ModelForm
class UserModelForm(forms.ModelForm):
    # 默认只校验数据是否为空，如果需要定义某个字段的校验方法，需要自定义属性
    name = forms.CharField(min_length=3, label='姓名')

    # 默认定义model和fileds属性
    class Meta:
        model = models.UserInfo
        fields = ['name', 'password', 'age', 'gender', 'account', 'create_time', 'depart']
    # 重写__init__方法，在fields对象的插件方法中添加属性
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"placeholder":field.label}

def user_add(request):
    if request.method == 'GET':
        form = UserModelForm()
        return render(request, 'user_add.html', {'form':form})
    # 实例化modelform对象，将POST请求数据传递给modelform做数据校验
    # 如果在UserModelForm中定义的是默认的fields，则默认只校验数据是否为空
    form = UserModelForm(data = request.POST)
    # 如果数据校验成功
    if form.is_valid():
        form.save()
        return redirect('/user/info/')
    # 数据校验失败
    return render(request, 'user_add.html', {'form':form}) 

def user_edit(request, nid):
    # 根据用户ID获取第一条数据
    first_obj = models.UserInfo.objects.filter(id = nid).first()
    if request.method == 'GET':
        # 实例化modelform对象，将返回的模型实例对象传递给instance参数，可以做到自动显示内容
        form = UserModelForm(instance = first_obj)
        return render(request, 'user_edit.html', {'form':form})
    # 将请求获取到的参数传递给modelform，将查询对象传递给instance，表示修改这个实例的数据，否则会新增一条数据
    form = UserModelForm(data = request.POST, instance = first_obj)
    # 数据校验成功
    if form.is_valid():
        form.save()
        return redirect('/user/info/')
    # 数据校验失败
    return render(request, 'user_edit.html/', {'form':form})

def user_delete(requst, nid):
    models.UserInfo.objects.filter(id = nid).delete()
    return redirect('/user/info/')

from django.core.exceptions import ValidationError
class UserModelForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ['name', 'password', 'age', 'gender', 'account', 'create_time', 'depart']
    def clean_name(self):
        # 使用self.cleaned_data['字段'] 来获取用户请求发送过来的某一个数据
        txt_name = self.cleaned_data["name"]
        # ORM模型中，`.exclude()`方法可以排除条件，`.exists()`可以判断某个条件是否存在值
        # `self.instance.pk`表示当前字段名实例的id
        exits = models.UserInfo.objects.exclude(id = self.instance.pk).filter(name = txt_name).exists()
        # 手动写校验要求，也是支持正则等等。
        if exits:
            raise ValidationError('姓名已经存在')
        # 满足要求就直接返回
        return txt_name