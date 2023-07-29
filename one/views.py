from django.shortcuts import render
from django.http import HttpResponse,HttpRequest,HttpResponseRedirect
from .models import *
from django.template import loader
# Create your views here.
class Norecordsfound(Exception):
    pass
class Negative_val(Exception):
    pass

def display(request):
    dvalues=itemdet.objects.values.order_by("itno")
    dobjects=itemdet.objects.all().order_by("itprice")
    try:
        amt=int(input("Enter the amount"))
        if amt>=0:
            dvalues=dvalues.filter(itprice__ite=amt)
        if len(dvalues)==0:
            raise Norecordsfound("No such records")
        else:
            raise Negative_val("Amount cannot be negative")
    except Exception as e:
        t=loader.get_template("Exception.html")
        c=dict({'dobjects':e})
        print(c)
        return render(request,'Exception.html',c)

    t=loader.get_template("Display.html")
    c=dict({'dvalues':dvalues,'dobjects':dobjects})
    return render(request,'Display.html',c)

def maxprice(request):
    dobjects=itemdet.objects.all().order_by('itprice').first()
    t=loader.get_template("singlerecord.html")
    c=dict({'dobjects':dobjects})
    return render(request, 'singlerecord.html',c)

def input1(request):
    t=loader.get_template("input.html")
    c=dict({'form':item_Form()})
    return render(request,'input.html')

def createitemdet(request):
    if request.method=='POST':
        form=item_Form(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/display/')
