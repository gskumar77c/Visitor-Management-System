from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserCreationForm

def home(request):
	return render(request,'home.html')




def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		form.save()
		return redirect('login')

	form = UserCreationForm()
	return render(request,'register.html',{'form':form})