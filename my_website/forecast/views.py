from dataclasses import fields
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
# from django.contrib.auth import login_required
# from django.contrib.auth import LoginRequiredMixin
from .models import Program, Forecast, download_csv, QuarterPeriod
from .forms import ForecastForm, ProgramForm
from django.urls import reverse_lazy
from django.forms import formset_factory
import django_filters
from django_filters.views import FilterView
# Create your views here.

class IndexView(TemplateView):
    #template_name will return the html template of whatever file you point it to.
    template_name = 'index.html' #we set up the TEMPLATE_DIR in settings.py, so it knows to look in that folder.

class ProgramListView(ListView):
    model = Program #connecting the view to the Post model

    # def get_queryset(self): #this is to filter for data
    #     #get_queryset = python version of getting query.
    #     #filter based on these conditions: Grab publish date.
    #     #__lte  = less than or equal to. The __ means you are setting up a condition.
    #     #the '-' in order by makes it to where you are order descending.
    #     #More info in the documentation: https://docs.djangoproject.com/en/4.0/topics/db/queries/#field-lookups
    #     return Program.objects.filter(forecast_this_cycle=True).order_by('-program')

class ProgramCreateView(CreateView):
    redirect_field_name = 'forecast/forecast_list.html'
    model = Program
    # program_formset = formset_factory(model, fields=('program','program_manager','forecast_this_cycle','sbe_2','internal_ord_list'))
    form_class = ProgramForm

class ProgramDetailView(DetailView):
    model=Program

class ProgramUpdateView(UpdateView):

    form_class = ProgramForm
    model = Program
    redirect_field_name = 'forecast/program_list.html'
    success_url =  reverse_lazy('program_list')

class CreateForecastView(CreateView):
    # login_url = '/login/'
    redirect_field_name = 'forecast/forecast_list.html'

    form_class = ForecastForm
    
    model = Forecast
    def get_form_kwargs(self):
        kwargs = super(CreateForecastView, self).get_form_kwargs()
        return kwargs


class ForecastUpdateView(UpdateView):
    redirect_field_name = 'forecast/forecast_list.html'
    form_class = ForecastForm
    model = Forecast

class ForecastListView(ListView):
    model = Forecast
    show = True

    def get_queryset(self): #this is to filter for data
        model2 = QuarterPeriod
        #get_queryset = python version of getting query.
        #filter based on these conditions: 
       
        #the '-' in order by makes it to where you are order descending.
        #More info in the documentation: https://docs.djangoproject.com/en/4.0/topics/db/queries/#field-lookups
        show = True
        return Forecast.objects.filter(quarter_period__forecast_period__forecast_this_cycle =show).order_by('-program')
    #     #Filter for objects based on another model:
        #https://stackoverflow.com/questions/64277776/filtering-one-model-based-on-another-models-field
    #     #https://stackoverflow.com/questions/66426594/filtering-objects-based-on-another-model

class ForecastDetailView(DetailView):
    model = Forecast

class ForecastDeleteView(DeleteView):
    model = Forecast
    form_class = ForecastForm
    redirect_field_name = 'forecast/forecast_list.html'
    success_url= reverse_lazy('forecast_list')    

def broken_page(request):
    return render(request, 'broken_link.html')

def export_csv(request):
  # Create the HttpResponse object with the appropriate CSV header.
  data = download_csv(request, Forecast.objects.all())
  response = HttpResponse(data, content_type='text/csv')
  return response


class ForecastFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Forecast
        fields = ['program', 'line_item','quarter_period',]
        

class ForecasttList(FilterView):
    model = Forecast
    context_object_name = 'forecasts'
    filterset_class = ForecastFilter
    