from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .form import CreateUserForm
from django.contrib import messages

# Create your views here.
def userReg(request):
    page = 'Register'
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User Registered Successfully.')
            return redirect('login')
        else:
            messages.warning(request, 'Something wrong! Try again.')


    context = {'page':page, 'form':form}
    return render(request, 'users/app.html', context)



def userLog(request):
    page = 'Login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'User Logged in Successfully...')
            return redirect('welcome')
        else:
            messages.warning(request, 'username or password is incorrect!')
    context = {'page':page}
    return render(request, 'users/app.html', context)

def userOut(request):
    logout(request)
    messages.success(request, 'User Logged out.')
    return redirect('login')

def welcome(request):
    return render(request, 'users/after.html')