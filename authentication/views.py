from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserCreationForm,UserUpdateForm,ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile,User


@login_required
def home(request):
	return render(request,'authentication/home.html')




def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			usr = User.objects.get(email = form.cleaned_data.get('email'))
			pf = Profile(user = usr)
			pf.save()
			return redirect('login')
		else:
			usr = form.cleaned_data.get('email')
			if usr==None:
				messages.warning(request, 'Invalid email address')
			else :
				pas1 = form.cleaned_data.get('password1')
				pas2 = form.cleaned_data.get('password2')
				if(pas1 != pas2) :
					messages.warning(request, 'confirm password must be same as password')

	form = UserCreationForm()
	return render(request,'authentication/register.html',{'form':form})


@login_required
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST,
			instance = request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, 
			instance = request.user.profile)

		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request,f'Account has been updated')
			return redirect('profile')

	else :
		u_form = UserUpdateForm(instance = request.user)
		p_form = ProfileUpdateForm(instance = request.user.profile)

	context = {'u_form' : u_form,
				'p_form' : p_form
				}
	return render(request,'authentication/profile.html',context)