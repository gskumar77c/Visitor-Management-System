from .models import User,Profile
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField



class UserCreationForm(forms.ModelForm):

	password1 = forms.CharField(label='password',widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password *"}))
	password2 = forms.CharField(label='confirm password',widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Conform Password *"}))
	email  = forms.CharField(max_length=255,widget = forms.EmailInput(attrs={"class":"form-control","placeholder":"Email *"}))
	fullname = forms.CharField(max_length=200,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Full Name *"}))


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



class UserUpdateForm(forms.ModelForm):
	fullname = forms.CharField()

	class Meta:
		model = User
		fields = ['fullname']

class ProfileUpdateForm(forms.ModelForm):
	dob = forms.DateField(widget=forms.DateInput(attrs={"placeholder":"YYYY-MM-DD"}))
	class Meta:
		model = Profile
		fields = ['dob','address','image']