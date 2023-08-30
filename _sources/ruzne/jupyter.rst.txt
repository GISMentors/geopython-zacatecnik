Jupyter notebook
================

`Jupyter <http://jupyter.org/>`_ je webová aplikace, která vám umožní vytvářet
dokumenty, které obsahují kód programu, vizualizace, formátovaný text - vše v
jednom.

Pokud si chcete hrát s nějakou Python knihovnou, je Jupyter skvělá
volba - můžete si kód hned popisovat, vracet se k jeho jednotlivým
částem, měnit jej a sledovat změny chování.

.. figure:: images/jupyter.png
   :class: middle
           
Jak zobrazit rastrová data numpy
--------------------------------

Použít můžeme například knihovnu Matplotlib

.. code-block:: python

    import rasterio
    from matplotlib import pyplot
    with rasterio.open("/data/data/lsat7_2002_nir.tiff") as src:
         pyplot.imshow(src.read(1), cmap='pink')
         pyplot.show()

anebo funkci ``rasterio.plot.show`` funkci, která umí navíc pracovat
se třemi kanály a ještě zobrazí správné geografické souřadnice.

.. code-block:: python

    import rasterio
    from rasterio.plot import show
    with rasterio.open("/data/data/lsat7_2002_nir.tiff") as src:
        show(src.read(), transform=src.transform)

Dále můžeme zobrazit i `více kanálů vedle sebe nebo třeba histogram
<https://rasterio.readthedocs.io/en/latest/topics/plotting.html?highlight=plotting>`__.


Jak zobrazit vektorová data
---------------------------

Objekty typu ``shapely.geometry.BaseGeometry`` lze zobrazit přímo
jejich vypsáním:

.. code-block:: python
                
    import shapely
    import shapely.geometry
    geom = shapely.geometry.LineString([(0, 0), (1, 1), (1,2), (2,2)])

    geom

.. figure:: images/shapely-screen.png
   :class: middle
           
Docker kontejner
----------------

Technologie `Docker <https://www.docker.com/>`__ nám umožní
nakonfigurovat prostředí a spustit jej v samostaném "kontejneru" bez
nutnosti instalovat cokoliv (kromě samotného Dockeru) na hostitelský
systém.

.. note:: Pokud vám tento krok připadá příliš komplikovaný, nic se neděje,
        můžete pokračovat za použití ``virtualenv`` nebo instalací potřebných
        závislostí na váš domácí systém.


Pro účely tohoto kurzu jsme `připravili Docker image <https://github.com/GISMentors/geopython-docker>`_, který můžete stáhnout ze stránek `Docker hub <https://hub.docker.com/r/opengeolabs/gismentors/>`_ příkazem::

    docker pull opengeolabs/gismentors:geopython

A následně ho můžete pustit příkazem::

    docker run -p 8888:8888 \
           -v $(pwd):/localdata/ \
           --rm --name geopython-workshop \
           opengeolabs/gismentors:geopython

Potom už stačí jenom otevřít prohlížeč na adresse `http://localhost:8888/
<http://localhost:8888>`_, zadat heslo ``geopython`` a máte před sebou kompletně
připravený Jupyter notebook s nainstalovanými závislostmi potřenými pro tento
workshop.

Uložená data
~~~~~~~~~~~~

Data jsou dostupná v adresáři :file:`/data/data`. Adresář pro výstupy
můžete založit v adresáři :file:`/outputs/`.

