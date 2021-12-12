#!/usr/bin/env python
# coding: utf-8

# In[1]:


dataset = [{
      "store": "Verona",
      "latitude": 45.472300,
      "longitude": 10.9645700,
    }, {
      "store": "Treviso - Montebelluna",
      "latitude": 45.7789400,
      "longitude": 12.0018200,
    }, {
      "store": "Pordenone - Fiume Veneto",
      "latitude": 45.94545,
      "longitude": 12.717415,
    }, {
      "store": "Trieste",
      "latitude": 45.69379,
      "longitude": 13.11839,
    }, {
      "store": "Udine - Tavagnacco",
      "latitude": 46.11039,
      "longitude": 13.27786,
    }, {
      "store": "Brescia - San Zeno sul Naviglio",
      "latitude": 45.49626,
      "longitude": 10.21856,
    }, {
      "store": "Padova",
      "latitude": 45.413944,
      "longitude": 11.919801,
    }, {
      "store": "Venezia - Marcon",
      "latitude": 45.547356,
      "longitude": 12.3867,
    }, {
      "store": "Venezia - San Dona di Piave",
      "latitude": 45.607,
      "longitude": 12.5397,
    }, {
      "store": "Bergamo",
      "latitude": 45.6885,
      "longitude": 9.6014,
    }, {
      "store": "Vicenza",
      "latitude": 45.29185,
      "longitude": 11.98584,
    }, {
      "store": "Bologna",
      "latitude": 44.198454,
      "longitude": 11.617676,
    }, {
      "store": "Reggio Emilia",
      "latitude": 44.112067,
      "longitude": 10.172083,
    }, {
      "store": "Como",
      "latitude": 45.7632796,
      "longitude": 9.0558871,
    }, {
      "store": "Torino - Chivasso",
      "latitude": 45.01360,
      "longitude": 7.93376,
    }, {
      "store": "Cremona",
      "latitude": 45.140326,
      "longitude": 10.03,
    }, {
      "store": "Verona - Castelnuovo del Garda",
      "latitude": 45.4419,
      "longitude": 10.727042,
    }, {
      "store": "Milano - Rozzano",
      "latitude": 45.3344,
      "longitude": 9.17192,
    }, {
      "store": "Sondrio - Castione Andevenno",
      "latitude": 46.185900,
      "longitude": 9.8166800,
    }, {
      "store": "Treviso - San Fior",
      "latitude": 45.902810,
      "longitude": 12.3623220,
    }, {
      "store": "Milano - Baranzate",
      "latitude": 45.533447,
      "longitude": 9.07669,
    }, {
      "store": "Alessandria",
      "latitude": 44.09236,
      "longitude": 8.35420,
    }, {
      "store": "Modena",
      "latitude": 44.464,
      "longitude": 10.74113,
    },{
      "store": "Imola",
      "latitude": 44.3905,
      "longitude": 11.33159,
},{
      "store": "Cerro Maggiore",
      "latitude": 45.10434,
      "longitude": 8.9561,
},{
      "store": "Castelletto Ticino",
      "latitude": 45.19472, 
      "longitude": 8.17704,
},

  ]


# ### Esempio output
# "Verona" : { "Treviso": 70km, "Venezia": 80km .... ....}

from pprint import pprint
from math import radians, sin, cos, asin, sqrt


def calc_distances(lon1,lon2,lat1,lat2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])    
    dlon = lon2 - lon1
    dlat = lat2 - lat1    
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    return(round(2 * 6371 * asin(sqrt(a)),2))


def get_distances(data):
    store_distances = {}
    for j in data:
        dict_city = {}
        for i in range(len(data)):
            dict_city[data[i]['store']] = calc_distances(j['latitude'],data[i]['latitude'],j['longitude'],data[i]['longitude'])

        store_distances[j['store']] =  dict_city
    return(store_distances)


stores = get_distances(data=dataset)
pprint(stores)

