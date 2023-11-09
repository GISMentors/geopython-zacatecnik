Příklad použití CMD Python API
------------------------------

Knihovna nabízí kromě Python API také velkou sadu nejrůznějších
nástrojů do příkazové řádky (`seznam
<https://gdal.org/programs/index.html>`__), více na školení
:skoleni:`Open Source GIS <open-source-gis/knihovny/gdal.html>`.

Příklad převodu vektorových dat z formátu *Esri Shapefile* na *OGC
GeoPackage* pomocí konzolového nástroje `ogr2ogr`. Součástí je převod do WGS-84 (`epsg`:4326) a vyběr prvků patřících do IV. zóny.

.. code-block:: bash

   ogr2ogr -f GPKG -where "ZONA = 'IV'" -t_srs EPSG:4326 chko_IV_epsg4326.gpkg chko.shp

Stejného výsledku lze dosáhnout v Pythonu pomocí funkce
`gdal.VectorTranslate
<https://gdal.org/api/python/osgeo.gdal.html#osgeo.gdal.VectorTranslate>`__:

.. code-block:: python

   from osgeo import gdal
   gdal.VectorTranslate('chko_IV_epsg4326.gpkg', 'chko.shp', format='GPKG',
                        where="ZONA = 'IV'", dstSRS='EPSG:4326')
