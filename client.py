import json, requests
from inspect import getmembers
from base import DbManager
import dck
import swapi

def get_json_dict(url):
    print(url)
    resp = requests.get(url)
    if (resp.status_code != 200):
        print(resp)
        return None
    return json.loads(resp.text)

class_attrs = {}

def persist(obj_class, obj_dict, key_class, key_name):
    attrs = {}
    if (obj_class not in class_attrs):
        obj = obj_class()
        for memb in getmembers(obj):
            key = memb[0]
            if (not key.startswith('_') and key != 'metadata' and not key.endswith('_at')):
                attrs[key] = 1
        class_attrs[obj_class] = attrs
    else:
        attrs = class_attrs[obj_class]
    results = db.open().query(obj_class).filter(key_class == obj_dict[key_name]).all()
    if (len(results) == 0):
        obj = obj_class()
        for k,v in obj_dict.items():
            if (k in attrs):
                setattr(obj, k, v)
        print('persisting: {}'.format(obj_dict[key_name]))
        try:
            db.save(obj)
        except Exception as exp:
            print(type(exp))

def populate_swapi(url, obj_class):
    while (True):
        page_dict = get_json_dict(url)
        if (page_dict is None):
            break
        for obj_dict in page_dict['results']:
            persist(obj_class, obj_dict, obj_class.url, 'url')
        if (page_dict['next'] is None):
            break
        url = page_dict['next']

def populate_dck(url, obj_class):
    results = get_json_dict(url)
    if (results is not None):
        for obj_dict in results:
            persist(obj_class, obj_dict, obj_class.api, 'api')
            return
    i = 1
    while (True):
        results = get_json_dict('{}{}'.format(url, i))
        if (results is None):
            break
        for obj_dict in results:
            persist(obj_class, obj_dict, obj_class.api, 'api')
        i = i + 1

#############################

db = DbManager()  # db is global, so not passing into populate

populate_swapi('https://swapi.co/api/films/', swapi.Film)
populate_swapi('https://swapi.co/api/people/', swapi.Person)
populate_swapi('https://swapi.co/api/planets/', swapi.Planet)
populate_swapi('https://swapi.co/api/species/', swapi.Species)
populate_swapi('https://swapi.co/api/starships/', swapi.Starship)
populate_swapi('https://swapi.co/api/vehicles/', swapi.Vehicle)

populate_dck('http://data.coding.kitchen/api/cities/', dck.City)
populate_dck('http://data.coding.kitchen/api/clubs/', dck.Club)
populate_dck('http://data.coding.kitchen/api/companies/', dck.Company)
populate_dck('http://data.coding.kitchen/api/departments/', dck.Department)
populate_dck('http://data.coding.kitchen/api/exchanges/', dck.Exchange)
populate_dck('http://data.coding.kitchen/api/leagues/', dck.League)
populate_dck('http://data.coding.kitchen/api/people/', dck.Person)
populate_dck('http://data.coding.kitchen/api/states/', dck.State)

