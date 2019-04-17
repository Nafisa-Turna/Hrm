from django.forms import ModelForm,TextInput
from dashboard.models import Department

class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = '__all__'
        widgets ={
            "department_name" : TextInput(attrs={'style':'width:300px;margin-left: 20px;'}),
            "designation_name" : TextInput(attrs={'style':'width:300px;margin-left: 58px;'}),
        }
        