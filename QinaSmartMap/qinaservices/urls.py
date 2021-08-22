from django.conf.urls import url
from qinaservices import views

app_name = 'qinaservices'

urlpatterns = [
    url(r'^map/$', views.services_map, name='map'),

]