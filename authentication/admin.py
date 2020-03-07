from django.contrib import admin
from .models import User,Profile
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm,UserChangeForm



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
admin.site.register(Profile)