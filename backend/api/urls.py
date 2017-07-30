from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^countries/$', views.CountryList.as_view()),
    url(r'^user/(?P<username>[a-z0-9]+)$', views.UserProfile.as_view())
]
