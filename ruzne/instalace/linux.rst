Instalace na operačním systému Linux
====================================

Nejsnazším způsobem je použít balíčky jazyka Python přímo z
distribuce. V případě Ubuntu nebo Debian stačí spustit terminál a
pomocí nástroje :program:`apt` Python nainstalovat.

.. figure:: ../images/install-ubuntu.png

        Instalace jazyka Python do prostředí Linux

Vedle samotného interpretu jazyka je dobré pořídit i balíčkovací
nástroj :program:`pip` pro instalaci dalších knihoven

.. code-block:: bash

        $ sudo apt install python3 python3-pip

Po instalaci můžeme ověřit přítomnost jazyka spuštěním jeho interpretu::

        $ python3
        Python 3.11.6 (main, Oct  8 2023, 05:06:43) [GCC 13.2.0] on linux
        Type "help", "copyright", "credits" or "license" for more information.
        >>>

Protože se pohybujeme v "geo" světě, je dobré doinstalovat i další potřebné
knihovny, zejména podporu pro knihovnu `GDAL <http://gdal.org>`_. Pokud je v
balíčcích přítomná, tím lépe


.. code-block:: bash

   sudo apt-get install fiona python3-fiona rasterio python3-rasterio \
    python3-owslib python3-pyproj python3-gdal libgdal-dev

.. tip:: Pro uživatele Ubuntu. Pokud potřebuje novější verze knihoven
   než jsou v distribuci, tak před instalací zaregistrujte ještě
   `repositář UbuntuGIS
   <https://launchpad.net/~ubuntugis/+archive/ubuntu/ubuntugis-unstable/+packages?field.name_filter=python&field.status_filter=published&field.series_filter=>`__.

   .. code-block:: bash

      sudo add-apt-repository ppa:ubuntugis/ubuntugis-unstable
      sudo apt update
