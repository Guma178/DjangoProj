from django.urls import path
from hello.views import index
from hello.views import info
from hello.views import catalog, by_rubric

urlpatterns = [
    path('', index),
    path('index/', index),
    path('info/', info),
    path('catalog/', catalog),
    path('catalog/<int:rubric_id>/', by_rubric)
]