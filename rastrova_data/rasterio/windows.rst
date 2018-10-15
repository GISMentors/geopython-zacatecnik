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
    with rasterio.open('data/B04-2018-05-06.tiff') as red:
        w = red.read(1, window=Window(0, 0, 512, 256))
    
    print(w.shape)

Bloky
^^^^^

Rastrové soubory ukládají většinou data po blocích pokud chcete využívat okna
pro čtení, je efektivní, aby velikost oken odpovídala velikosti bloků.
Následujícím způsobem můžeme zpracovat první kanál našeho rastrového souboru po
blocích::

    with rasterio.open('data/B04-2018-05-06.tiff') as red:
        for ji, window in red.block_windows(1):
            r = red.read(1, window=window)
            print(r.shape)

To jakým způsobem jsou bloky pro rastrový soubor definovány můžete
zjistit z příkazové řádky nástrojem ``gdalinfo``.

.. code-block:: bash

    gdalinfo data/B04-2018-05-06.tiff

    Driver: GTiff/GeoTIFF
    Files: B04-2018-05-06.tiff
        B04-2018-05-06.tiff.aux.xml
    Size is 3117, 1716
     
    ...
    Band 1 Block=3117x8 Type=UInt16, ColorInterp=Gray

Vidíme, že náš rastr používá bloky o velikosti 3117×8 pixel - tedy 8 řádků.
Někdy může být efektivnější celý rastr převzorkovat, než se pustíte do jeho
blok-po-bloku processingu. To můžeme udělat např. 
nástrojem knihovny GDAL `gdalwarp` (viz školení
:skoleni:`Úvod Open Source GIS <open-source-gis/knihovny/gdal.html#prikazy-pro-praci-s-rastrovymi-daty>`).

.. code-block:: bash

    gdalwarp -r mode -co TILED=YES -co BLOCKXSIZE=256 -co BLOCKYSIZE=256 B04-2018-05-06.tiff outputs/B04-2018-05-06-256block.tiff

    Creating output file that is 1287P x 831L.
    Processing input file ../../data/B04-2018-05-06.tiff.
    0...10...20...30...40...50...60...70...80...90...100 - done.

    gdalinfo outputs/B04-2018-05-06-256block.tiff

    ...
    Band 1 Block=256x256 Type=UInt16, ColorInterp=Gray

A otevřít v Pythonu::

    with rasterio.open('outputs/B04-2018-05-06-256block.tiff') as red:

        for ji, window in src.block_windows(1):
            r = red.read(1, window=window)
            print(r.shape)

NDVI pomocí bloků
^^^^^^^^^^^^^^^^^

Následující příklad prezentuje opět výpočet NDVI, tentokrát ale bude
postupovat po blocích (čtení i zápis). Tento přístup bude fungovat
rychleji při větším objemu dat.

.. literalinclude:: ../../_static/skripty/rasterio-ndvi-windows.py
   :language: python
