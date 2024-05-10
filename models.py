from django.db import models

# Create your models here.
class sim3(models.Model) :
    title = models.CharField(max_length=100)
    number_of_pages = models.IntegerField()
    publish_date = models.DateField()
    quantity = models.IntegerField()

def _str_(self):
    return self.title




    # /simtri/list