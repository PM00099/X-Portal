from django.urls import path,include
from .views import signup,login,logout,show


urlpatterns = [
     path('signup',signup,name='signup'),
     path('login',login,name='login'),
     path('logout',logout,name='logout'),
     path('show',show,name='show'),
]
 