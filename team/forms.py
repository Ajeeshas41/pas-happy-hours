from django import forms
from .models import Team

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        widgets = {
            'teamname' : forms.TextInput(
                attrs={'placeholder': '', 'autocomplete': 'off'}
            ),
            'securitykey' : forms.TextInput(
                attrs={ 'placeholder': '', 'autocomplete': 'off'}
            ),
        }
        labels = {
            'teamname': 'Team Name',
            'securitykey': 'Security Key'
        }
        error_messages = {
            'teamname': {
                'max_length': '1 user can add one team',
            },
        }

        fields = ['teamname','securitykey']