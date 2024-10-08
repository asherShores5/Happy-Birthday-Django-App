from django.db import models

class Birthday(models.Model):
    birthday_date = models.DateField()
    class Meta:
        app_label = 'app1'