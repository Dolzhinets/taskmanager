from django.urls import path
from .import views

urlpatterns = [
        path('', views.index, name='home'), # name='home' - для перехода на страницу. в файле base.html
        path('about', views.about, name='about'), # вставляется {% url 'home' %}"
        path('create', views.create, name='create')
]