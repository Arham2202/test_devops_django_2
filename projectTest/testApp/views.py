from django.shortcuts import render, redirect
from testApp.models import TableOne

def home(request):
    user_data = TableOne.objects.all() # SELECT * FROM TableOne
    if request.method == 'POST':
        name = request.POST.get('var_name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        # file 
        file = request.FILES.get('file')
        # print(f"Name: {name}, Mobile: {mobile}, Email: {email}")
        TableOne.objects.create(name= name, mobile= mobile, email= email, file= file)
        return redirect("/")
    # json -> {}
    # data_front= {
    #     'data': user_data
    #     }
    return render(request, 'home.html', {'data': user_data})


'''
data = [{},{},{}]
'''