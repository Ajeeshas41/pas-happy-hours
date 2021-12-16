from django.urls import path
from .views import GameGenreView, GameQuestionView, UpdateGenreView, UpdateGameView, GetAnswerView, LockGameView, GameUserView, GameUserUpdateView

urlpatterns = [
    path('genre-admin/', GameGenreView.as_view(), name='genre-game-home-admin'),
    path('genre/', GameGenreView.as_view(), name='genre-game-home'),
    path('genre-update/<int:id>/<int:genre>/', UpdateGenreView.as_view(), name='genre-update'),
    path('question/', GameQuestionView.as_view(), name='game-question'),
    path('question-update/<int:id>/', UpdateGameView.as_view(), name='question-update'),
    path('get-answer/<int:id>/', GetAnswerView.as_view(), name='get-answer'),
    path('lock-game/<int:id>/<int:status>/', LockGameView.as_view(), name='lock-game'),
    path('user-game/', GameUserView.as_view(), name='user-game'),
    path('user-answer/', GameUserUpdateView.as_view(), name='user-answer'),
]