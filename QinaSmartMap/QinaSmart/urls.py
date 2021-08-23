"""QinaSmart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from qinaservices import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    url(r'^$', views.home, name='home'),
    path('admin/', admin.site.urls, name='admin'),
    url(r'^map/$', views.services_map, name='map'),
    url(r'^education/$', views.education_map, name='education'),
    url(r'^education/$', views.education_map, name='education'),
    url(r'^helth/$', views.health_map, name='health'),
    url(r'^religious/$', views.religious_map, name='religious'),
    url(r'^other/$', views.other_map, name='other'),
    url(r'^admin/$', views.admin, name='admin'),
    url(r'^hospital_data/$', views.hospital_data, name='hospital_data'),
    url(r'^ambulance_data/$', views.ambulance_data, name='ambulance_data'),
    url(r'^post_data/$', views.post_data, name='post_data'),
    url(r'^fire_data/$', views.fire_data, name='fire_data'),
    url(r'^mosque_data/$', views.mosque_data, name='mosque_data'),
    url(r'^church_data/$', views.church_data, name='church_data'),
    url(r'^kindergarten_data/$', views.kindergarten_data, name='kindergarten_data'),
    url(r'^primary_data/$', views.primary_data, name='primary_data'),
    url(r'^prep_data/$', views.prep_data, name='prep_data'),
    url(r'^high_data/$', views.high_data, name='high_data'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
