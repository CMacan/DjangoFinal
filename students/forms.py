from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_number', 'last_name', 'email', 'field_of_study']
        labels = {
            'student_number': 'Student Number',
            'fist_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'field_of_study': 'Field of Study'
        }
        widgets = {
            'student_number': forms.NumberInput(attrs={'class':'form-control'}),
            'student_number': forms.TextInput(attrs={'class':'form-control'}),
            'fist_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),  
            'field_of_study': forms.TextInput(attrs={'class':'form-control'})
        }