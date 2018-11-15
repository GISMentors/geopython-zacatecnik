Příklad vytvoření nové vrstvy
-----------------------------

Následující příklad ukazuje přístup k vektorovým datům *od A do Z*,
tedy vytvoření nové datové vrstvy, nastavení metadat, vytvoření a
zápis nového geoprvku, uložení změn do souboru. To celé by šlo vykonat
pomocí výše zmíněné knihovny :ref:`Fiona <fiona>` několikanásobně
jednodušeji. OGR přistupuje k datům na nižší úrovni, což může být
někdy výhodnější.

.. code-block:: python

    >>> from osgeo import osr
    >>> # Vytvoření driveru pro formát GML a vytvoření prázdného souboru
    >>> drv = ogr.GetDriverByName('GML')
    >>> ds = drv.CreateDataSource('/tmp/out.gml')
    >>> srs = osr.SpatialReference()
    >>> srs.ImportFromEPSG(5514)
    >>> layer = ds.CreateLayer('out.gml', srs, ogr.wkbLineString)

    >>> # Vytvoření nového atributu 'Nazev' a 'Kod'
    >>> field_name = ogr.FieldDefn('Nazev', ogr.OFTString)
    >>> field_name.SetWidth(24)
    >>> field_number = ogr.FieldDefn('Kod', ogr.OFTInteger)
    >>> layer.CreateField(field_name)
    >>> layer.CreateField(field_number)

    >>> # Vytvoření nové geometrie typu linie - načtením z formátu WKT
    >>> line = ogr.CreateGeometryFromWkt('LINESTRING(%f %f, %f %f)' % (0, 0, 1, 1))

    >>> # Vytvoření nového prvku, nastavení geometrie a atributu Nazev
    >>> feature = ogr.Feature(layer.GetLayerDefn())
    >>> feature.SetGeometry(line)
    >>> feature.SetField("Nazev", 'Základní linie')
    >>> feature.SetField("Kod", 42)
    >>> ...
    >>> layer.CreateFeature(feature)
    >>> ...
    >>> # Úklid
    >>> feature.Destroy()
    >>> ds.Destroy()

Výsledek zkontrolujeme:

.. code:: python

    >>> ds = ogr.Open('/tmp/out.gml')
    >>> layer = ds.GetLayer(0)
    >>> layer.GetFeatureCount()
    1
    >>> ds.Destroy()

    
.. Malá odbočka k pyproj
.. 
.. .. code-block:: python
.. 
..     >>> import pyproj
..     >>> sjtsk = pyproj.Proj("+init=epsg:5514")
..     >>> wgs = pyproj.Proj("+init=epsg:4326")
.. 
