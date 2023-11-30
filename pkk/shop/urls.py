from django.urls import path
from . import views

app_news = 'shop'

urlpatterns = [
    path('' , views.index, name='index'),
]
