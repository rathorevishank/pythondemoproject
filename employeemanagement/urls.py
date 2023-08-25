from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
  path('home/',employee_home),
  path('add_emp/',add_employee),
  path('update-emp/<int:emp_id>/',update_employee),
  path('delete-emp/<int:emp_id>/',delete_employee),
  path('do-update-emp/<int:emp_id>/',do_update_emp),
  path('feedback/',feedback),
  path('testimonials/',testimonials)
  

]


