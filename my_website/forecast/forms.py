#this forms.py file was not created automatically, it needs to be manually created.
from django import forms
from .models import Program, QuarterPeriod, LineItem, Sbe_2, Forecast,ForecastPeriod #.model means to look inside the same directory



class ForecastForm(forms.ModelForm): #you frequently call forms.ModelForm to make the form.
    class Meta():
        model = Forecast
        fields = ('program','line_item','quarter_period','amt','comment')

    def __init__(self, *args, **kwargs):
        super(ForecastForm, self).__init__(*args, **kwargs)
        self.fields['quarter_period'].queryset = QuarterPeriod.objects.filter(enter_inputs=True)
        self.fields['program'].queryset = Program.objects.filter(forecast_this_cycle=True)


class ProgramForm(forms.ModelForm): #you frequently call forms.ModelForm to make the form.
    class Meta():
        model = Program
        fields = ('program','program_manager','forecast_this_cycle','sbe_2')


