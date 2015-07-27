from django import forms
from demoapp.models import Note

class CreateNotesForm(forms.Form):
    title = forms.CharField(label='Title',max_length=1000,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Please enter Usefull Note Title here'}))
    body = forms.CharField(label='body',widget=forms.Textarea(attrs={'class':'form-control','placeholder': 'Please enter usefull description about the note'}))

    def clean(self):
        cleaned_data = super(CreateNotesForm, self).clean()
        title = cleaned_data.get("title")
        body = cleaned_data.get("body")
        if Note.objects.filter(title=title):
            raise forms.ValidationError('This Title is already in use. Please supply a different Title.')
