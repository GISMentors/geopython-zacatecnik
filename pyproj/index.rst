Transformace souřadnic
======================

Na závěr malá odbočka k souřadnicovým systémům a Python rozhraní pro
knihovnu `Proj <https://proj4.org/>`_ - `PyProj
<https://github.com/jswhit/pyproj>`__.

V následujícím příkladu si ukážeme převod ze systému S-JTSK
(:epsg:`5514`) do WGS-84 (:epsg:`4326`):

.. literalinclude:: ../_static/skripty/pyproj-example.py
   :language: python

::

    (12.807805435216094, 49.45302198345776)
