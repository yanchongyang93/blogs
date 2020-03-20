#自定义模板标签代码
from django import template
from ..models import Post,Category,Tag
from django.db.models.aggregates import Count

register = template.Library()

@register.inclusion_tag('blog/inclusions/_recent_posts.html',takes_context=True)
def show_recent_posts(context,num=5):
    return {
        'recent_post_list':Post.objects.all().order_by('-created_time')[:num],
    }


@register.inclusion_tag('blog/inclusions/_archives.html',takes_context=True)
def show_archives(context):
    return {
        'data_list':Post.objects.dates('created_time','month',order='DESC'),
    }


@register.inclusion_tag('blog/inclusions/_categories.html', takes_context=True)
def show_categories(context):
    category_list = Category.objects.annotate(num_post=Count('post')).filter(num_post__gt=0)
    return {
        'category_list':category_list,
    }

@register.inclusion_tag('blog/inclusions/_tags.html',takes_context=True)
def show_tags(context):
    tag_list = Category.objects.annotate(num_post=Count('post')).filter(num_post__gt=0)
    return {
        'tag_list':tag_list,
    }



