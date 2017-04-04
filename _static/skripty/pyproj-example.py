import pyproj
sjtsk = pyproj.Proj("+init=epsg:5514")
wgs = pyproj.Proj("+init=epsg:4326")
print (sjtsk(-868208.53, -1095793.57, inverse=True))
