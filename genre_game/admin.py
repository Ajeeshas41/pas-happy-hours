from django.contrib import admin

from .models import Genre, GenreTeam, Game, Question

admin.site.register(Genre)
admin.site.register(GenreTeam)
admin.site.register(Game)
admin.site.register(Question)