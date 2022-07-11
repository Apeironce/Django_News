from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from blog.forms import AddPostForm
from blog.models import *

menu = [{'title': 'Главная', 'url_name': 'home'},
        {'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Войти', 'url_name': 'login'}
        ]


def home(request):
    posts = Post.objects.all()
    context = {
        'menu': menu,
        'posts': posts,
        'title': 'Главная страница',
        'cat_selected': 0,
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
    posts = Post.objects.filter(cat_id=cat_id)
    context = {
        'menu': menu,
        'posts': posts,
        'title': 'Отображение по категориям',
        'cat_selected': cat_id,
    }

    return render(request, 'blog/home.html', context=context)


def show_post(request, post_slug):
    post = get_object_or_404(Post, pk=post_slug)
    context = {
        'menu': menu,
        'posts': post,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, 'blog/post.html', context=context)


def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    return render(request, 'blog/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})


def login(request):
    return HttpResponse("Авторизация")


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена<h1>')
