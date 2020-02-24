========================================
Výběr textového editoru pro jazyk Python
========================================

Pro uživatele Windows se jako vhodný jeví nástroj PyCharm. 
V komunitní verzi je k dispozici zdarma. Jeho instalace
je jednoduchá. Ke stažení je na `<https://www.jetbrains.com/pycharm/>`_

Po spuštění editoru je možné vytvořit nový projekt.

.. figure:: images/pycharm-project.png
   :class: middle

Při jeho konfiguraci je možné nastavit interpret jazyka.

.. figure:: images/pycharm-interpret.png
   :class: middle

V případě využití OSGeo4W je vhodný BAT soubor C:\\OSGeo4W64\\bin\\python-qgis.bat
Obsahuje přes samotným spuštěním python.exe nastavení cest, ke knihovnám.

V nově vytvořeném projektu můžeme kliknout pravým tlačítkem na název projektu a
přidat nový Python soubor.

.. figure:: images/pycharm-file.png
   :class: middle

Soubor můžeme naplnit importem knihoven, které budeme používat, 
tak abychom ověřili, že máme konfiguraci v pořádku.

.. code-block:: python

    import rasterio
    import shapely
    import fiona
    from osgeo import gdal
    from osgeo import ogr

Spuštění kódu realizujeme přes menu Run.

.. figure:: images/pycharm-run-1.png
   :class: middle

Vytvoříme novou konfiguraci.

.. figure:: images/pycharm-run-2.png
   :class: middle

Zejména vybereme skript, který chceme v této konfiguraci spouštět.

.. figure:: images/pycharm-run-3.png
   :class: middle

A pak již můžeme pomocí tlačítka Run skript spustit.
Další spuštění je pak již jednodušší, protože konfigurace je již k dispozici.

Pokud vše proběhne bez problémů uvidíme výstup s exit code 0.

.. figure:: images/pycharm-run-4.png
   :class: middle

