from django.shortcuts import render

# Create your views here.


def main(request):
    return render(request, 'parser_vk_post/base.html')


def all_posts(request):
    posts = [x for x in range(10)]
    return render(request, 'parser_vk_post/all_posts.html', context={'posts': posts})
