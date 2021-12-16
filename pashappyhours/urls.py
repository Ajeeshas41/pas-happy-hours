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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

from main.views import SelectGameView, HomeView, ResultView
from user.views import UserLoginView, register_user
from team.views import  register_team, join_team, setup_team, TeamListView, TeamDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('register-user/', register_user, name='register-user'),
    path('logout/',LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('setup-team/', setup_team, name='setup-team'),
    path('register-team/', register_team, name='register-team'),
    path('join-team/', join_team, name='join-team'),
    path('setup-team/', setup_team, name='setup-team'),
    path('team/', TeamListView.as_view(), name='team-list'),
    path('team-detail/<int:pk>/', TeamDetailView.as_view(), name='team-details'),
    path('game-home/', SelectGameView.as_view(), name='game-home'),
    path('result/', ResultView.as_view(), name='result'),
    path('genre-game/', include('genre_game.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)