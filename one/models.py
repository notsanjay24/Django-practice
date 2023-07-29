from django.db import models
from django import forms
# Create your models here.
class itemdet(models.Model):
    itname=models.CharField(max_length=25)
    itno=models.IntegerField()
    itprice=models.IntegerField()
    itqty=models.IntegerField()

class itform(forms.ModelForm):
    class Meta:
        model=itemdet
        exclude=()
