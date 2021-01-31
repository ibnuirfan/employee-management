from rest_framework import viewsets, permissions
from .models import Employee, Appraisal, Manager, Department
from .serializers import EmployeeSerializer, ManagerSerializer, AppraisalSerializer, DepartmentSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:    
        form = UserCreationForm()
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, "Account was created for " + user)
                return redirect('login')

    context = {'form':form}
    return render(request, 'register.html',context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')    
    else:  
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.info(request, 'username or password is incorrect')           
        context = {}
        return render(request, 'login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url = 'login')
def emp(request):
     if request.method == 'GET':
        current_user_id = request.user.id
        if request.user.is_superuser:
            return redirect('http://127.0.0.1:8000/employee')
        else:
            
            employee = Employee.objects.get(user_id = current_user_id)
            employee_id = employee.EmpId       
            if Manager.objects.filter(emp_id = employee_id):
                manager_id = Manager.objects.filter(emp_id = employee_id).values('mgr_id')[0]['mgr_id']
                selected_employees = Employee.objects.filter(manager_id = manager_id)
                context = {'employees':selected_employees}
                return render(request,'show.html',context) 
            else:    
                appraisal = Appraisal.objects.get(emp_id = employee_id)
                context = {'form':employee, 'appraisal':appraisal}
                return render(request,'index.html',context) 
    
@login_required(login_url = 'login')
def edit(request, emp_id): 
        emp_id = int(emp_id)
        employee = Employee.objects.get(EmpId=emp_id)
        appraisal = Appraisal.objects.get(emp_id = emp_id)
        context = {'form':employee, 'appraisal':appraisal}
        return render(request,'edit.html', context)  


@login_required(login_url = 'login')
def update(request, emp_id):
    if request.method == 'POST':
        emp_id = int(emp_id)  
        appraisal = Appraisal.objects.get(emp_id = emp_id)  
        form = AppraisalForm(request.POST, instance = appraisal)  
        if form.is_valid():  
            form.save() 
        return redirect('http://127.0.0.1:8000/')

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (permissions.IsAdminUser,)
    
class AppraisalViewSet(viewsets.ModelViewSet):
    queryset = Appraisal.objects.all()
    serializer_class = AppraisalSerializer
    permission_classes = (permissions.IsAdminUser,)

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = (permissions.IsAdminUser,)
