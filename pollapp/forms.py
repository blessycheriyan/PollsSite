from django import forms

from pollapp.models import users




class userform(forms.ModelForm):
    class Meta():
        model = users
        fields = "__all__"