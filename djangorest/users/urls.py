from django.conf.urls import url
from .views import *

app_name = 'users'

urlpatterns = [
    url(r'^create/$', CreateUserAPIView.as_view()),
    url(r'^login/$', authenticate_user),
]