from django.contrib import admin

# Register your models here.
from apps.banks.models import Bank, Branch

admin.site.register((Bank, Branch), )
