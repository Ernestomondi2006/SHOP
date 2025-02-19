
from django.contrib import admin
from django.urls import path
from shopapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('gallary/', views.images,name='gallary'),
    path('about/', views.about,name='about'),
]
