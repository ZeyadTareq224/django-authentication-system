from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


from.forms import CreateUserForm


def home(request):
	return render(request, 'accounts/home.html')



def account_login(request):
	if request.user.is_authenticated:
		return render(request, 'errors/unauthorized.html', status=401)
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, "Username Or Password Is Incorrect")
	return render(request, 'accounts/login.html')


def account_logout(request):
	logout(request)
	return redirect('account_login')



def account_signup(request):
	if request.user.is_authenticated:
		return render(request, 'errors/unauthorized.html', status=401)
	form = CreateUserForm()
	if request.method == "POST":
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('account_login')

			messages.success(request, 'Account Created Successfully')
			return redirect('account_login')
	context = {'form': form}
	return render(request, 'accounts/signup.html', context)
