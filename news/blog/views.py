from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from blog.models import *

menu = [['Главная', '/'], ['Архив', '/archive/2022/'], ['О сайте', '/about/'], ['Добавить статью', '/'], ['Войти', '/']]


def home(request, cat_id):
    posts = Post.objects.all()
    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404

    context = {
        'menu': menu,
        'posts': posts,
        'cats': cats,
        'title': 'Главная страница',
        'cat_selected': cat_id,
    }

    return render(request, 'blog/home.html', context=context)


def about(request):
    return render(request, 'blog/about.html', {'menu': menu, 'title': 'О сайте'})


def categories(request, cat):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{cat}</p>")


def archive(request, year):
    if int(year) > 2022:
        return redirect('home', permanent=True)
    return render(request, 'blog/archive.html', {'menu': menu, 'year': year, 'title': f'Архив за {year} год'})


def show_category(request, cat_id):
    return HttpResponse(f"Отображение категории с oid = {cat_id}")


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена<h1>')
