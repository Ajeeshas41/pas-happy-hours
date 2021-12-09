from django.shortcuts import render

def home(request):
    return render(request, 'main/index.html')

def game(request):
    return render(request, 'main/game.html')

def result(request):
    return render(request, 'main/result.html')
