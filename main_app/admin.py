from django.contrib import admin

from .models import Car, Maintenance, Tires


admin.site.register(Car)
admin.site.register(Maintenance)
admin.site.register(Tires)
