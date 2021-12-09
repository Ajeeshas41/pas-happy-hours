"""pashappyhours URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView

from main.views import home, game, result
from user.views import UserLoginView, register_user
from team.views import  register_team, join_team, setup_team, TeamListView, TeamDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('register-user/', register_user, name='register-user'),
    path('logout/',LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('setup-team/', setup_team, name='setup-team'),
    path('register-team/', register_team, name='register-team'),
    path('join-team/', join_team, name='join-team'),
    path('setup-team/', setup_team, name='setup-team'),
    path('team/', TeamListView.as_view(), name='team-list'),
    path('team-detail/<int:pk>/', TeamDetailView.as_view(), name='team-details'),
    path('game-home/', game, name='game-home'),
    path('result/', result, name='result'),
]
