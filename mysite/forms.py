from django import forms
from .models import House

class HouseCreateForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ['name','rent','area','bedrooms','parking','img','bedrooms','description','Owner','address','ListedByOwner','Type']
