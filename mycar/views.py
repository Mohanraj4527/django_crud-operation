from django.shortcuts import render,redirect
from .models import myuser

def index(request):
    return render(request,'./home/home.html')

def about(request):
    return render(request,'./about/about.html')

def product(request):
    items=[
        
       {"title": "Nexon","text": "The car is tata product","price": 500000},
       {"title": "Punch","text": "The car is tata product","price": 600000},
       {"title": "Sfari","text": "The car is tata product","price": 400000},
       {"title": "Harrier","text": "The car is tata product","price": 300000},
       {"title": "Tigor","text": "The car is tata product","price": 600000},
       {"title": "Altros","text": "The car is tata product","price": 400000},
       {"title": "Tiago","text": "The car is tata product","price": 500000},
       {"title": "Curvv","text": "The car is tata product","price": 600000},
       {"title": "Tigor Ev","text": "The car is tata product","price": 400000},
       {"title": "Nexon Ev","text": "The car is tata product","price": 500000},
       {"title": "Punch Ev","text": "The car is tata product","price": 600000},
       {"title": "Tiago EV","text": "The car is tata product","price": 400000}
    ]         


    return render(request,'./product/product.html',{"items":items})
 
def contact(request):
     return render(request,'./contact/contact.html')

def petrol(request):
     return render(request,'./petrol/petrol.html')

def nexon(request):
    return render(request,'./petrol/nexon/nexon.html')

def punch(request):
    return render(request,'./petrol/punch/punch.html')

def curvv(request):
    return render(request,'./petrol/curvv/curvv.html')

def tiago(request):
    return render(request,'./petrol/tiago/tiago.html')

def registerform (request):
    return render(request,'./form/registerform.html')

def register (request):
    
    Name=request.POST.get("name")
    Age=request.POST.get("age")
    Phone=request.POST.get("phone")
    Email=request.POST.get("email")
    Model=request.POST.get("model")
    Price=request.POST.get("price")

    user=myuser(Name=Name,Age=Age,Phone=Phone,Email=Email,Model=Model,Price=Price)
    user.save()
 
    return render(request,'./form/register.html',{"myuser":user})

def data(request):
    user=myuser.objects.all()
    return render(request,'./form/data.html',{"myusers":user})

def update(request,id):
    user=myuser.objects.get(id=id)
    return render(request,'./form/update.html',{"user":user})

def updaterec(request,id):
    user=myuser.objects.get(id=id)
    Name=request.POST.get("name")
    Age=request.POST.get("age")
    Phone=request.POST.get("phone")
    Email=request.POST.get("email")
    Model=request.POST.get("model")
    Price=request.POST.get("price")
    user.Name=Name
    user.Age=Age
    user.Phone=Phone
    user.Email=Email
    user.Model=Model
    user.Price=Price
    user.save()
    return redirect('/data')

def delete(request,id):
    user=myuser.objects.get(id=id)
    user.delete()
    return redirect('/data')

 
