from django.shortcuts import render, redirect
from todo_application.models import Task
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password) # this is done on the User data table 
        print(user, username, password)
        if user is not None:
            login(request, user)
            return redirect('home')
            
    return render(request, 'login.html')

def registration(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        user = User.objects.create_user(username= username, email=email, password = password)
        user.save()
        
        return redirect('login')
    return render(request, 'reg.html')

@login_required   
def home(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        created_on = request.POST.get('created_on')
        deadline = request.POST.get('deadline')

        task = Task(user=request.user, title=title, description=description, created_on=created_on, deadline=deadline)
        task.save()
        
        return redirect('task')
    return render(request, 'home.html')

@login_required   
def home(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        created_on = request.POST.get('created_on')
        deadline = request.POST.get('deadline')

        task = Task(user=request.user, title=title, description=description, created_on=created_on, deadline=deadline)
        task.save()
        
        return redirect('task')
    return render(request, 'home.html')

@login_required
def taskUpdate(request, id):
    task = Task.objects.get(pk = id, user=request.user)
    task.completed = True
    task.save()
    return redirect('task')

@login_required
def taskDelete(request, id): 
    task = Task.objects.get(pk = id, user=request.user)
    task.delete()
    return redirect('task')

