from . import views
from django.urls import include, path

urlpatterns = [
    path('', views.index, name = 'index'),
    path('home/', views.home, name = 'home'),
    path('create/', views.create, name='create')

]