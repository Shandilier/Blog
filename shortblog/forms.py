from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms
from .models import UserProfile,Blog
from django.contrib.auth.models import User


class EditProfileForm(UserChangeForm):
	class Meta:
		model=User
		fields={'first_name','last_name','password'}

class EditUserProfileForm(forms.ModelForm):
	class Meta:
		model=User
		fields={'first_name','last_name'}

class SignUpForm(UserCreationForm):
	
	Email_Id=forms.EmailField(max_length=100,help_text='Please enter a valid Email Address')

	class Meta:
		
		model=User
		fields=('username','first_name','last_name','Email_Id','password1','password2')

class BlogForm(forms.ModelForm):
	publish=forms.DateField(widget=forms.SelectDateWidget)
	class Meta:
		model=Blog
		fields = [
			
            "title",
            "content",
            "image",
            "draft",
            "publish",
]


