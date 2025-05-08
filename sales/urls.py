from django.urls import path
from . import views

urlpatterns =[
    path('',views.index,name='index'),
    path('category',views.category,name='category'),
    path('items/<str:cat>/',views.items,name='items'),
    path('search',views.search,name='search'),
    path('scroll',views.infinite_scroll,name='scroll'),
    path('help',views.help,name='help'),
    path('about',views.about,name='about')
]