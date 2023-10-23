from osgeo import ogr, osr

# Vytvoření driveru pro formát GML a vytvoření prázdného souboru
fn = '/tmp/out.gml'
drv = ogr.GetDriverByName('GML')
ds = drv.CreateDataSource(fn)
srs = osr.SpatialReference()
srs.ImportFromEPSG(5514)
layer = ds.CreateLayer('out', srs, ogr.wkbLineString)

# Vytvoření nového atributu 'Nazev' a 'Kod'
field_name = ogr.FieldDefn('Nazev', ogr.OFTString)
field_name.SetWidth(24)
field_number = ogr.FieldDefn('Kod', ogr.OFTInteger)
layer.CreateField(field_name)
layer.CreateField(field_number)

# Vytvoření nové geometrie typu linie - načtením z formátu WKT
line = ogr.CreateGeometryFromWkt('LINESTRING({} {}, {} {})'.format(0, 0, 1, 1))

# Vytvoření nového prvku, nastavení geometrie a atributu Nazev
feature = ogr.Feature(layer.GetLayerDefn())
feature.SetGeometry(line)
feature.SetField("Nazev", 'Základní linie')
feature.SetField("Kod", 42)
# ...
layer.CreateFeature(feature)
# ...
# Úklid
feature.Destroy()
ds.Destroy()

# Výsledek zkontrolujeme:
ds = ogr.Open(fn)
layer = ds.GetLayer(0)
print(layer.GetFeatureCount())
ds.Destroy()
