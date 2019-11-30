from django.contrib import admin

# Register your models here.
from .models import *

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'name','designation','phone_no','email','department','room_no','in_office')

class EntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'visitor_title', 'visitor_name','visitor_phone_no','visitor_email','host_name','in_time','out_time','left_office','verification')

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Entry, EntryAdmin)