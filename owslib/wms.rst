
.. _OWSLibWMS:

OGC WMS
-------

.. index::
    single: WMS
    single: OGC OWS

`OGC Web Map Service <http://opengeospatial.org/standards/wms>`_
slouží ke stahování a sdílení mapových dat. Klientovi nejsou posílána
vlastní data, ale pouze náhled (obrázek) těchto dat.

.. note::

   Více informací na :skoleni:`školení Úvod do GIS
   <open-source-gis/standardy/ogc/wms.html>`.

.. literalinclude:: ../_static/skripty/owslib-wms-example.py
   :language: python
   :lines: 1,3-7
   
.. code-block:: python

    Prohlížecí služba WMS - ZM 10
    Prohlížecí služba WMS-ZM10-P je poskytována jako veřejná prohlížecí
    služba nad daty Základní mapy ČR 1:10 000.
    Zeměměřický úřad
    Pod Sídlištěm 9

Dostupné mapové vrstvy:

.. literalinclude:: ../_static/skripty/owslib-wms-example.py
   :language: python
   :lines: 9

.. code-block:: python

    {'GR_ZM10': <owslib.wms.ContentMetadata instance at 0x7f1d7bc1b8c0>}

Rozsah vrstvy:

.. literalinclude:: ../_static/skripty/owslib-wms-example.py
   :language: python
   :lines: 11-13

.. code-block:: python
   
    (-950003.175021186, -1250003.1750036045, -399990.474995786, -899996.8249909044, 'EPSG:5514')
    (11.214011580382529, 47.96491460125967, 19.40766262309513, 51.691664934538636)

Stažení a uložení dat:

.. literalinclude:: ../_static/skripty/owslib-wms-example.py
   :language: python
   :lines: 15-23

.. important:: Možné problémy při připojení ke službě. V minulosti končilo připojení chybou
          ``requests.exceptions.TooManyRedirects: Exceeded 30
          redirects.`` Vysvětlení hledejte na našem `blogu <http://gismentors.cz/blog/user-agent-hlavicka-requestu-na-wms-server/>`__.
          
.. task:: Vyzkoušejte připojení ke službě:

          .. code-block:: python

             url='http://gis.nature.cz/arcgis/services/UzemniOchrana/Natura2000/MapServer/WmsServer'
             layer='1' # Evropsky významné lokality (EVL)


          Výše zmíněna služba AOPK podporuje pouze WMS verze
          1.3.0. Vzhledem k tomu, že OWSLib používá ve výchozím
          nastavení verzi služby 1.1.1, je třeba verzi vynutit:

          .. code-block:: python

             wms = WebMapService(url, version='1.3.0')
