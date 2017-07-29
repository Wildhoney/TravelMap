from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^countries/$', views.country_list),
]