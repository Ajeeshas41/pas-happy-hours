from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.contrib import messages

from .forms import TeamForm
from .models import Team, Participant

@login_required
def register_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            available = Team.objects.filter(user = request.user).exists()
            if not available:
                team = form.save(commit=False)
                team.user = request.user
                team.save()
                participant = Participant.objects.get(user=request.user)
                participant.team = team
                participant.save()
                messages.success(request, f'You have successfully created the team - { team.teamname }')
                return redirect('team-details', pk=team.pk)
            else:
                messages.error(request, 'Team already available')
                return redirect('team-list')
    else:
        form = TeamForm()

    return render(request, 'team/register.html', {'form': form})

def setup_team(request):
    form = TeamForm()
    return render(request, 'team/team_setup.html', {'form': form})

@login_required
def join_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            try:
                team_exists = Team.objects.get(teamname=form.cleaned_data.get('teamname'), securitykey=form.cleaned_data.get('securitykey'))
            except:
                team_exists = None

            if team_exists:
                participant = Participant.objects.get(user=request.user)
                participant.team = team_exists
                participant.save()
                messages.success(request, f'You have added to the team { participant.team.teamname }')
                return redirect('team-details', pk=team_exists.pk)
            else:
                messages.error(request, 'Entered team name or security key is incorrect!')
        return redirect('join-team')
    else:
        form = TeamForm()
    
    return render(request, 'team/team_join.html', {'form': form})

class TeamListView(ListView):
    model = Team
    template_name = 'team/team_list.html'
    context_object_name = 'teams'

    def get_queryset(self):
        return Team.objects.filter(is_active=True)


class TeamDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Team
    template_name = 'team/team_details.html'

    def test_func(self):
        team = self.get_object()
        return self.request.user.participant.team.id == team.id
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Participant.objects.filter(team=self.get_object()).count()
        context['participant'] = c
        return context
