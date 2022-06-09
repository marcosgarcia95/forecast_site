from django.db import models
from django.utils import timezone
from django.urls import reverse, reverse_lazy #after someone creates a post,
from django.http import HttpResponse
import csv
# Create your models here. Create models after setting up your settings.py file.


class Program(models.Model):
    #author: directly link an author to an authorization user.
    program = models.CharField(max_length=100)
    program_manager = models.CharField(max_length = 100)
    forecast_this_cycle = models.BooleanField(default=True)
    sbe_2 = models.ForeignKey('Sbe_2', on_delete=models.CASCADE)
    # text_field = models.TextField()
    # #created_date: setting it to the timezone time that the post is created
    # created_date = models.DateTimeField(default = timezone.now())
    # #pub_date: We leave this blank in case we want to post later
    # pub_date = models.DateTimeField(blank=True, null=True)


    def remove_from_forecast(self):
        """Remove from forecast if you are not needing to forecast"""
        self.forecast_this_cycle = False
        self.save()


    def get_absolute_url(self):
        """This method needs to be called get_absolute_url to know where to go after the program is made.
        reverse = go back to this url"""
        return reverse('index')#,kwargs={'pk':self.pk}) #post_detail is the name of the view/url
        #kwargs is a dictionary where we pass the primary key equal to this post's pk. Pk is created automatically
        #if it's not specified

    def __str__(self):
        return self.program


# class Comment(models.Model):
#     #post: the foreign key comes from the Post class above. blog = current app.
#     #related_name = 'comments'. The reason we do this is because we connect each comment to a post.
#     post = models.ForeignKey('blog.Post', related_name = 'comments', on_delete = models.CASCADE)
#     author = models.CharField(max_length=200)
#     text = models.TextField()
#     created_date = models.DateTimeField(default = timezone.now())
#     approved_comment = models.BooleanField(default = False) #all comments are not approved until the admin approves
#
#     def approve(self):
#         """We have this method to approve the comment"""
#         self.approved_comment = True
#         self.save()
#
#     def get_absolute_url(self):
#         """This method will take you back to the post_list view after approving your comment."""
#         return reverse('post_list')
#
#
#     def __str__(self):
#         return self.text

class Sbe_2(models.Model):
    sbe_2 = models.CharField(max_length=15, null=True)
    forecast_this_cycle = models.BooleanField(default=True)
    def __str__(self):
        return self.sbe_2

class QuarterPeriod(models.Model):
    quarter_period = models.CharField(max_length=8, null=True)
    forecast_this_cycle = models.BooleanField(default=True)
    def __str__(self):
        return self.quarter_period

class LineItem(models.Model):
    line_item = models.CharField(max_length=20)
    def __str__(self):
        return self.line_item

class Forecast(models.Model):
    quarter_period = models.ForeignKey('QuarterPeriod', on_delete=models.CASCADE)
    program = models.ForeignKey('Program', on_delete = models.CASCADE)
    line_item = models.ForeignKey('LineItem', on_delete=models.CASCADE)
    amt = models.FloatField()
    comment = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.program) + " " + str(self.quarter_period) +" "+ str(self.line_item) + " " + str(self.amt)

    def get_absolute_url(self):
        """This method needs to be called get_absolute_url to know where to go after the post is made.
        reverse = go back to this url"""
        return reverse('program_list')#,kwargs={'pk':self.pk}) #post_detail is the name of the view/url
        #kwargs is a dictionary where we pass the primary key equal to this post's pk. Pk is created automatically
        #if it's not specified


#taken from stack overflow: https://stackoverflow.com/questions/18685223/how-to-export-django-model-data-into-csv-file
def download_csv(request, queryset):
  if not request.user.is_staff:
    raise PermissionDenied

  model = queryset.model
  model_fields = model._meta.fields + model._meta.many_to_many
  field_names = [field.name for field in model_fields]

  response = HttpResponse(content_type='text/csv')
  response['Content-Disposition'] = 'attachment; filename="export.csv"'

  # the csv writer
  writer = csv.writer(response, delimiter=";")
  # Write a first row with header information
  writer.writerow(field_names)
  # Write data rows
  for row in queryset:
      values = []
      for field in field_names:
          value = getattr(row, field)
          if callable(value):
              try:
                  value = value() or ''
              except:
                  value = 'Error retrieving value'
          if value is None:
              value = ''
          values.append(value)
      writer.writerow(values)
  return response
