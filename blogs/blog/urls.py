from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    #视图函数
    # path('',views.index,name='index'),
    # path('posts/<int:pk>/',views.detail,name='detail'),
    # path('archives/<int:year>/<int:month>/',views.archive,name='archive'),
    # path('categories/<int:pk>/',views.category,name='category'),
    # path('tag/<int:pk>/',views.tag,name='tag'),
    path('search/',views.search,name='search'),


    #类视图
    path('',views.IndexView.as_view(),name='index'),
    path('categories/<int:pk>/',views.CategoryView.as_view(),name='category'),
    path('posts/<int:pk>/',views.PostDetailView.as_view(),name='detail'),
    path('archives/<int:year>/<int:month>/',views.archiveView.as_view(),name='archive'),
    path('tag/<int:pk>/',views.tagView.as_view(),name='tag'),

]