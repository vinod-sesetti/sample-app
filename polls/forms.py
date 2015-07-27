from django import forms
from .models import Question, Post

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


class CommentForm(forms.Form):
    comment = forms.CharField(max_length=300)
    # class Meta:
    #     model = Question
    #     fields = ('question')



    # def save(self, commit=True):
    #     print self 
    #     user = User.objects.get("user_id")   
    #     # user = User.objects.create_user(
    #     #     username=self.cleaned_data.get("username"),
    #     #     first_name=self.cleaned_data["first_name"],
    #     #     last_name=self.cleaned_data["last_name"],
    #     #     email=self.cleaned_data["email"],
    #     #     )
    #     # user.set_password(self.cleaned_data["password1"])

    #     if commit:
    #         user.save()
    #     return user 


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # exclude = ['author', 'updated', 'created', ]
        fields = ['text']
        widgets = {
            'text': forms.TextInput(
                attrs={'id': 'post-text', 'required': True, 'placeholder': 'Say something...'}
            ),
        }   