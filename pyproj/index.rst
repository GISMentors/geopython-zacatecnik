Transformace souřadnic
======================

Na závěr malá odbočka k souřadnicovým systémům a Python rozhraní pro
knihovnu `Proj4 <http://trac.osgeo.org/proj>`_ - `PyProj
<https://github.com/jswhit/pyproj>`_.

V následujícím příkladu si ukážeme převod ze systému S-JTSK
(:epsg:`5514`) do WGS-84 (:epsg:`4326`):

.. literalinclude:: ../_static/skripty/pyproj-example.py
   :language: python
   :lines: 1-4

.. code-block:: python

    (12.807805435216094, 49.45302198345776)
