from django.contrib import admin
from employee.models import Employee, Appraisal, Manager, Department

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'department_id', 'first_name', 'last_name', 'gender', 'dob', 'nationality', 'email_address', 'address', 'postal_code', 'date_joined', 'is_active')

@admin.register(Appraisal)
class AppraisalAdmin(admin.ModelAdmin):
    list_display = ('appraisal_id', 'employee_id', 'manager_id', 'department_id', 'criteria', 'year', 'score')

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_id', 'department_name')

@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('manager_id', 'manager_name', 'manager_title')

