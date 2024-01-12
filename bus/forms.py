from django import forms
from .models import Routes

class RouteForm(forms.Form):
    routes_dropdown = forms.ModelChoiceField(queryset=Routes.objects.values('route_number'))