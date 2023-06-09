from django.db import models


# Create your models here.

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    my_class = models.CharField(max_length=50)
    timing = models.CharField(max_length=50)
   
    def __str__(self):
        return f"{self.first_name} {self.last_name}"




