from osgeo import ogr
ds = ogr.Open("data/chko.shp")
print(ds)
print(ds.GetLayerCount())
l = ds.GetLayer(0)
print(l)
print(l.GetFeatureCount())
    
print(l.GetGeomType())
print(l.GetGeomType() == ogr.wkbPolygon)
print(l.schema)
print(l.schema[4].name)

features_nr = l.GetFeatureCount()
for i in range(features_nr):
    f = l.GetNextFeature()
    print(f.GetField('NAZEV'))
    break

f = l.GetFeature(54)
f.GetField('NAZEV')
print (f.GetField('NAZEV'))

geom = f.GetGeometryRef()
print(geom.GetEnvelope())

c = geom.Centroid()
print(c.GetPoint())

buff = c.Buffer(100)
print(geom.Intersects(buff))
