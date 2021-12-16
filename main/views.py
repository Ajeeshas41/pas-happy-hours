from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = 'main/index.html'

class SelectGameView(LoginRequiredMixin, TemplateView):
    template_name = 'main/game.html'

class ResultView(TemplateView):
    template_name = 'main/result.html'
