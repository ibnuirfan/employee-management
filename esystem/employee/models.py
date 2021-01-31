from django.db import models
import datetime

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField('First Name', max_length=50, blank=True)
    last_name = models.CharField('Last Name', max_length=50, blank=True)
    gender = models.CharField('Gender', max_length=10, blank=True)
    dob = models.DateField('Date of birth', null=True)
    nationality = models.CharField('Nationality', max_length=50, blank=True)
    email_address = models.CharField('Email Address', max_length=50, blank=True)
    address = models.CharField('Address', max_length=150, blank=True)
    postal_code = models.CharField('Postal Code', max_length=10, blank=True)
    date_joined = models.DateField('Date Joined', null=True)
    is_active = models.BooleanField('Is active', default=True)
    manager = models.ForeignKey('Manager', on_delete=models.CASCADE, default=1)
    department = models.ForeignKey('Department', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = "Employees"

class Appraisal(models.Model):
    appraisal_id = models.AutoField(primary_key=True)
    criteria = models.CharField('Criteria', max_length=255, blank=True)
    year = models.DateField('Year of Appraisal', null=True)
    score = models.IntegerField('Overall Performance', blank=True)
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, default=1)
    manager = models.ForeignKey('Manager', on_delete=models.CASCADE, default=1)
    department = models.ForeignKey('Department', on_delete=models.CASCADE, default=1)

    class Meta:
            verbose_name_plural = "Appraisals"


class Manager(models.Model):
    manager_id = models.AutoField(primary_key=True)
    manager_name = models.CharField('Manager Name', max_length=25, blank=True)
    manager_title = models.CharField('Manager Title', max_length=25, blank=True)
    
    def __str__(self):
        return self.manager_title

    class Meta:
        verbose_name_plural = "Managers"

class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField('Department', max_length=25, blank=True)

    def __str__(self):
        return self.department_name

    class Meta:
        verbose_name_plural = "Department"

    