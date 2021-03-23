from django.contrib import admin
from .models import Genre, Movie


# 创建页面展示的内容
class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


class MovieAdmin(admin.ModelAdmin):
    # filter = ("title", "genre")
    exclude = ('date_created', )
    list_display = ('title', 'number_in_stock', 'daily_rate', 'date_created')


# Register your models here.
admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
