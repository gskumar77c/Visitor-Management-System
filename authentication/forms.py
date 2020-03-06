from .models import User
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField



class UserCreationForm(forms.ModelForm):

	password1 = forms.CharField(label='password',widget=forms.PasswordInput)
	password2 = forms.CharField(label='confirm password',widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ('email','fullname')

	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		if password2 and password1 and password1 != password2 :
			raise forms.ValidationError("passwords do not match")
		return password1

	def save(self,commit=True):
		user = super().save(commit=False)
		user.set_password(self.cleaned_data['password1'])
		if commit:
			user.save()
		return user



class UserChangeForm(forms.ModelForm):
	password = ReadOnlyPasswordHashField()

	class Meta:
		model  = User
		fields = ('email','password','fullname','is_active','is_admin')

	def clean_password(self):
		return self.initial['password']