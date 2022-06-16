from django.urls import path

from . import views

app_name='word_app'

urlpatterns = [
    path('', views.index, name="index")
]