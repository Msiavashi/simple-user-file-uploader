
from django.conf.urls import url
from .views import *

app_name = 'api'

urlpatterns = [
    url(r'^user/template/$', TemplateAPI.as_view()),
    url(r'^user/template/(?P<tid>\d+)/$', TemplateDelete.as_view()),
]