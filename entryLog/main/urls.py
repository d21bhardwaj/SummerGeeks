from django.urls import path
from main import views


urlpatterns = [
    path('', views.home, name='home'),
    path('log/', views.log, name='log'),
    path('guest/', views.all_guest, name='all_guest'),
    path('guest/entry', views.guest_entry, name='guest_entry'),
    path('employee/upload', views.employee_upload, name='employee_data'),
    path('employee/', views.all_employee, name='employee_log'),
    path('employee/availability/<int:employee_id>', views.employee_availablity, name='employee_availablity'),
    path('guest/checkout/<int:guest_id>', views.guest_check_out, name='guest_check_out'),

]
