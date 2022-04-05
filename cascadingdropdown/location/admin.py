from django.contrib import admin

# Register your models here.
from .models import State, District, Village

admin.site.register(State)
admin.site.register(District)
admin.site.register(Village)