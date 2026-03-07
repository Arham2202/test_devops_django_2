from django.shortcuts import render, redirect
from students.models import students

def  registration(request):
    user_data = students.objects.all() # SELECT * FROM TableOne
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
    
        
        students.objects.create(name= name, mobile= mobile, email= email)
        return redirect("/")

    return render(request, 'registration.html', {'data': user_data})

def studentlist(request):
    students = students.objects.all()
    return render(request, 'studentlist.html', {'students': students})