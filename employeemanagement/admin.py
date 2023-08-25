from django.contrib import admin
from .models import *



# Register your models here.

class EmpAdmin(admin.ModelAdmin):
    list_display = ['name', 'emp_id', 'phone', 'address', 'email', 'department', 'working', 'salary']
    search_fields = ['name', 'emp_id']
    list_editable = ['phone', 'address', 'email', 'department', 'working', 'salary']
    list_filter = ['department', 'working','salary']
    
admin.site.register(Employee, EmpAdmin)
admin.site.register(Testimonial)