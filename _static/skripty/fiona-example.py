import fiona

chko = fiona.open('data/chko.shp', 'r')
print(chko)
print(chko.driver)

# doporučujeme využít více obvyklou cestu otevírání souborů pomocí příkazu
# `with`, který je schopný na konci bloku kódu soubor automaticky uzavřít
#
# with fiona.open("data/chko.shp", "r") as chko:
#   print(chko)

from fiona.crs import to_string
print(to_string(chko.crs))

from fiona.crs import from_epsg
from_epsg(5514)

for feature in chko:
    print(feature['geometry']['type'])

print(chko[54]['properties']['NAZEV'])

from shapely.geometry import shape
cr = chko[54]
poly = shape(cr['geometry'])
print (poly.bounds)

simple = poly.simplify(10)
print (simple.intersects(poly))

buff = poly.buffer(10)
print (buff.contains(poly))

from shapely.geometry import mapping
import copy
feature = copy.deepcopy(cr)
feature['id'] = -1
feature['geometry'] = mapping(buff)
feature['properties']['NAZEV'] = u'Mordor'
chko = fiona.open('data/chko.shp', 'a')
print (len(chko))

chko.write(feature)
print (len(chko))

chko.close()
