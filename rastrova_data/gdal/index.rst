Knihovna GDAL
=============

Pro práci s rastrovými geodaty se "tradičně" používá knihovna `GDAL
<http://gdal.org>`__. Knihovna GDAL je nízkoúrovňová, přistupuje k
datům pokud možno efektivním způsobem. V současnosti knihovna GDAL
podporuje více než `140 rastrových GIS formátů
<http://gdal.org/formats_list.html>`__.

Datový model
------------

Koncept pro rastrová data do značné míry odpovídá přístupu k
:ref:`vektorovým datům <ogr-model>`:

* **Driver** - ovladač pro čtení a zápis dat
* **Datasource** - zdroj dat, ze kterého a do kterého se čte a zapisuje
* **RasterBand** - rastrový kanál. U něterých zdrojů dat je jenom jedno
  pásmo, ale může jich mít teoreticky neomezeně (např. u
  hyperspektrálních dat).

.. figure:: images/gdal-schema.png
   :class: middle
           
Mezi další důležité charakteristiky rastrových dat patří prostorové
rozlišení (velikost pixelu v mapových jednotkách) a jeho hraniční
souřadnice.

Užitečné odkazy:

* `Popis abstraktního modelu pro rastrová data
  <http://gdal.org/gdal_datamodel.html>`__
* `API <http://gdal.org/python/>`__
* `Cookbook
  <https://pcjericks.github.io/py-gdalogr-cookbook/raster_layers.html>`__


Příklad vytvoření nového souboru z matice hodnot
------------------------------------------------

V následující ukázce vytvoříme nový rastrový soubor a vyplníme ho maticí
hodnot. Výsledek uložíme do souboru ve formátu :wikipedia-en:`GeoTIFF`.

Nejprve nastavíme několik výchozích hodnot, velikost matice (mřížky),
tj. velikost pixelu, číselná hodnota pro ``nodata`` (žádná) data,
jméno výsledného souboru a extent (hraniční souřadnice) rastrových
dat.

.. code-block:: python

    >>> from osgeo import gdal, ogr, osr

    >>> # počet pixelů ve směru os x a y, a hodnota pro nodata
    >>> pixel_size = 20
    >>> NoData_value = -9999

    >>> # název výstupního souboru
    >>> raster_fn = 'test.tif'

    >>> # hraniční souřadnice mřížky
    >>> x_min, x_max, y_min, y_max = (0, 100, 0, 100)

V dalším kroku vypočteme prostorové rozlišení, velikost pixelu na
základně počtu pixelů ve směru os a rozsahu rastrových dat.

.. code-block:: python

    >>> # prostorové rozlišení
    >>> x_res = int((x_max - x_min) / pixel_size)
    >>> y_res = int((y_max - y_min) / pixel_size)

Nyní můžeme vytvořit *datový zdroj* pro rastrová data. Nejprve
vytvoříme instanci objektu `Driver` pro požadovaný formát a následně
prázdný rastrový soubor. Zde musíme specifikovat

* jméno výsledného souboru
* prostorové rozlišení ve směru os `x` a `y`
* počet pásem (kanálů)
* typ číselné hodnoty

Nakonec nastavíme transformační parametry, které jsou ve
stejném formátu v jakém bývají uloženy v tzv. *world file* souboru:

* souřadnice levého-horního rohu `x`
* rozlišení ve směru osy `x`
* naklonění osy `x`
* souřadnice levého-horního roku `y`
* rozlišení ve směru osy `y`
* naklonění osy `y`

.. code-block:: python

    >>> target_driver = gdal.GetDriverByName('GTiff')
    >>> target_ds = target_driver.Create(raster_fn, x_res, y_res, 1, gdal.GDT_Byte)
    >>> target_ds.SetGeoTransform((x_min, pixel_size, 0, y_max, 0, -pixel_size))

V dalším kroku zapíšeme data do vybraného pásma (číslování pásem
začíná hodnotou 1 a ne více obvyklou 0). Do připraveného rastrového
kanálu můžeme nyní zapsat hodnoty jako matici hodnot ve formátu
:wikipedia-en:`NumPy`.

