import os
from django.contrib.gis.utils import LayerMapping
from .models import Hospital, Ambulance, PostOffice, Mosque, Church, FireStation, Kindergarten, PrimarySC, \
    PreparatorySC, HighSC, CityBorder, Roads
from django.contrib.gis.gdal import DataSource

# Auto-generated `LayerMapping` dictionary for hs model
hs_mapping = {
    'name': 'Name',
    'enname': 'EnName',
    'type': 'type',
    'geom': 'MULTIPOINT',
}
# Auto-generated `LayerMapping` dictionary for ambulance model
ambulance_mapping = {
    'name': 'name',
    'carnum': 'carnum',
    'geom': 'MULTIPOINT',

}
# Auto-generated `LayerMapping` dictionary for postoffice model
postoffice_mapping = {
    'name': 'Name',
    'postal_cod': 'postal_Cod',
    'grade': 'Grade',
    'e_name': 'E_Name',
    'geom': 'MULTIPOINT',
}
# Auto-generated `LayerMapping` dictionary for mosque model
mosque_mapping = {
    'name': 'Name',
    'enname': 'ENname',
    'geom': 'MULTIPOINT25D',

}

# Auto-generated `LayerMapping` dictionary for church model
church_mapping = {
    'name': 'Name',
    'enname': 'EnName',
    'geom': 'MULTIPOINT25D',

}

# Auto-generated `LayerMapping` dictionary for FireStation model
firestation_mapping = {
    'name': 'name',
    'enname': 'EnName',
    'geom': 'MULTIPOINT',

}

# Auto-generated `LayerMapping` dictionary for Kindergarten model
kindergarten_mapping = {
    'name': 'Name',
    'classes': 'classes',
    'enname': 'EnName',
    'geom': 'MULTIPOINT25D',

}
# Auto-generated `LayerMapping` dictionary for ElementarySC model
primarysc_mapping = {
    'name': 'Name',
    'enname': 'EnName',
    'classes': 'classes',
    'geom': 'MULTIPOINT25D',

}

# Auto-generated `LayerMapping` dictionary for PreparatorySC model
preparatorysc_mapping = {
    'name': 'Name',
    'classes': 'classes',
    'enname': 'EnName',
    'geom': 'MULTIPOINT25D',
}

# Auto-generated `LayerMapping` dictionary for HighSC model
highsc_mapping = {
    'name': 'Name',
    'classes': 'classes',
    'enname': 'EnName',
    'geom': 'MULTIPOINT25D',

}

cityborder_mapping = {
    'section_a_field': 'Section_A_',
    'section_e_field': 'Section_E_',
    'geom': 'MULTIPOLYGON',
}

roads_mapping = {
    'name': 'name',
    'geom': 'MULTILINESTRING',
}

# kg_shp=DataSource('qinaservices/data')
hs_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'services/hs.shp'))
ambc_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'services/ambc.shp'))
pst2_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'services/pst2.shp'))
msq_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'services/msq.shp'))
chr_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'services/chr.shp'))
fir_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'services/fir.shp'))
kg_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'services/kg.shp'))
sc1_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'services/sc1.shp'))
sc2_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'services/sc2.shp'))
sc3_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'services/sc3.shp'))
border_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'services/border.shp'))
roads_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'services/roads.shp'))


def run_a(verbose=True):
    lm = LayerMapping(Hospital, hs_shp, hs_mapping, encoding='UTF-8')
    lm.save(strict=True, verbose=verbose)
    lm = LayerMapping(Ambulance, ambc_shp, ambulance_mapping, encoding='UTF-8')
    lm.save(strict=True, verbose=verbose)
    lm = LayerMapping(PostOffice, pst2_shp, postoffice_mapping, encoding='UTF-8')
    lm.save(strict=True, verbose=verbose)
    lm = LayerMapping(Mosque, msq_shp, mosque_mapping, encoding='UTF-8')
    lm.save(strict=True, verbose=verbose)
    lm = LayerMapping(Church, chr_shp, church_mapping, encoding='UTF-8')
    lm.save(strict=True, verbose=verbose)
    lm = LayerMapping(FireStation, fir_shp, firestation_mapping, encoding='UTF-8')
    lm.save(strict=True, verbose=verbose)
    lm = LayerMapping(Kindergarten, kg_shp, kindergarten_mapping, encoding='UTF-8')
    lm.save(strict=True, verbose=verbose)
    lm = LayerMapping(PrimarySC, sc1_shp, primarysc_mapping, encoding='UTF-8')
    lm.save(strict=True, verbose=verbose)
    lm = LayerMapping(PreparatorySC, sc2_shp, preparatorysc_mapping, encoding='UTF-8')
    lm.save(strict=True, verbose=verbose)
    lm = LayerMapping(HighSC, sc3_shp, highsc_mapping, encoding='UTF-8')
    lm.save(strict=True, verbose=verbose)
    lm = LayerMapping(CityBorder, border_shp, cityborder_mapping, encoding='UTF-8')
    lm.save(strict=True, verbose=verbose)
    lm = LayerMapping(Roads, roads_shp, roads_mapping, encoding='UTF-8')
    lm.save(strict=True, verbose=verbose)


def run_b(verbose=True):
    lm = LayerMapping(Roads, roads_shp, roads_mapping, encoding='UTF-8')
    lm.save(strict=True, verbose=verbose)
# def run_c(verbose=True):
# def run_d(verbose=True):
