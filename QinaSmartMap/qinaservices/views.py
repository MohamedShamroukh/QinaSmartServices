from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template import RequestContext
from django.views.generic import View
from django.core.serializers import serialize
from .models import Hospital, Ambulance, PostOffice, Mosque, Church, FireStation, Kindergarten, PrimarySC, \
    PreparatorySC, HighSC
from django.template.context import Context


# Create your views here.

def hospital_data(request):
    hospital = serialize('geojson', Hospital.objects.all())
    return HttpResponse(hospital, content_type='json')


def ambulance_data(request):
    ambulance = serialize('geojson', Ambulance.objects.all())
    return HttpResponse(ambulance, content_type='json')


def post_data(request):
    post = serialize('geojson', PostOffice.objects.all())
    return HttpResponse(post, content_type='json')


def fire_data(request):
    fire = serialize('geojson', FireStation.objects.all())
    return HttpResponse(fire, content_type='json')


def mosque_data(request):
    mosque = serialize('geojson', Mosque.objects.all())
    return HttpResponse(mosque, content_type='json')


def church_data(request):
    church = serialize('geojson', Church.objects.all())
    return HttpResponse(church, content_type='json')


def kindergarten_data(request):
    kindergarten = serialize('geojson', Kindergarten.objects.all())
    return HttpResponse(kindergarten, content_type='json')


def primary_data(request):
    primary = serialize('geojson', PrimarySC.objects.all())
    return HttpResponse(primary, content_type='json')


def prep_data(request):
    prep = serialize('geojson', PreparatorySC.objects.all())
    return HttpResponse(prep, content_type='json')


def high_data(request):
    high = serialize('geojson', HighSC.objects.all())
    return HttpResponse(high, content_type='json')


def home(request):
    """ Renders home page """
    return render(
        request,
        'index.html',
        {
            'title': 'Qina Smart Map ',
        }
    )


def services_map(request):
    """ Renders map page """
    return render(
        request,
        'Map.html',
        {
            'title': ' Qina services Map',
        }
    )


def education_map(request):
    """ Renders map page """
    return render(
        request,
        'education.html',
        {
            'title': ' Qina services Map',
        }
    )


def health_map(request):
    """ Renders map page """
    return render(
        request,
        'health.html',
        {
            'title': ' Qina services Map',
        }
    )


def religious_map(request):
    """ Renders map page """
    return render(
        request,
        'religious.html',
        {
            'title': ' Qina services Map',
        }
    )


def other_map(request):
    """ Renders map page """
    return render(
        request,
        'other.html',
        {
            'title': ' Qina services Map',
        }
    )


def admin(request):
    """ Renders home page """
    return render(
        request,
        admin.site.urls,
        {
            'title': 'Qina Smart Map',
        }
    )
