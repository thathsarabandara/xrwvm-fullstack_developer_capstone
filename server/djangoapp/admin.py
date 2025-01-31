from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.

# CarModelInline class
admin.site.register(CarMake)
# CarModelAdmin class
admin.site.register(CarModel)
# CarMakeAdmin class with CarModelInline

# Register models here
