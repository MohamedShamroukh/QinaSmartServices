from django.contrib import admin
from .models import Hospital, Ambulance, PostOffice, Mosque, Church, FireStation, Kindergarten, PrimarySC, PreparatorySC, HighSC
from leaflet.admin import LeafletGeoAdmin


# Register your models here.

class HsAdmin(LeafletGeoAdmin):
    list_display = ('name',)


class AmbcAdmin(LeafletGeoAdmin):
    list_display = ('name',)


class Pst2Admin(LeafletGeoAdmin):
    list_display = ('name',)


class MsqAdmin(LeafletGeoAdmin):
    list_display = ('name',)


class ChrAdmin(LeafletGeoAdmin):
    list_display = ('name',)


class FirAdmin(LeafletGeoAdmin):
    list_display = ('name',)


class KgAdmin(LeafletGeoAdmin):
    list_display = ('name',)


class Sc1Admin(LeafletGeoAdmin):
    list_display = ('name',)


class Sc2Admin(LeafletGeoAdmin):
    list_display = ('name',)


class Sc3Admin(LeafletGeoAdmin):
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




