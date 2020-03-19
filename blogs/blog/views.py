from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post,Category,Tag

from django.views.generic import ListView,DetailView


# Create your views here.
'''
这个是视图函数，需要改写成类的通用视图
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
    post.increase_view()
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

'''

class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'


class CategoryView(IndexView):
    def get_queryset(self):
        cate = get_object_or_404(Category,pk=self.kwargs.get('pk'))
        return super().get_queryset().filter(category=cate)


class archiveView(IndexView):
    def get_queryset(self):
        cate = get_object_or_404(Post,created_time__year=self.kwargs.get('year'),
                                 created_time__month=self.kwargs.get('month'))
        return super().get_queryset().filter(category=cate)


class tagView(IndexView):
    def get_queryset(self):
        tag = get_object_or_404(Tag,pk=self.kwargs.get('pk'))
        return super().get_queryset().filter(tags=tag)



class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        response = super().get(request,*args,*kwargs)
        self.object.increase_view()
        return response


