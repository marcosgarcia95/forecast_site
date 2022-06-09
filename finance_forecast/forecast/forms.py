#this forms.py file was not created automatically, it needs to be manually created.
from django import forms
from .models import Program, QuarterPeriod, LineItem, Sbe_2, Forecast #.model means to look inside the same directory


class ForecastForm(forms.ModelForm): #you frequently call forms.ModelForm to make the form.
    class Meta():
        model = Forecast
        fields = ('program','line_item','quarter_period','amt','comment')
