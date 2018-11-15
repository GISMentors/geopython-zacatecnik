Práce s vektorovými daty
========================

Pro práci s vektorovými daty se v jazyce Python tradičně používá
knihovna `GDAL <http://gdal.org>`__ (resp. její čast označovaná jako
*OGR*). V poslední době však začíná být populární knihovna `Fiona
<https://github.com/Toblerity/Fiona>`__ v kombinaci s `Shapely
<https://github.com/Toblerity/Shapely>`__.

*Fiona/Shapely* je projekt programátora `Seana Gilliese
<http://sgillies.net/>`__, který vytvořil vlastní aplikační rozhraní
ke knihovně OGR, které více odpovídá standardům a postupům objektového
jazyka Python. OGR je z tohoto pohledu knihovna, pomocí které lze
provádět v porovnání s Fionou "nízkoúrovňovné" operace.

.. note:: Pro více informací o vektorových datech ve školení
   :skoleni:`Úvod do GIS <open-source-gis/formaty/vektor.html>`.

.. toctree::
   :maxdepth: 2

   fiona/index
   ogr/index
