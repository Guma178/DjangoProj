from django.urls import path
from hello.views import index
from hello.views import info
from hello.views import catalog

urlpatterns = [
    path('', index),
    path('index/', index),
    path('info/', info),
    path('catalog/', catalog)
]