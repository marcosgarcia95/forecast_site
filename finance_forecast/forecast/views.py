from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
# from django.contrib.auth import login_required
# from django.contrib.auth import LoginRequiredMixin
from .models import Program, Forecast, download_csv
from .forms import ForecastForm
from django.urls import reverse_lazy
# Create your views here.

class IndexView(TemplateView):
    #template_name will return the html template of whatever file you point it to.
    template_name = 'index.html' #we set up the TEMPLATE_DIR in settings.py, so it knows to look in that folder.

class ProgramListView(ListView):
    model = Program #connecting the view to the Post model

    def get_queryset(self): #this is to filter for data
        #get_queryset = python version of getting query.
        #filter based on these conditions: Grab publish date.
        #__lte  = less than or equal to. The __ means you are setting up a condition.
        #the '-' in order by makes it to where you are order descending.
        #More info in the documentation: https://docs.djangoproject.com/en/4.0/topics/db/queries/#field-lookups
        return Program.objects.filter(forecast_this_cycle=True).order_by('-program')
class ProgramDetailView(DetailView):
    model=Program

class CreateForecastView(CreateView):
    # login_url = '/login/'
    redirect_field_name = 'forecast/program_detail.html'

    form_class = ForecastForm

    model = Forecast

class ForecastUpdateView(UpdateView):
    redirect_field_name = 'forecast/program_detail.html'
    form_class = ForecastForm
    model = Forecast

class ForecastListView(ListView):
    model = Forecast
    def get_queryset(self):
        program = Forecast.objects.distinct()
        return program

class ForecastDetailView(DetailView):
    model = Forecast

def broken_page(request):
    return render(request, 'broken_link.html')

def export_csv(request):
  # Create the HttpResponse object with the appropriate CSV header.
  data = download_csv(request, Forecast.objects.all())
  response = HttpResponse(data, content_type='text/csv')
  return response
