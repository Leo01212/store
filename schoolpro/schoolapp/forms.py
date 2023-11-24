# forms.py
from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(label='Name')
    dob = forms.DateField(label='DOB')
    age = forms.IntegerField(label='Age')
    gender = forms.ChoiceField(label='Gender', choices=[('male', 'Male'), ('female', 'Female')])
    phone_number = forms.CharField(label='Phone Number')
    email = forms.EmailField(label='Email')
    address = forms.CharField(label='Address')
    department = forms.ChoiceField(label='Department', choices=[('computer_science', 'Computer Science'), ('biology', 'Biology'), ('commerce', 'Commerce'), ('history', 'History'), ('agriculture', 'Agriculture')])
    course = forms.ChoiceField(label='Course',choices=[('bsc_computer_science','Bsc Computer Science'),('bsc_computer_application', 'Bsc Computer Application'),('bsc_botany', 'Bsc Botany'), ('bsc_zoology', 'Bsc Zoology'),('bba', 'BBA'), ('bcom', 'BCom'),('ba_history', 'BA History'), ('ba_politics', 'BA Politics'),('bsc_agriculture', 'Bsc Agriculture'), ('msc_agriculture', 'Msc Agriculture')],widget=forms.Select(attrs={'style': 'width: 200px;'}))
    purpose = forms.ChoiceField(label='Purpose', choices=[('enquiry', 'Enquiry'), ('place_order', 'Place Order'), ('return', 'Return')])
    materials_provide = forms.MultipleChoiceField(label='Materials Provide', choices=[('notebook', 'Notebook'), ('pen', 'Pen'), ('exam_papers', 'Exam Papers')], widget=forms.CheckboxSelectMultiple)


