GeoDjango
=========

`Django <https://www.djangoproject.com/>`_ Django je vyspělý webový framework
napsaný v jazyce Python, který podporuje rychlý vývoj a čisté, pragmatické
konstrukce. Django je dnes v komunitě Pythonu velice populární a existuje
množství rozšíření. Jedním takovým rozšířením je i tzv. `GeoDjango <https://docs.djangoproject.com/en/2.1/ref/contrib/gis/>`_

`django.contrib.gis` (GeoDjango)  rozšiřuje datové modely používané v Django o
typy geometrií. Pro ukládání používá buď databázi PostGIS nebo SpatiaLite.

* GeometryField
* PointField
* LineStringField
* PolygonField
* MultiPointField
* MultiLineStringField
* MultiPolygonField
* GeometryCollectionField
* RasterField

Definice modelu
---------------

Příklad definice modelu v s geometrickým atributem

.. code-block:: python

    from django.contrib.gis.db import models

    class Street(models.Model):

        name = models.CharField(max_length=50)
        width = models.FloatField()
        geometry = models.LineStringField()

Závislosti
----------

Jako databázový backend používá GeoDjango PostGIS, SpatiaLite ale i další
databáze. Následující tabulka ukazuje další potřebné knihovny, pro různé verze
databází:


+------------+--------------------------------+----------------+------------------------------------------------+
| Databáze   | Požadované knihovny            | Verze databází | Poznámka                                       |
+============+================================+================+================================================+
| PostgreSQL | GEOS, GDAL, PROJ.4, PostGIS    | 9.3+           | Vyžaduje PostGIS.                              |
+------------+--------------------------------+----------------+------------------------------------------------+
| MySQL      | GEOS, GDAL                     | 5.5+           | Není kompatibilní s OGC; omezená funkcionalita |
+------------+--------------------------------+----------------+------------------------------------------------+
| Oracle     | GEOS, GDAL                     | 12.1+          | Express Edition (XE) není podporována          |
+------------+--------------------------------+----------------+------------------------------------------------+
| SQLite     | GEOS, GDAL, PROJ.4, SpatiaLite | 3.6.+          | Vyžaduje SpatiaLite 4.0+                       |
+------------+--------------------------------+----------------+------------------------------------------------+

GeoDjango dále závisí na následujících knihovnách

* GDAL/OGR pro zpracování dat
* GEOS pro prostorové topologické operace
* PROJ.4 pro souřadnicové transformace

.. todo:: Tato část je zatím *pahýl* a potřebuje rozšířit.
