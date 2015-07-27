
from django import forms

from models import UploadFile,User
class UploadFileForm(forms.ModelForm):
    
    class Meta:
        model = UploadFile
        fields = ('file',)

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email',)
       