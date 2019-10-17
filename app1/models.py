from django.db import models
from django.forms import EmailField
from django.core.validators import validate_email

# Create your models here.
class submit_form_ml(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.CharField(max_length=100)
    message = models.CharField(max_length=800)

    def __str__(self):
        return self.first_name

