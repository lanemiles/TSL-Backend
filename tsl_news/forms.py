# relevant imports
from django import forms


# create the form that the user's will use
class URLForm(forms.Form):
    url = forms.CharField(max_length=512)
