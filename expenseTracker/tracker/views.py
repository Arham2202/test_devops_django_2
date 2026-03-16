from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from tracker.models import Expense, Income
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        User.objects.create_user(username=username, password=password)

        return redirect('login')

    return render(request, 'register.html')


def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect('dashboard')

    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    expenses = Expense.objects.filter(user=request.user)
    income = Income.objects.filter(user=request.user)

    total_expense = sum(e.amount for e in expenses)
    total_income = sum(i.amount for i in income)

    balance = total_income - total_expense

    context = {
        'expenses': expenses,
        'income': income,
        'total_expense': total_expense,
        'total_income': total_income,
        'balance': balance
    }

    return render(request, 'dashboard.html', context)


@login_required
def add_expense(request):
    if request.method == "POST":
        title = request.POST['title']
        category = request.POST['category']
        amount = float(request.POST['amount'])
        date = request.POST['date']

        Expense.objects.create(
            user=request.user,
            title=title,
            category=category,
            amount=amount,
            date=date
        )

        return redirect('dashboard')

    return render(request, 'add_expense.html')


@login_required
def add_income(request):
    if request.method == "POST":
        source = request.POST['source']
        amount = float(request.POST['amount'])
        date = request.POST['date']

        Income.objects.create(
            user=request.user,
            source=source,
            amount=amount,
            date=date
        )

        return redirect('dashboard')

    return render(request, 'add_income.html')


@login_required
def delete_expense(request, id):
    exp = Expense.objects.get(id=id)
    exp.delete()
    return redirect('dashboard')