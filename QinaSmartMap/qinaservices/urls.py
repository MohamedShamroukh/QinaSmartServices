from django.conf.urls import url
from qinaservices import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'qinaservices'

urlpatterns = [
    url(r'^map/$', views.services_map, name='map'),

]