"""
<<<<<<< HEAD
URL configuration for myproject project.
=======
URL configuration for myproject2 project.
>>>>>>> 20491f934666bd79a5b8c5dc2f756942736540cc

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
<<<<<<< HEAD
from  myapp import views
=======
from myapp import views
>>>>>>> 20491f934666bd79a5b8c5dc2f756942736540cc

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
<<<<<<< HEAD
    path("prediction/",views.prediction, name='prediction'),
    path("history/",views.history, name='history'),
=======
    path('prediction/',views.prediction,name='prediction'),
    path('history/',views.history,name='history'),
>>>>>>> 20491f934666bd79a5b8c5dc2f756942736540cc
]
