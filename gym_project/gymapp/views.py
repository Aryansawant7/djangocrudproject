from django.shortcuts import render
from django.shortcuts import redirect
from gymapp.models import Gym
# Create your views here.

def home(request):
    return render(request,'home.html')

def add(request):
    return render(request,'add.html')

def view(request):
    context={}
    data=Gym.objects.all()
    context['gym']=data
    return render(request,'view.html',context)

def save(request):
    t=request.POST['Name']
    a=request.POST['Plan']
    p=request.POST['Price']
    e=request.POST['Training']

    # print(t,a,p)
    b=Gym.objects.create(name=t,plan=a,price=p,training=e)
    b.save()
    return redirect('/view')

def deletecustomer(request,rid):
    a=Gym.objects.filter(id = rid)
    a.delete()
    return redirect('/view')

def updatecustomer(request,rid):
    gym=Gym.objects.filter(id = rid)
    context={}
    if request.method == 'GET':
        context['gym']= gym[0]
        return render(request,'updategym.html',context)
    else:   
        t=request.POST['Name']
        a=request.POST['Plan']
        p=request.POST['Price']
        e=request.POST['Training']
        gym.update(name=t,plan=a,price=p,training=e)
        return redirect('/view')
    




