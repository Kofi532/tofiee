from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Member

class memberf(forms.ModelForm):
	class Meta:
		model = Member
		fields = ["username","price","title","region","city","description","size","contact", "dp","pic1","pic2","pic3","pic4","pic5","pic6","rooms","bathrooms","utilities","category"] #username,active,slug
		widgets = {'username': forms.HiddenInput(),'region':forms.HiddenInput(),'city':forms.HiddenInput()}
    

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user