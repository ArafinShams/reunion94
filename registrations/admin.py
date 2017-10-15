from django.contrib import admin

# Register your models here.
from .models import RegistrationPersonal, RegistrationAddress, RegistrationPayment

admin.site.register(RegistrationPersonal)
admin.site.register(RegistrationAddress)
admin.site.register(RegistrationPayment)
