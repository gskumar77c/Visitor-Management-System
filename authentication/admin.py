from django.contrib import admin
from .models import User
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


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


class UserAdmin(BaseUserAdmin):
	form = UserChangeForm
	add_form = UserCreationForm

	list_display = ('email','fullname','is_admin')
	list_filter = ('is_admin',)
	fieldsets = (
			(None,{'fields':('email','password')}),
			('Personal info',{'fields':('fullname',)}),
			('Permissions',{'fields':('is_admin',)}),
		)

	add_fieldsets = (
			(None,{
				'classes':('wide',),
				'fields':('email','fullname','password1','password2'),
				}),
		)
	search_fields = ('email','fullname')
	ordering = ('email',)
	filter_horizontal = ()


admin.site.register(User,UserAdmin)
admin.site.unregister(Group)