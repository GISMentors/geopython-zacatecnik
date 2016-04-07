.. only:: latex

   #####
   Obsah
   #####

.. only:: html

   `GISMentors <http://gismentors.cz>`_ | Školení `GRASS GIS
   <http://gismentors.cz/skoleni/grass-gis>`_ | `QGIS
   <http://gismentors.cz/skoleni/qgis>`_ | `PostGIS
   <http://gismentors.cz/skoleni/postgis>`_ | `GeoPython
   <http://gismentors.cz/skoleni/geopython>`_

   ********
   Motivace
   ********

.. figure:: images/python-logo.png
   :class: small
        
* :wikipedia:`Python` "baví"
* Python se "neučí", Python se "píše"
* Python je dnes asi nejvíce "geopozitivní" programovací jazyk

  * s množstvím knihoven a nástrojů (`GDAL <http://gdal.org>`_, `PROJ4
    <http://trac.osgeo.org/proj/>`_, `Shapely
    <http://toblerity.org/shapely/manual.html>`_, `Fiona
    <http://toblerity.org/fiona/manual.html>`_, `Rasterio
    <https://github.com/mapbox/rasterio>`_, `MapServer Python
    MapScript <http://mapserver.org/mapscript/python.html>`_, `GeoServer
    gsconfig <https://pypi.python.org/pypi/gsconfig>`_, `OWSLib
    <http://geopython.github.io/OWSLib/>`_, `PyWPS
    <http://pywps.wald.intevation.org/>`_, `pycsw <http://pycsw.org/>`_,
    ...)
  * a širokou podpora v deskopech (GRASS GIS - `PyGRASS
    <http://grass.osgeo.org/grass71/manuals/libpython/pygrass_index.html>`_,
    Esri ArcGIS - `arcpy
    <http://resources.arcgis.com/en/help/main/10.1/index.html#//000v000000v7000000>`_,
    QGIS - `PyQGIS
    <http://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/plugins.html>`_,
    ...)

.. index::
   pair: datové sady; ke stažení

.. notedata::

   *Data ke školení* je stažitelná jako `zip archiv
   <http://training.gismentors.eu/geodata/geopython/data.tgz>`_ (63
   MB). Dále můžete výužít data ze školení :skoleni:`QGIS pro
   začátečníky <qgis-zacatecnik>`  a to `vektorovová data
   <http://training.gismentors.eu/geodata/qgis/data.zip>`_ (436 MB) a
   rastrová data `DMT
   <http://training.gismentors.eu/geodata/qgis/dmt.zip>`_ (97 MB).

.. warning:: :red:`Toto je pracovní verze školení, která je aktuálně
             ve vývoji!`
                       
.. only:: html
             
   #####   
   Obsah
   #####
   
.. toctree::
   :maxdepth: 2

   uvod
   python/index
   vektorova_data/index
   rastrova_data/index
   owslib/index
   mapscript/index
   pyproj/index

*******
Dodatky
*******

Související materiály
=====================

Python
------

* Kurz PyLadies (česky): http://pyladies.cz/praha/
* Učebnice jazyka Python (česky): http://www.root.cz/knihy/ucebnice-jazyka-python
* Python guide: http://docs.python-guide.org/en/latest
* Dive into Python: http://www.diveintopython.net


GeoPython
---------

* **Python GDAL/OGR Cookbook**: http://pcjericks.github.io/py-gdalogr-cookbook/
* Shapely manual: http://toblerity.github.io/shapely/manual.html
* "Python Geospatial Development" book, Erik Westra:

  http://www.packtpub.com/python-geospatial-development/book
* Přednáška GDAL (ČVUT v Praze),

  http://geo.fsv.cvut.cz/~gin/yfsg/Free-Software-GIS-03-gdal-proj.pdf
* `Portál FreeGIS <http://freegis.fsv.cvut.cz/gwiki/GDAL#Uk.C3.A1zky_Python_skript.C5.AF>`_

Fóra, dokumentace
-----------------

* The GIS Stack Exchange: http://gis.stackexchange.com/

  (http://gis.stackexchange.com/?tags=python)
* Last but not least, https://www.google.com

O dokumentu
===========

Text školení je licencován pod `Creative Commons Attribution-ShareAlike 4.0 International License <http://creativecommons.org/licenses/by-sa/4.0/>`_.

.. figure:: images/cc-by-sa.png 
   :width: 130px
   :scale-latex: 120
              
*Verze textu školení:* |release| (sestaveno |today|)

Autoři
------

Za `GISMentors <http://www.gismentors.cz/>`_:

* `Jáchym Čepický <http://www.gismentors.cz/mentors/cepicky>`_ ``<jachym.cepicky opengeolabs.cz>``
* `Martin Landa <http://www.gismentors.cz/mentors/landa>`_ ``<martin.landa opengeolabs.cz>``

Text dokumentu
--------------

.. only:: latex

   Online HTML verze textu školení je dostupná na adrese:

   * http://training.gismentors.eu/geopython/

Zdrojové texty školení jsou dostupné na adrese:

* https://github.com/GISMentors/geopython

