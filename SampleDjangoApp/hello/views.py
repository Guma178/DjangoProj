from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from hello.models import Db
from hello.models import Rubric
# Create your views here.

def index(request):
    return HttpResponse('<font size=12 color=green>Hello user!</font></br><a href="../hello/catalog">Catalog</a>')

def info(request):
    return HttpResponse('<font size=8 color=blue><h3>Information</h3></br>This site made with Django.</font>')

def catalog(request):
    current_rub = Rubric.objects.all()[0]
    bbs = Db.objects.filter(rubric=current_rub.pk)
    template = loader.get_template("index.html")
    all_rub = Rubric.objects.all()
    context = {'cdb' : bbs, 'rub' : current_rub, 'rubs' : all_rub}
    return HttpResponse(template.render(context, request))

def by_rubric(request, rubric_id):
    bbs = Db.objects.filter(rubric=rubric_id)
    template = loader.get_template("index.html")
    current_rub = Rubric.objects.get(pk=rubric_id)
    all_rub = Rubric.objects.all()
    context = {'cdb' : bbs, 'rub' : current_rub, 'rubs' : all_rub}
    return HttpResponse(template.render(context, request))