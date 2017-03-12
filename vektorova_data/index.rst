Práce s vektorovými daty
========================

Pro práci s vektorovými daty se v jazyce Python tradičně používá
knihovna `GDAL <http://gdal.org>`_ (resp. její čast označovaná jako
*OGR*). V poslední době však začíná být populární i knihovna `Shapely
<http://toblerity.org/shapely/>`_ a především `Fiona
<http://toblerity.org/fiona/>`_.

V rámci školení se zaměříme se na knihovny *Fiona* a *GDAL* (resp. její
část, která nese označení *OGR*). **Fiona** je projekt programátora `Seana
Gilliese <http://sgillies.net/>`_, který vytvořil vlastní aplikační
rozhraní ke knihovně OGR, které více odpovídá standardům a postupům
objektového jazyka Python. **OGR** je z tohoto pohledu knihovna, pomocí
které lze provádět v porovnání s Fionou nízkoúrovňovné operace.

.. note::

   Téma *OGR* je více popsáno ve školení :skoleni:`GeoPython pro
   pokročilé <geopython-pokrocily/vektorova_data/ogr/>`.

.. toctree::
   :maxdepth: 2

   fiona/index
