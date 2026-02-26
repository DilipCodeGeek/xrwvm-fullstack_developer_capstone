from django.contrib import admin
from .models import CarMake, CarModel


# CarModel Inline (so models appear inside make)
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1


# CarMake Admin (attach inline)
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]


# CarModel Admin
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'car_type', 'year', 'dealer_id')


# Register models
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)