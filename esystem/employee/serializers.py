from rest_framework import serializers
from. models import Employee, Appraisal, Manager, Department

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('employee_id', 'department_id', 'first_name', 'last_name', 'username', 'password', 'gender', 'dob', 'nationality', 'email_address', 'address', 'postal_code', 'date_joined', 'is_active')

class AppraisalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appraisal
        fields = ('appraisal_id', 'employee_id', 'manager_id', 'department_id', 'criteria', 'year', 'score')

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ('manager_id', 'manager_name', 'manager_title')

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('department_id', 'department_name')