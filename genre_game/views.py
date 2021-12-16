from django.shortcuts import render, redirect
from django.http import JsonResponse, request
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils import timezone

from .models import Genre, Game, Question


class LockGameView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    def get(self, request, id, status):
        game = Game.objects.get(id=id)
        team = game.team
        if status:
            game.won = 1
            game.is_locked = 1
            team.score += 5
        
        else:
            game.is_locked = 1
        
        game.enabled = 0
        game.save()
        team.save()
        return redirect('genre-game-home')

    def test_func(self):
        return self.request.user.is_staff

class GetAnswerView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):

    def post(self, request, id):
        game = Game.objects.get(id=id)
        original_answer = game.question.answer
        input_answer = game.answer
        game.is_locked = 1
        game.save()

        data = {'oAnswer':'', 'iAnswer': ''}
        if original_answer:
            data['oAnswer'] = original_answer

        if input_answer:
            data['iAnswer'] = input_answer

        return JsonResponse(data)

    def test_func(self):
        return self.request.user.is_staff

class UpdateGenreView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):

    def get(self, request, id, genre):
        genre = Genre.objects.get(id=genre)
        game = Game.objects.get(id=id)
        game.genre = genre
        game.save()
        return redirect('game-question')
    
    def test_func(self):
        return self.request.user.is_staff

class UpdateGameView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    
    def post(self, request, id):
        q = request.POST.get('id')
        question = Question.objects.get(id=q)
        question.is_locked = 1
        question.save()

        game = Game.objects.get(id=id)
        game.question = question
        game.started_at = timezone.now()
        game.enabled = 1
        game.save()
        return redirect('genre-game-home')
    
    def test_func(self):
        return self.request.user.is_staff

class GameGenreView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'genre_game/genre.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        genre = Genre.objects.filter(is_active=True)
        game = Game.objects.filter(is_locked=False).first()
        team_games = Game.objects.filter(team=game.team)
        played_genre = []
        for t in team_games:
            played_genre.append(t.genre)

        context['start'] = True

        if game:
            context['game'] = game
        if genre:
            context['genre'] = genre
        if played_genre:
            context['played_genre'] = played_genre
            
        return context
    
    def test_func(self):
        return self.request.user.is_staff

class GameQuestionView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'genre_game/game.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        game = Game.objects.filter(is_locked=False).first()
        genre = game.genre
        questions = Question.objects.filter(is_active=True, genre=genre)
        if game:
            context['game'] = game
        if genre:
            context['questions'] = questions
            
        return context
    
    def test_func(self):
        return self.request.user.is_staff






class GameUserView(LoginRequiredMixin, TemplateView):
    template_name = 'genre_game/game_user.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            game = Game.objects.filter(enabled=True).first()
            team = game.team.team
            if self.request.user.participant.team != team:
                game = None
        except:
            game = None

        if game:
            context['game'] = game
            
        return context
    
    
class GameUserUpdateView(LoginRequiredMixin, TemplateView):
    
    def post(self, id):
        g = self.request.POST.get('id')
        overriden = self.request.POST.get('override')
        game = Game.objects.get(id=g)

        if game.team.team == self.request.user.participant.team:

            if not game.enabled:
                data = {'err': '0'}
                return JsonResponse(data)
            
            if game.is_locked:
                data = {'err': 'Answer locked, you are unable to submit the new answer'}
                return JsonResponse(data)

            if overriden == 'true':
                pass
            elif game.is_submitted:
                data = {'err': 'Answer already submitted, if you want to continue, please check the override box and submit again'}
                return JsonResponse(data)
            
            game.answer = self.request.POST.get('answer')
            game.is_submitted = 1
            game.submitted_at = timezone.now()
            game.submitted_by = self.request.user
            game.save()              

            data = {'ok': 'Answer submitted'}
            return JsonResponse(data)
            
        
        data = {'err': '0'}
        return JsonResponse(data)
    