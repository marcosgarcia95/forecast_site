from django.contrib import admin
from .models import Program, Sbe_2,QuarterPeriod, LineItem, Forecast, ForecastPeriod
# Register your models here.
admin.site.register(Program)
admin.site.register(Sbe_2)
admin.site.register(QuarterPeriod)
admin.site.register(LineItem)
admin.site.register(Forecast)
admin.site.register(ForecastPeriod)
