from django.shortcuts import render
from .models import Appointment, BankUser

def appointment(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']
        reason = request.POST['reason']
        time = request.POST['time']
        bank_address = request.POST['bank_address']

        # Save form data to the database
        appointment = Appointment(name=name, email=email, age=age, reason=reason, time=time, bank_address=bank_address)
        appointment.save()

        # Fetch all appointments to display below the form
        appointments = Appointment.objects.all()
        return render(request, 'appointment.html', {'appointments': appointments})

    return render(request, 'appointment.html')

from django.contrib.auth import authenticate, login
from django.shortcuts import render
from .models import BankUser

def create_account(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        # Create a new user account
        user = BankUser(username=username, password=password, email=email)
        user.save()

        # Redirect the user to a success page or other actions
        return render(request, 'account_created.html')

    return render(request, 'create_account.html')

# views.py
from django.contrib.auth import authenticate, login
from django.shortcuts import render

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page or other actions upon successful login
            return render(request, 'login_success.html')
        else:
            # Provide feedback for incorrect login
            return render(request, 'login.html', {'error_message': 'Invalid username or password.'})

    return render(request, 'login.html')
