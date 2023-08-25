from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Employee,Testimonial
from .forms import FeedbackForm

# Create your views here.
def employee_home(request):
   #return HttpResponse("hello from emp")
   employee = Employee.objects.all()  # create a list of employees
   return render(request, 'emp/home.html',{
      'employee':employee
   })

def add_employee(request):
  if request.method == 'POST':
     #datafetch 
      emp_name = request.POST.get('emp_name')
      emp_id = request.POST.get('emp_id')
      emp_salary = request.POST.get('emp_salary')
      emp_phone = request.POST.get('emp_phone')
      emp_address = request.POST.get('emp_address')
      emp_email = request.POST.get('emp_email')
      emp_dept = request.POST.get('emp_department')
      emp_working = request.POST.get('emp_working')

         #create model object
      e=Employee()
      e.name=emp_name
      e.emp_id=emp_id
      e.salary=emp_salary
      e.phone=emp_phone
      e.address=emp_address
      e.email=emp_email
      e.department=emp_dept
      if emp_working is None:
       e.working=False
      else:
         e.working=True

       #save the object data
      e.save() 
      return redirect('/emp/home/')
         #print("data is coming")
     
  return render(request, 'emp/add_emp.html',{})

def delete_employee(request,emp_id):
   print("Employee id : ",emp_id)
   emp=Employee.objects.get(pk=emp_id)
   emp.delete()
   return redirect('/emp/home/')

def update_employee(request,emp_id):
   print("Employee id : ",emp_id)
   emp=Employee.objects.get(pk=emp_id)
   return render(request, 'emp/update_emp.html',{
      'emp':emp
   })

def do_update_emp(request,emp_id):
    if request.method == 'POST':
     #datafetch 
      emp_name = request.POST.get('emp_name')
      emp_id_temp = request.POST.get('emp_id')
      emp_salary = request.POST.get('emp_salary')
      emp_phone = request.POST.get('emp_phone')
      emp_address = request.POST.get('emp_address')
      emp_email = request.POST.get('emp_email')
      emp_dept = request.POST.get('emp_department')
      emp_working = request.POST.get('emp_working')

      e=Employee.objects.get(pk=emp_id)
      e.name=emp_name
      e.emp_id=emp_id_temp
      e.salary=emp_salary
      e.phone=emp_phone
      e.address=emp_address
      e.email=emp_email
      e.department=emp_dept
      if emp_working is None:
       e.working=False
      else:
         e.working=True

       #save the object data
      e.save() 
      return redirect('/emp/home/')
    
def feedback(request):
   if request.method == 'POST':
      pass
   else:
      form= FeedbackForm()

   return render(request, 'emp/feedback.html',{'form':form})

def testimonials(request):
   testi= Testimonial.objects.all()
   return render(request, 'emp/testimonials.html',{
      'testi':testi
   })

      