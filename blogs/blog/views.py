from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post,Category,Tag

# Create your views here.
def index(request):
    #直接返回一个字符串
    # return  HttpResponse("welcome")

    # return render(request,'blog/index.html',context={
    #     'title': '我的博客首页',
    #     'welcome': '欢迎来到我的博客首页'
    # })
    post_list = Post.objects.all()
    return render(request,'blog/index.html',context={'post_list':post_list})



def detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request,'blog/detail.html',context={'post':post})


def archive(request,year,month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    )
    return render(request,'blog/index.html',context={'post_list':post_list})


def category(request,pk):
    cate = get_object_or_404(Category,pk=pk)
    post_list = Post.objects.filter(category=cate)
    return render(request,'blog/index.html',context={'post_list':post_list})


def tag(request,pk):
    t = get_object_or_404(Tag,pk=pk)
    post_list = Post.objects.filter(tags=t)
    return render(request,'blog/index.html',context={'post_list':post_list})