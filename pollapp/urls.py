from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [

    path('main', views.main, name='main'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('log', views.login, name='login'),
    path('home', views.home, name='home'),
    path('homepage', views.homepage, name='homepage'),

    path('', views.userpage, name='userpage'),
    path('uspg', views.uspg, name='uspg'),


     path('', views.main, name='main'),

    path('index', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
