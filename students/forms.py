from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_number', 'first_name', 'last_name', 'email', 'field_of_study', 'profile_picture']
        labels = {
            'student_number': 'Student Number',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'field_of_study': 'Field of Study',
            'profile_picture': 'Profile Picture'
        }
        widgets = {
            'student_number': forms.NumberInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),  
            'field_of_study': forms.TextInput(attrs={'class':'form-control'}),
            'profile_picture': forms.FileInput(attrs={'class':'form-control-file'}),
        }
    
    def clean_student_number(self):
        student_number = self.cleaned_data.get('student_number')
        if not str(student_number).isdigit():
            raise forms.ValidationError("Please enter a valid student number.")
        return student_number