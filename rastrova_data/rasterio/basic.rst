.. _rasterio-basic:

Základní metadata rastrových dat
--------------------------------

V následujícím příkladu otevřeneme rastrový soubor ve formátu
:wikipedia-en:`GeoTIFF` a podíváme se na některá metadata:


.. literalinclude:: ../../_static/skripty/rasterio-example.py
   :language: python
   :lines: 1-3
              
.. code-block:: python

    BoundingBox(left=596670.0, bottom=185000.0, right=678330.0, top=258500.0)

.. literalinclude:: ../../_static/skripty/rasterio-example.py
   :language: python
   :lines: 5

.. code-block:: python
                
   {u'lon_0': -79, u'datum': u'NAD83', u'y_0': 0, u'no_defs': True,
   u'proj': u'lcc', u'x_0': 609601.22,
   u'units': u'm', u'lat_2': 34.33333333333334, u'lat_1': 36.16666666666666,
   u'lat_0': 33.75}

.. literalinclude:: ../../_static/skripty/rasterio-example.py
   :language: python
   :lines: 7

.. code-block:: python
                
    {u'AREA_OR_POINT': u'Area'}

.. literalinclude:: ../../_static/skripty/rasterio-example.py
   :language: python
   :lines: 9

.. code-block:: python
                
    (1287, 831)

.. literalinclude:: ../../_static/skripty/rasterio-example.py
   :language: python
   :lines: 11
    
.. code-block:: python
                
    (10.0, 10.0)

.. figure:: ../images/rgb.png

   RGB kompozice.

Načtení dat barevných kanálů:

.. literalinclude:: ../../_static/skripty/rasterio-example.py
   :language: python
   :lines: 13-14

.. code-block:: python

    3
