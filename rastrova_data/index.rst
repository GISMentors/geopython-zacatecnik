Práce s rastrovými daty
=======================

Rastrová data mohou být v porovnání s vektorovými daty často řádově
objemnější. Tomu je třeba přizpůsobit práci s nimi. Rastrová data jsou
většinou uspořádané do matice hodnot v číselné podobě.

.. note::
   
   Více k rastrové reprezentaci ve školení :skoleni:`Úvod do GIS
   <open-source-gis/formaty/rastr.html>`.

Pro práci s rastrovými geodaty se "tradičně" používá knihovna `GDAL
<http://gdal.org>`_. Knihovna GDAL je nízkoúrovňová, přistupuje k
datům pokud možno efektivním způsobem. Alternativou ke knihovně GDAL
je `Rasterio <https://github.com/mapbox/rasterio>`_, která je nad
touto knihovnou postavena. Jedná se o jakousi analogii ke knihovnám
*OGR* a :doc:`Fiona <../vektorova_data/fiona/index>` pro práci s
vektorovými daty.


.. note::

    Téma *GDAL* je více popsáno ve školení :skoleni:`GeoPython pro
    pokročilé <geopython-pokrocily/rastrova_data/>`.

.. toctree::
   :maxdepth: 2

   rasterio/index
