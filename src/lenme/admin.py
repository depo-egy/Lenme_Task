from django.contrib import admin
from .models import Investor , Borrower , Loan
# Register your models here.

admin.site.register(Investor)
admin.site.register(Borrower)
admin.site.register(Loan)
