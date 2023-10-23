import fiona

chko = fiona.open('data/chko.shp', 'r', encoding='utf-8')
print(chko)
print(chko.driver)

# doporučujeme využít více obvyklou cestu otevírání souborů pomocí příkazu
# `with`, který je schopný na konci bloku kódu soubor automaticky uzavřít
#
# with fiona.open("data/chko.shp", "r", encoding='utf-8') as chko:
#   print(chko)

# souřadnicový systém
print(chko.crs)

# jméno souboru
print(chko.path)

# jméno vrstvy
print(chko.name)

# hraniční souřadnice
print(chko.bounds)

# všechna metadata pohromadě
print(chko.meta)
import json # naformátovat výstup
# TypeError: Object of type CRS is not JSON serializable
#print(json.dumps(chko.meta, sort_keys=True, indent=4, separators=(',', ': ')))

with fiona.open('data/natural.shp') as data:
    print(data.crs)

from fiona.crs import from_epsg
print(from_epsg(5514))

print("Počet prvků: ", len(chko))

for feature in chko:
    print(feature['geometry']['type'])
    break

print(chko[54]['properties']['NAZEV'])

from shapely.geometry import shape
cr = chko[54]
poly = shape(cr['geometry'])
print(poly.bounds)

simple = poly.simplify(10)
print(simple.intersects(poly))

buff = poly.buffer(10)
print(buff.contains(poly))

from shapely.geometry import mapping
from fiona import Feature, Geometry
props = dict(cr.properties)
props['NAZEV'] = 'Mordor'
feature = Feature(geometry=Geometry.from_dict(mapping(buff)), properties=props)
chko.close()
chko = fiona.open('data/chko.shp', 'a')
print(len(chko))

chko.write(feature)
print(len(chko))

chko.close()
