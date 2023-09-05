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