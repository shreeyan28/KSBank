from django.contrib import admin
from .models import Appointment

admin.site.register(Appointment)

#for creat_account 
from django.contrib import admin
from .models import BankUser

admin.site.register(BankUser)
