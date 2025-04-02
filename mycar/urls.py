from django.urls import path
from .views import index,about,product,contact,petrol,nexon,punch,curvv,tiago,registerform,register,data,update,updaterec,delete

urlpatterns=[
    path ('',index,name="index"),
    path('about',about,name="about"),
    path('product',product,name="product"),
    path('contact',contact,name="contact"),
    path('petrol',petrol,name="petrol"),
    path('petrol/nexon',nexon,name="nexon"),
    path('petrol/punch',punch,name="punch"),
    path('petrol/curvv',curvv,name="curvv"),
    path('petrol/tiago',tiago,name="tiago"),
    path('registerform',registerform,name="registerform"),
    path('register',register,name="register"),
    path('data',data,name="data"),
    path('update/<int:id>/',update,name="update"),
    path('update/updaterec/<int:id>/',updaterec,name="updaterec"),
    path('delete/<int:id>/',delete,name="delete")
]