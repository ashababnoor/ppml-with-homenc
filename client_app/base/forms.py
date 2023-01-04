from django import forms
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class DiabetesForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('base:home')
        self.helper.form_method = 'GET'
        self.helper.add_input(Submit('submit', 'Submit'))

    high_bp = forms.IntegerField(label="Do you have high Blood Pressure?", required=True, min_value=0, max_value=1)
    high_chol = forms.IntegerField(label="Do you have high Cholesterol?", required=True, min_value=0, max_value=1)
    chol_check = forms.IntegerField(label="Did you check your Cholesterol in last 5 years?", required=True, min_value=0, max_value=1)
    weight = forms.FloatField(label="How much do you weigh in kilograms?", required=True,)
    height = forms.FloatField(label="How tall are you in centimeters?", required=True,)
    smoker = forms.IntegerField(label="Have you smoked at least 100 cigarettes in your entire life?", required=True, min_value=0, max_value=1)
    stroke = forms.IntegerField(label="Have you ever had a stroke before?", required=True, min_value=0, max_value=1)
    heart = forms.IntegerField(label="Have you ever had coronary heart disease (CHD) or myocardial infarction (MI)?", required=True, min_value=0, max_value=1)
    pa = forms.IntegerField(label="Have you done any physical activity in past 30 days excluding your job?", required=True, min_value=0, max_value=1)
    fruits = forms.IntegerField(label="Do you consume fruits once or more times per day?", required=True, min_value=0, max_value=1)
    



