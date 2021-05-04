from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'codetoanbug.com',
        'title': 'Bài đăng đầu tiên',
        'content': 'Đây là nội dung bài đăng đầu tiên.',
        'date_posted': 'May 4, 2021'
    },
{
        'author': 'codetoanbug.com',
        'title': 'Bài đăng thứ hai',
        'content': 'Đây là nội dung bài đăng thứ hai.',
        'date_posted': 'May 4, 2021'
    }
]
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
