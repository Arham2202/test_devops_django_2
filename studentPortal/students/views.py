from django.shortcuts import render, redirect
from students.models import TableOne

def  home(request):
    user_data = TableOne.objects.all() # SELECT * FROM TableOne
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        
        file = request.FILES.get('file')
        
        TableOne.objects.create(name= name, mobile= mobile, email= email, file= file)
        return redirect("/")

    return render(request, 'home.html', {'data': user_data})
