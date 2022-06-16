Editor Atom
===========

Editor Atom je k dispozici pro různé operační systémy.
Jedná se o editor, který v základu podporuje zvýrazňování syntaxe
různých jayzků, včetně jazyka Python.

Ke stažení je k dispozici na `https://atom.io/
<https://atom.io/>`__.

Instalace je jednoduchá.

Po spuštění je možné vytvořit nový soubor s příponou ``py``,
který v okamžiku uložení bude zvýrazněn dle syntaxe jazyka Python.

Spouštění skriptů přímo z editoru umožňuje řada balíčků, které je však nutno instalovat.
Nejznámější je *atom-python-run*, ale ten se nám bohužel nepodařilo nakonfigurovat tak,
aby načítal prostředí OSGeo4W.
Konfigurace se zdařila s využitím balíčku *script*.

Instalace balíčků se provádí z menu :menuselection:`File --> Settings`.
Zde zvolíme možnost ``Install`` a napíšeme **script**.

.. figure:: ../images/atom-install-packages.png
   :class: middle

Pak stiskneme tlačítko ``Install`` pro nalezený balíček *script*.

Po nainstalování můžeme nakonfigurovat interpret pro spouštění
z menu :menuselection:`Packages --> Script --> Configure Script`.

.. note:: Pokud nevidíte  :menuselection:`Packages --> Script --> Configure Script`
          zkuste Atom restartovat.

Zde pak musíme zapsat cestu k interpretu jazyka Python. V případě
využití OSGeo4W je vhodný BAT soubor
:file:`C:\\OSGeo4W\\bin\\python-qgis-ltr.bat` (anebo
:file:`C:\\OSGeo4W\\bin\\python-qgis.bat` na základě verze
QGISu, kterou máte nainstalovánu). Tento postup v každém případě
předpokládá, že máte v prostředí OSGeo4W nainstalován QGIS. Před
samotným spuštěním :file:`python.exe` nastaví korektní cesty ke
knihovnám.

Po nakonfigurování cesty je možné skript spouštět pomocí klávesové zkratky:

``Shift+Ctrl+b``

.. figure:: ../images/atom-configure-script.png
   :class: middle

   Konfigurace editoru pro prostředí OSGeo4W.

Výsledek spuštění následujícího skriptu

.. code-block:: python

    import rasterio
    import shapely
    import fiona
    from osgeo import gdal
    from osgeo import ogr
    print(fiona.__version__)

.. figure:: ../images/atom-run-output.png
   :class: middle

   Výsledek spuštění skriptu se objeví ve spodní části okna.
