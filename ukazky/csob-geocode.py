#!/usr/bin/env python

import csv
import fiona
import random
from fiona.crs import from_epsg
from shapely.geometry import mapping, Point
import urllib2, urllib
import json

def create_shp(filename):
    schema = { 'geometry' : 'Point',
               'properties' : { 'mesto' : 'str',
                                'ulice' : 'str',
                                'cp' : 'str',
                                'telefon' : 'str',
                                'e-mail' : 'str' }
               }
    csob = fiona.open(filename, 'w', driver='ESRI Shapefile', schema=schema,
                      crs=from_epsg(5514), encoding='utf-8')
    return csob

def read_csv(filename):
    fd = open(filename)
    hlavicka = True
    data = []
    for row in csv.reader(fd):
        if hlavicka:
            hlavicka = False
            continue
        data.append(row)

    fd.close()

    return data

def write_features(shp, data):
    skipped = 0
    for row in data:
        ulice_cp = row[1]
        # odstranit z ulice pobocku (pokud je uvedena)
        if ulice_cp.endswith(')'):
            ulice_cp = ulice_cp.split('(', -1)[0]
        # rozdelit na ulici a cislo popisne
        ulice_slova = ulice_cp.split(' ', -1)
        ulice = ' '.join(ulice_slova[:-1])
        cp = ulice_slova[-1]

        # vygeneruj nahodne souradnice v rozsahu 0 a 1000
	x, y =  generate_point(addr="%s %s %s" % (row[0], ulice, cp))
	point = None
	if x and y:
            point = Point(x, y)

            # vytvorit a zapsat novy prvek
            feat = {'geometry': mapping(point),
                    'properties': {'mesto': row[0],
                                   'ulice' : ulice,
                                   'cp' : cp,
                                   'telefon' : row[2],
                                   'e-mail' : row[3]},
                    }
            shp.write(feat)
        else:
            print "Ulici %s nelze geokodovat, prvek preskocen" % row[1]
            skipped += 1
    
    if skipped > 0:
        print "Preskoceno %d prvku (z %d)" % (skipped, len(data))
    
def generate_point(min=0, max=1000, addr=None):
    url = 'http://nominatim.openstreetmap.org/search?q=' + urllib.quote(addr) + '&format=json&limit=1'
    response = urllib2.urlopen(url)
    jsondata = response.read()
    data = json.loads(jsondata)

    if data:
	    return float(data[0]["lon"]), float(data[0]["lat"])
    else:
	    return None, None

def main():
    # vytvorit novy shapefile
    csob = create_shp('csob.shp')

    # cist vstupni csv soubor    
    data = read_csv('csob.csv')

    write_features(csob, data)

    # zavrit vystupni shapefile, zapsat data na disk
    csob.close()

main()
