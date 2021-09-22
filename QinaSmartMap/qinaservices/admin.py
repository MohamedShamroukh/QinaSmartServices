from django.contrib import admin
from .models import Hospital, Ambulance, PostOffice, Mosque, Church, FireStation, Kindergarten, PrimarySC, PreparatorySC, HighSC, CityBorder, Roads
from leaflet.admin import LeafletGeoAdmin


# Register your models here.

class HsAdmin(LeafletGeoAdmin):
    list_display = ('name', 'enname', 'type',)


class AmbcAdmin(LeafletGeoAdmin):
    list_display = ('name', 'carnum',)


class Pst2Admin(LeafletGeoAdmin):
    list_display = ('name', 'e_name', 'grade','postal_cod',)


class MsqAdmin(LeafletGeoAdmin):
    list_display = ('name','enname',)


class ChrAdmin(LeafletGeoAdmin):
    list_display = ('name', 'enname',)


class FirAdmin(LeafletGeoAdmin):
    list_display = ('name','enname',)


class KgAdmin(LeafletGeoAdmin):
    list_display = ('name','enname', 'classes',)


class Sc1Admin(LeafletGeoAdmin):
    list_display = ('name','enname', 'classes',)


class Sc2Admin(LeafletGeoAdmin):
    list_display = ('name','enname', 'classes',)


class Sc3Admin(LeafletGeoAdmin):
    list_display = ('name','enname', 'classes',)


class BorderAdmin(LeafletGeoAdmin):
    list_display = ('section_a_field','section_e_field', )


class RoadAdmin(LeafletGeoAdmin):
    list_display = ('name',)


admin.site.register(Hospital, HsAdmin)
admin.site.register(Ambulance, AmbcAdmin)
admin.site.register(PostOffice, Pst2Admin)
admin.site.register(Mosque, MsqAdmin)
admin.site.register(Church, ChrAdmin)
admin.site.register(FireStation, FirAdmin)
admin.site.register(Kindergarten, KgAdmin)
admin.site.register(PrimarySC, Sc1Admin)
admin.site.register(PreparatorySC, Sc2Admin)
admin.site.register(HighSC, Sc3Admin)
admin.site.register(CityBorder, BorderAdmin)
admin.site.register(Roads, RoadAdmin)



