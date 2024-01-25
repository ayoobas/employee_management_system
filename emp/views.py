from django.shortcuts import render,  redirect 
from .models import Employee
from django.http import HttpResponse
from . forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required





# Create your views here.
@login_required(login_url = "login")
def allemployees(request):
    emp = Employee.objects.all()

    return render(request, "emp/allemployees.html", {"allemployees":emp})

def singleemployee(request, empid):
    return render(request, "emp/singleemployee.html")


def addemployee(request):
    if request.method == "POST":
       employeeid = request.POST.get('employeeid')
       name = request.POST.get('name')
       email = request.POST.get('email')
       address = request.POST.get('address')
       phone = request.POST.get('phone')
      
           #Create an object of the Employee model
       e = Employee()
       e.employeeid = employeeid
       e.name = name
       e.email = email
       e.address = address
       e.phone = phone
       e.save()
       return redirect("/allemployees")
    
    return render(request, "emp/addemployee.html")

def deleteemployee(request, empid):
   e = Employee.objects.get(pk = empid)
   e.delete()
   return redirect("allemployees") #This is calling the function


def updateemployee(request, empid):
    e = Employee.objects.get(pk = empid)
    #return redirect("allemployees")
    return render(request, "emp/updateemployee.html", {"singleemp": e})

def doupdateemployee(request, empid):
    emp_id = request.POST.get('employeeid')
    update_name = request.POST.get('name')
    update_email = request.POST.get('email')
    update_address = request.POST.get('address')
    update_phone   = request.POST.get('phone')

    emp = Employee.objects.get(pk = empid)
    emp.employeeid  = emp_id 
    emp.name  = update_name 
    emp.email  =  update_email
    emp.address  = update_address
    emp.phone = update_phone
    emp.save()
    return redirect("allemployees")

def register(request):
    form = CreateUserForm() #Create an object and assign it to form
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("login") #login is from the urls.py 
    context = {'registerform':form}

    return render(request, 'emp/register.html', context = context ) #Helps to pass the registerform into the register.html

def my_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data = request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username = username, password = password)
            if user is not None:
                auth.login(request, user)
                return redirect("allemployees")
    context = {'loginform': form} #pass the login form into login.html through context

    return render(request, 'emp/login.html', context=context)



def homepage(request):
    return render(request, 'emp/allemployees.html')

def user_logout(request):
    auth.logout(request)
    return redirect("login")






    

