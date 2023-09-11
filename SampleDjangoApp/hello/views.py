from django.shortcuts import render
from django.http import HttpResponse
from hello.models import Db
# Create your views here.

def index(request):
    return HttpResponse('<font size=12 color=green>Hello user!</font></br><a href="../hello/catalog">Catalog</a>')

def info(request):
    return HttpResponse('<font size=8 color=blue><h3>Information</h3></br>This site made with Django.</font>')

def catalog(request):
    html = '<font color=gray><h3>Catalog</h3></font>'
    html += '<table><tr><td>Name</td><td>Description</td><td>Price</td></tr>'
    for b in  Db.objects.order_by('-price'):
    #for b in Db.objects.all():
        html += f"<tr><td>{b.title}</td><td>{b.content}</td><td>{b.price}</td></tr>"
    html += '</table>'
    return HttpResponse(html)