.. code-block:: python

    >>> band = target_ds.GetRasterBand(1)
    >>> ...
    >>> import numpy as np
    >>> band.WriteArray(np.array([[0, 0, 0, 0, 0],
    ...                  [0, 10, 15, 10, 0],
    ...                  [0, 15, 25, 15, 0],
    ...                  [0, 10, 15, 10, 0],
    ...                  [0, 0, 0, 0, 0]]))

Dále definujeme pro data souřadnicový systém. Ten se nastavuje pomocí
zápisu ve formátu :wikipedia-en:`Well-known text` (WKT). Souřadnicový
systém definujeme pomocí kódu :wikipedia-en:`EPSG` a vyexportujeme
jako formátu WKT:

.. code-block:: python

    >>> outRasterSRS = osr.SpatialReference()
    >>> outRasterSRS.ImportFromEPSG(5514)
    >>> target_ds.SetProjection(outRasterSRS.ExportToWkt()) # !!! jiné než u vektorových dat

A nakonec uklidíme (pro jistotu) a uzavřeme zápis:

.. code-block:: python

    >>> band.FlushCache()

Rasterizace vektorových dat
---------------------------

Další ne zcela obvyklou operací může být převod vektorových dat do
rastrové reprezentace. Začátek je stejný jako v předchozím případě:

.. code-block:: python

    >>> from osgeo import gdal, ogr, osr
    >>> ...
    >>> # počet pixelů ve směru os x a y, a hodnota pro nodata
    >>> pixel_size = 50
    >>> NoData_value = -9999
    >>> ...
    >>> # název výstupního souboru
    >>> raster_fn = 'chko.tif'

Otevřeme vstupní vektorová data:

.. code-block:: python

    >>> # název vstupního vektorového souboru
    >>> vector_fn = 'chko.shp'
    >>> # otevření zdroje dat (DataSource)
    >>> source_ds = ogr.Open(vector_fn)
    >>> # načtení první vrstvy z datového zdroje            
    >>> source_layer = source_ds.GetLayer()

A nyní můžeme zjistit potřebné hraniční souřadnice vstupních geodat a
vytvořit tak cílový rastrový soubor:

.. code-block:: python

    >>> # získat hraniční souřadnice
    >>> x_min, x_max, y_min, y_max = source_layer.GetExtent()
    >>> ...
    >>> # vytvořit data source pro výstupní data
    >>> x_res = int((x_max - x_min) / pixel_size)
    >>> y_res = int((y_max - y_min) / pixel_size)
    >>> tiff_driver = gdal.GetDriverByName('GTiff')
    >>> target_ds = tiff_driver.Create(raster_fn, x_res, y_res, 3, gdal.GDT_Byte)
    >>> target_ds.SetGeoTransform((x_min, pixel_size, 0, y_max, 0, -pixel_size))

Zkopírujeme také informaci o souřadnicovém systému (S-JTSK
:epsg:`5514`) ze vstupního datové zdroje na výstup:

.. code-block:: python

    >>> outRasterSRS = osr.SpatialReference()
    >>> outRasterSRS.ImportFromEPSG(5514)
    >>> target_ds.SetProjection(outRasterSRS.ExportToWkt()) # !!! jiné než u vektorů

Zlatým hřebem tohoto příkladu je funkce ``RasterizeLayer()`` s
následujícími parametry:

* cílový datový zdroj
* rastrová pásma (kanály)
* zdrojová vektorová vrstva
* hodnoty pro jednotlivá pásma
* dodatečné parametry

.. code-block:: python

    >>> gdal.RasterizeLayer(target_ds,
        [1, 2, 3],
        source_layer,
        burn_values=[255,125,0],
        options=['ALL_TOUCHED=TRUE']) # žádné mezery okolo znaku '='
    >>> target_ds.FlushCache()

.. gdal.RasterizeLayer(dataset, [1], layer, options = ["ATTRIBUTE=KOD"])

Tato funkce vektorová data zrasterizuje a zapíše je do výstupního
rastrového souboru.

.. figure:: images/chko
           
   Výsledek rasterizace CHKO.

.. tip:: Porovnejte s příkladem pro knihovnu :ref:`Rasterio
   <rasterio-vectorise>`.
