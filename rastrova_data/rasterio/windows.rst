.. _rasterio-windows:

Použití oken při čtení a zápis
------------------------------
I když jsou zpracovávaná rastrová data větší, než je pamět RAM vašeho stroje, je
možné použít tzv. `"okna" pro jejich čtení nebo zápis <https://mapbox.github.io/rasterio/topics/windowed-rw.html>`_.

Okna (:class:`rasterio.Window`) jsou pravidelné matice vstupního rastru. Lze je
také popsat jako 2 páry souřadnic pixelů::
    
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

Jak jsou bloky na rastru definovány můžete z příkazové řádky nástrojem
``gdalinfo``.

.. code-block:: bash

    gdalinfo data/lsat7_2002_nir.tiff

    Driver: GTiff/GeoTIFF
    Files: ../../data/lsat7_2002_nir.tiff
    Size is 1287, 831
    ...
    Band 1 Block=1287x1 Type=Float32, ColorInterp=Gray
    Band 2 Block=1287x1 Type=Float32, ColorInterp=Undefined
    Band 3 Block=1287x1 Type=Float32, ColorInterp=Undefined

Vidíme, že náš rastr používá bloky o velikosti 1287x1 pixel - tedy celý řádek.
Někdy může být efektivnější celý rastr převzorkovat, než se pustíte do jeho
blok-po-bloku processingu.

.. code-block:: bash

    gdalwarp -r mode -co TILED=YES -co BLOCKXSIZE=256 -co BLOCKYSIZE=256 ../../data/lsat7_2002_nir.tiff outputs/lsat7-256-block.tiff

    Creating output file that is 1287P x 831L.
    Processing input file ../../data/lsat7_2002_nir.tiff.
    0...10...20...30...40...50...60...70...80...90...100 - done.

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

Následující příklad počítá stejně jako předchozí příklad NDVI, tentokrát ale
bude postupovat po blocích (čtení i zápis)


.. literalinclude:: ../../_static/skripty/rasterio-ndvi-windows.py
   :language: python
