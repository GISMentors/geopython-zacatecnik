Příklad vytvoření obalové zóny
------------------------------

Na tomto příkladu si ukážeme, jak otevřít vektorová data ve formátu
Esri Shapefile, načíst datovou vrstvu, zobrazit atributy geoprvků a
vytvořit obalovou zónu nad načtenými geoprvky.

Nejprve otevření souboru s daty:

.. code-block:: python

    >>> from osgeo import ogr
    >>> ds = ogr.Open("data/chko.shp")
    >>> ds
    <osgeo.ogr.DataSource; proxy of <Swig Object of type 'OGRDataSourceShadow *' at 0x7f98d8152a50> >
    >>> ds.GetLayerCount()
    1

Práce s vrstvou, její otevření:

.. code-block:: python

    >>> l = ds.GetLayer(0)
    >>> l
    <osgeo.ogr.Layer; proxy of <Swig Object of type 'OGRLayerShadow *' at 0x7f98d80fa870> >
    >>> l.GetFeatureCount()
    5626

Schéma vrstvy - definice typu geometrie a jednotlivých atributových polí:

.. code-block:: python
    
   >>> l.GetGeomType()
   3
   >>> l.GetGeomType() == ogr.wkbPolygon
   True
   >>> l.schema
   [<osgeo.ogr.FieldDefn; proxy of <Swig Object of type 'OGRFieldDefnShadow *' at 0x7f98d80fa9f0> >,
   <osgeo.ogr.FieldDefn; proxy of <Swig Object of type 'OGRFieldDefnShadow *' at 0x7f98d80fa8...
   >>> ...
   >>> l.schema[4].name
   'NAZEV'

Vypsání názvu geoprvku (atribut ``NAZEV``):

.. code-block:: python

    >>> features_nr = l.GetFeatureCount()
    >>> for i in range(features_nr):
    ...     f = l.GetNextFeature()
    ...     print(f.GetField('NAZEV'))
    Český ráj
    ...

Vypsání vlastnosti geometrické složky popisu geoprvků (minimálního
ohraničujícího obdélíku a centroidu polygonu):

.. code-block:: python

    >>> f = l.GetFeature(54)
    >>> f.GetField('NAZEV')
    >>> print (f.GetField('NAZEV'))
    Český ráj
    >>> geom = f.GetGeometryRef()
    >>> geom.GetEnvelope()
    (-683329.1875, -681265.625, -993228.75, -991528.0)
    >>> c = geom.Centroid()
    >>> c.GetPoint()
    (-682407.4126500859, -992433.3498782327, 0.0)
    >>> buff = c.Buffer(100)
    >>> geom.Intersects(buff)
    True
