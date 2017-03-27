Poznámky k pracovnímu prostředí
===============================

.. todo:: doplnit

Ubuntu/Debian
-------------

Instalace knihoven z výchozích repozitářů by měla v běžné situaci
stačit.

.. code-block:: bash

   sudo apt-get fiona python-fiona rasterio python-rasterio python-owslib python-pyproj

.. tip:: Pokud potřebuje novější verze knihoven, tak před instalací
   zaregistrujte ještě UbuntuGIS repozitář.

   .. code-block:: bash

      sudo add-apt-repository ppa:ubuntugis/ubuntugis-unstable
      sudo apt-get update

MS Windows
----------
