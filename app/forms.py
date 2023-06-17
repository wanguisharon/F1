from django import ModelForm
from .models import Team, Driver, Race

class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ["name", "country"]

class DriverForm(ModelForm):
    class Meta:
        model = Driver
        fields = ["user", "team", "country", "wheight_before", "weight_after"]

class RaceForm(ModelForm):
    class Meta:
        model = Race
        fields = ["driver", "country"]