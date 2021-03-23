from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),  # name=XXX:为URL名称添加命名空间
    path('<int:movie_id>', views.detail, name='detail')  # <int:movie_id> 将movie_id转化为int
]
