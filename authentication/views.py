from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserCreationForm,UserUpdateForm,ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile,User,CheckInOut
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from django.contrib.auth import logout

@login_required
def home(request):
	usr = request.user
	if usr.is_admin :
		return redirect('../admin')
	gs =  CheckInOut.objects.filter(user = usr,checked=True)
	if gs.exists():
		return render(request,'authentication/home.html',{'check':True})
	else :
		return render(request,'authentication/home.html',{'check':False})




def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			usr = User.objects.get(email = form.cleaned_data.get('email'))
			pf = Profile(user = usr)
			pf.save()
			messages.warning(request, 'Account created Successfuly, Login!')
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



@login_required
def checkin_email(request):
	usr = request.user
	user = User.objects.get(email=usr)
	p = CheckInOut(user = user,checkin_time=timezone.now(),checked=True)
	p.save()
	s1 = p.__str__()
	s1 = s1.split('|')
	subject = 'Welcom to the Visitor Management System'
	message = f'Status : Checked In \nName: {user.fullname} \n{s1[0]}\n{s1[1]}\n{s1[2]}'
	email_from = settings.EMAIL_HOST_USER
	recipient_list = [usr,]
	try:
		send_mail( subject, message, email_from, recipient_list )
		messages.warning(request, 'CheckIn Successful!')
	except Exception as e:
		messages.warning(request, 'Problem in sending mail. Make sure your mail id is working')
	logout(request)
	return redirect('login')


@login_required
def checkout_email(request):
	usr = request.user
	user = User.objects.get(email=usr)
	p = user.checkinout_set.get(checked=True)
	p.checkout_time = timezone.now()
	p.checked = False
	p.save()
	s1 = p.__str__()
	s1 = s1.split('|')
	subject = 'Thank You for Visiting VMS'
	message = f'Status : Checked Out \n Name: {user.fullname} \n{s1[0]}\n{s1[1]}\n{s1[2]}\n{s1[3]}\n{s1[4]}'
	email_from = settings.EMAIL_HOST_USER
	recipient_list = [usr,]
	try:
		send_mail( subject, message, email_from, recipient_list )
		messages.warning(request, 'Checkout successful')
	except Exception as e:
		messages.warning(request, 'Checkout successful! , Problem in sending mail. Make sure your mail id is working')
	logout(request)
	return redirect('login')


@login_required
def view_log(request):
	usr =request.user
	user = User.objects.get(email=usr)
	p = user.checkinout_set.all().order_by('-checkin_time')
	
	return render(request,'authentication/view_log.html',{'q':p})