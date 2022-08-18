from ast import Pass
import email
from email import message
from multiprocessing import context
from django.shortcuts import redirect, render
from django.http import HttpResponse
from . models import Person
from .forms import PersonForm
from django.contrib.auth.models import User
# for flash messages
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username == '':
            messages.error(request, 'Username is required')
        elif password == '':
            messages.error(request, 'password required')
        user = authenticate(request, username=username, password=password)
        if username and password != '':
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Wrong Username and password')
    context = {}
    return render(request, 'base/login_register.html', context)


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
            User.objects.create_user(username, email, password)
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            messages.error('Looks like a username with that email or password already exists')
    return render(request, 'base/Create.html')


def home(request):
    users = {}
    if request.user.is_authenticated:
        user = request.user
        q = request.GET.get('q')
        if q != None:
            users = Person.objects.filter(Person_name__icontains=q)
        else:
            users = Person.objects.filter(user=user)
        return render(request, 'base/home.html', {'users': users})
    else:
        return redirect('login')


def CreateUser(request):
    if request.user.is_authenticated:
        user = request.user
        form = PersonForm()
        if request.method == 'POST':
            form = PersonForm(request.POST)
            if form.is_valid():
                cu = form.save(commit=False)
                cu.user = user
                cu.save()
            return redirect('home')
        context = {'form': form}
        return render(request, 'base/register_form.html', context)
    else:
        return render(request, 'base/login_register.html')


def DeletePerson(request, pk):
    person = Person.objects.get(id=pk)
    if request.method == 'POST':
        person.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': person})


def UpdatePerson(request, pk):
    person = Person.objects.get(id=pk)
    form = PersonForm(instance=person)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}

    return render(request, 'base/register_form.html', context)


def logoutPage(request):
    logout(request)
    return redirect('login')
