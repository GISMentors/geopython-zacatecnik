.. _rasterio-windows:

Použití oken pro čtení a zápis
------------------------------

Rastrová data lze číst a zapisovat i pomocí tzv. `"oken"
<https://rasterio.readthedocs.io/en/latest/topics/windowed-rw.html>`__. Tento
postup se hodí v případě, že pracujete s objemnými rastrovými daty,
které se do RAM vašeho počáítače nevejdou. Pomocí okna lze načíst část
matice rastrových dat, tu zpracovat a zapsat do výstupního souboru.

Okna (:class:`rasterio.Window`) jsou pravidelné matice vstupního
rastru. Lze je také popsat jako 2 páry souřadnic pixelů::
    
    ((první_řádek, poslední_řádek), (první_sloupec, poslední_sloupec))

nebo::

    Window(první_sloupeček, první_řádek, šířka, výška)

Příklad načtení dat::

    import rasterio
    with rasterio.open('data/lsat7_2002_nir.tiff') as src:
        w = src.read(1, window=Window(0, 0, 512, 256))
    
    print(w.shape)

Bloky
^^^^^

Rastrové soubory ukládají většinou data po blocích pokud chcete využívat okna
pro čtení, je efektivní, aby velikost oken odpovídala velikosti bloků.
Následujícím způsobem můžeme zpracovat první kanál našeho rastrového souboru po
blocích::

    with rasterio.open('data/lsat7_2002_nir.tiff') as src:
        for ji, window in src.block_windows(1):
            r = src.read(1, window=window)
            print(r.shape)

To jakým způsobem jsou bloky pro rastrový soubor definovány můžete
zjistit z příkazové řádky nástrojem ``gdalinfo``.

.. code-block:: bash

    gdalinfo data/lsat7_2002_nir.tiff

    Driver: GTiff/GeoTIFF
    Files: ../../data/lsat7_2002_nir.tiff
    Size is 1287, 831
    ...
    Band 1 Block=1287x1 Type=Float32, ColorInterp=Gray
    Band 2 Block=1287x1 Type=Float32, ColorInterp=Undefined
    Band 3 Block=1287x1 Type=Float32, ColorInterp=Undefined

Vidíme, že náš rastr používá bloky o velikosti 1287x1 pixel - tedy
celý řádek.  Někdy může být efektivnější celý rastr převzorkovat a
změnit nastavení bloků, než se pustíte samotného výpočtu. Toho
docílíme nástrojem knihovny GDAL `gdalwarp` (viz školení
:skoleni:`Úvod Open Source GIS
<open-source-gis/knihovny/gdal.html#prikazy-pro-praci-s-rastrovymi-daty>`).

.. code-block:: bash

    gdalwarp -r mode -co TILED=YES -co BLOCKXSIZE=256 -co BLOCKYSIZE=256 data/lsat7_2002_nir.tiff outputs/lsat7-256-block.tiff

    gdalinfo outputs/lsat7-256-block.tiff
    ...
    Band 1 Block=256x256 Type=Float32, ColorInterp=Gray
    Band 2 Block=256x256 Type=Float32, ColorInterp=Undefined
    Band 3 Block=256x256 Type=Float32, ColorInterp=Undefined

    with rasterio.open('data/lsat7_2002_nir.tiff') as src:
    
        for ji, window in src.block_windows(1):
            r = src.read(1, window=window)
            print(r.shape)

NDVI pomocí bloků
^^^^^^^^^^^^^^^^^

Následující příklad prezentuje opět výpočet NDVI, tentokrát ale bude
postupovat po blocích (čtení i zápis). Tento přístup bude fungovat
rychleji při větším objemu dat.

.. literalinclude:: ../../_static/skripty/rasterio-ndvi-windows.py
   :language: python
