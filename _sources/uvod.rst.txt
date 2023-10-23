Úvod
====

**Python** je populární programovací jazyk, který má své četné příznivce stejně
jako zarputilé odpůrce. Oproti jiným běžně rozšířeným jazykům je jeho syntaxe
zvláštní mimo jiné v tom, že nepoužívá závorky - bloky kódu jsou odděleny
pouhým *odsazením* zdrojového textu.

.. note:: **Příklad funkce main() v jazyku Python**

   .. code:: bash

      def main():
          print("ahoj")

Ve světe geoinformačních technologií je Python velice oblíbený (a
můžeme říci, že čím dál oblíbenější). Stojí rozkročen mezi jednoduchým
skriptováním v :wikipedia:`shellu <Shellový skript>` a pokročilým
programováním na takřka systémové úrovni v :wikipedia:`jazyce C <C
(programovací jazyk)>`. Má v sobě něco i z přístupů jazyka
:wikipedia:`Java <Java (programovací jazyk)>`. Většina existujících
knihoven a programů má pro tento jazyk svoje rozhraní, jako příklad
můžeme uvést `GDAL Python API <http://gdal.org/python/>`__.

S Pythonem lze ve světě GIS dojít daleko, níže uvádíme malý přehled
vybraných nástrojů a jejich napojení na jazyk Python:

**Desktop**
    * *GRASS GIS*: https://grass.osgeo.org (více na školení :skoleni:`GRASS GIS pro pokročilé <grass-gis-pokrocily/skripty/index.html>`)
    * *QGIS*: https://qgis.org (více na školeni :skoleni:`Tvorba zásuvných modulů QGIS <qgis-plugins>`)
    * *ArcGIS*: https://www.arcgis.com (`arcpy <https://pro.arcgis.com/en/pro-app/arcpy/get-started/what-is-arcpy-.htm>`__)

**Web**
    * *MapServer*: https://mapserver.org
    * *GeoServer*: https://geoserver.org
    * *TileCache*: http://tilecache.org
    * *PyWPS*: https://pywps.org
    * *GeoDjango*: https://geodjango.org
    * ...
      
**Knihovny a nástroje**
    * *GDAL*: https://gdal.org (`Python API <https://gdal.org/python/>`__)
    * *Fiona*: https://github.com/Toblerity/Fiona
    * *Shapely*: https://github.com/Toblerity/Shapely
    * *Rasterio*: https://github.com/mapbox/rasterio
    * *PyProj*: https://github.com/jswhit/pyproj
    * *R (rpy2)*: https://rpy2.github.io
    * *GeoPandas*: https://geopandas.org
    * ...
      
**Databáze**
    * *PostGIS*: https://postgis.net (https://pypi.org/project/postgis/)
    * *SpatiaLite*: https://www.gaia-gis.it/fossil/libspatialite/index (https://pypi.org/project/spatialite/)
    * *GeoAlchemy*: https://geoalchemy.org
    * ...
      
**Specializované nástroje**
    * *TopoJSON*: https://github.com/calvinmetcalf/topojson.py
    * *RTree index*: https://github.com/Toblerity/rtree
    * ...
      
Seznam samozřejmě není úplný či konečný.

V tomto kurzu se zaměříme na úvod do práce s vektorovými a rastrovými
GIS daty pomocí knihoven :doc:`Fiona/Shapely
<vektorova_data/fiona/index>` a :doc:`Rasterio
<rastrova_data/rasterio/index>`. Nevyhneme se ani knihovně :doc:`GDAL
<rastrova_data/gdal/index>` / :doc:`OGR
<vektorova_data/ogr/index>`. Vyzkoušíme si také práci s knihovnou pro
webové služby OGC :doc:`OWSLib <owslib/index>`. Okrajově se dotkneme
práce se souřadnicovými systémy pomocí knihovny :doc:`pyproj
<pyproj/index>`.

Cílem kurzu není přirozeně kompletní pokrytí problematiky GIS a jazyka
Python, nýbrž poskytnutí přehledu o nejčastěji používaných základních
nástrojích, nad kterými lze stavět další aplikace. Tyto nástroje jsou
ve své většině používány i dalšími programy a knihovnami a proto je
dobré o nich vědět a chápat jejich principy.
    
