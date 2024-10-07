from django import forms

class DataForm(forms.Form):
    c = [
    ['Python', 'Py'],
    ['Java', 'Java'],
    ['MERN', 'MERN']
]
    g = [
    ['Male', 'Male'],
    ['Female', 'Female'],
    ['Others', 'Others']
]
    name = forms.CharField(max_length=200,required=False)
    pno = forms.CharField(max_length=200,required=False)
    email = forms.CharField(max_length=200,required=False)
    add = forms.CharField(max_length=200,required=False)
    username = forms.CharField(max_length=200,required=False)
    password = forms.CharField(max_length=200,required=False)
    courses = forms.ChoiceField(choices = c,required=True)
    gender = forms.ChoiceField(choices=g,required=True)