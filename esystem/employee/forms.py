from employee.models import Employee, Appraisal 
class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Employee  
        fields = "__all__"  

class AppraisalForm(forms.ModelForm):
    class Meta: 
        model = Appraisal
        fields = ['criteria', 'score', ]