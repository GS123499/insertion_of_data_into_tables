from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.
def insert_topic(request):
    tn=input('enter topic name')
    T=Topic.objects.get_or_create(topic_name=tn)[0]
    T.save()
    return HttpResponse('the topic data is succesfully inserted')


def insert_webpage(request):
    tn=input('enter Topic name')
    name=input('enter a name')
    url=input('enter url')
    T=Topic.objects.get_or_create(topic_name=tn)[0]
    T.save()
    W=Webpage.objects.get_or_create(topic_name=T,name=name,url=url)[0]
    W.save()
    return HttpResponse('webpage data is succesfully uploaded')
    


def insert_AccessRecords(request):
    tn=input('enter a topic name')
    name=input('enter a name')
    url=input('enter url')
    date=input('enter a date')
    T=Topic.objects.get_or_create(topic_name=tn)[0]
    T.save()
    W=Webpage.objects.get_or_create(topic_name=T,name=name,url=url)[0]
    W.save()
    AR=Access_Records.objects.get_or_create(name=W,date=date)[0]
    AR.save()
    return HttpResponse('webpage data is succesfully uploaded')
    
