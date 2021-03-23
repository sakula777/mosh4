from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Movie


# Create your views here.


def index(request):
    movies = Movie.objects.all()  # 获取Movie中所有的信息
    # select * from movies_movie

    # Movie.objects.filter(release_year=1984)
    # # select * from movies_movie where release=1984
    #
    # Movie.objects.get(id=1)  # 返回一条
    # output = ', '.join([m.title for m in movies])  # 获取Movie中所有的title，并格式化为字符串
    # return HttpResponse(output)  # 响应到页面
    # 结合一个给定的模板和一个给定的上下文字典，并返回一个渲染后的 HttpResponse 对象。
    # 通俗的讲就是把context的内容, 加载进templates中定义的文件, 并通过浏览器渲染呈现.
    # render(request, template_name, context=None, content_type=None, status=None, using=None):
    return render(request, 'movies/index.html', {'movies': movies})


def detail(request, movie_id):
    # return HttpResponse(movie_id)
    # try:
    #     movie = Movie.objects.get(pk=movie_id)
    #     return render(request, 'movies/detail.html', {'movie': movie})
    # except Movie.DoesNotExist:
    #     raise Http404()  # ()内可自定义提示语句
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})


