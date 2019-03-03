from django.shortcuts import render
from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = f"<html><body>It is now {now}.<br/><h1>Engoloss <3</h1></body></html>"
    return HttpResponse(html)
