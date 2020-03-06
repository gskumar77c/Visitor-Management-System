from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserCreationForm
from django.contrib import messages

def home(request):
	return render(request,'home.html')




def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
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
	return render(request,'register.html',{'form':form})