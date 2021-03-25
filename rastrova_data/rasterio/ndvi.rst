.. _algebra:
.. _ndvi:

*******************************
Rastrová algebra - výpočet NDVI
*******************************

=================
Rasterová algebra
=================

Nástroj srovnatelný s topologickými překryvnými operacemi vektorových dat.
Umožňuje kombinovat rastrové vrstvy pomocí různých matematických operací.
Tyto matematické operace se vykonávají buď na jedné nebo více
vrstvách a jejich výstupem je vrstva nová. Rastrová algebra se často používá pro
prostorové modelování a analýzu.

Operátory jsou obvyklé matematické, statistické, relační a logické operátory (+,
-, \*, /, >, <, >=, <=, <>, mod, div, and, or, not, ...).

Funkce se dělí na:

    *Lokální*
        na individuální buňce, nová hodnota vzniká z jedné rastrové buňky jedné nebo více vrstev.
    *Fokální*
        v definovaném okolí, nová hodnota vzniká z definovaného okolí buňky
        (např. jako výsledek operace nad "oknem" 3x3 pixely)
    *Zonální*
        na specifické oblasti, nová hodnota vzniká ze zóny definované v jiné vrstvě.
    *Globální*
        používají se všechny buňky informační vrstvy (např. analýzy povrchů).

Jak již bylo uvedeno, tak Rasterio využívá pro uložení dat strukturu
`NumPy <http://www.numpy.org/>`__, což nám umožňuje s těmito datovými
strukturami pracovat standardním způsobem a využívat i pokročilé
nástroje pro analýzu obrazu, jako je `Sciktit Image
<http://scikit-image.org/>`__, `Matplot lib
<https://matplotlib.org/stable/tutorials/introductory/images.html#sphx-glr-tutorials-introductory-images-py>`__,
`OpenCV
<https://docs.opencv.org/3.0-last-rst/doc/py_tutorials/py_tutorials.html>`__
a další.

V našem příkladu si ukážeme jednoduchou analýzu - výpočet indexu NDVI ze
satelitních dat.

====
NDVI
====

:wikipedia-en:`Normalizovaný vegetační index
<Normalized_difference_vegetation_index>` je jednoduchý grafický
indikátor, který ukazuje na přítomnost zelené vegetace v daném objektu
(snímku). Tento index se obyčejně, ale nikoliv výhradně, používá pro
zpracování satelitních dat.

 .. figure:: ../images/ndvi-graph.png

        Graf absorbce červeného a infračerveného spektra, zdroj
        `Wikipedia NDVI
        <https://en.wikipedia.org/wiki/Normalized_difference_vegetation_index#/media/File:Par_action_spectrum.gif>`_

Chlorofyl zelených rostlin absorbuje červené světlo (od 0.4 do 0.7 µm).
Buněčná struktura naopak odráží infračervené spektrum (od 0.7 do 1.1 µm). Index
NDVI spočítáme jako poměr těchto dvou spekter::

        NDVI=(NIR−RED)/(NIR+RED)

kde
        * NIR - near-infrared (Band 8)
        * RED - red (Band 4)

Index NDVI nabývá hodnot mezi -1 a +1.  Obecně lze říci, že čím více odraženého
světla v infračerveném spektru v poměru k červené barvě, tím více je v daném
pixelu přítomna hustá zelená vegetace, jako například les.

Hustá vegetace bude nabývat relativně vysoké pozitivní hodnoty (0.3 až 0.8),
mraky a sníh budou mít negativní hodnoty indexu. Volně stojící voda (oceány,
jezera, řeky), mají spíše nízkou odrazivost v obou spektrech, jejich hodnoty
se pohybují okolo 0 z obou stran. Půdy, které mají tendenci odrážet
infračervenou barvu o něco více než červenou mají nízké hodnoty NDVI (0.1-0.2)


 .. figure:: ../images/NDVI_102003.png

        Příklad mapy NDVI Britských ostrovů z družice  NOAA AVHRR). `Wikipedia
        NDVI Great Britain
        <https://en.wikipedia.org/wiki/Normalized_difference_vegetation_index#/media/File:NDVI_102003.png>`_

============
Výpočet NDVI
============

Výpočet s daty v NumPy provedeme už jednoduše (:lcode:`10`):

.. literalinclude:: ../../_static/skripty/rasterio-example.py
   :language: python
   :lines: 1-12
   :emphasize-lines: 10
   :linenos:

-----------------------
Zápis do nového souboru
-----------------------

Pro výstupní soubor musíme nejprve nadefinovat jeho parametry, jako je
rozlišení, datový typ, počet pixelů, souřadnicový systém. Většinu
údajů můžeme zkopírovat ze vstupního souboru (:lcode:`8`), a ty
rozdílné (v našem případě datový typ) přepíšeme (:lcode:`14`):

.. literalinclude:: ../../_static/skripty/rasterio-example.py
   :language: python
   :lines: 8-17
   :linenos:
   :emphasize-lines: 1, 7
   :lineno-start: 8

.. note:: Výsledný soubor můžete prohlédnout např. v QGIS nebo v
   Jupyter Notebooku:

   .. code-block:: python

      bit8_green = ((ndvi+1)*128).astype('uint8') # convert to 0-256 values
      PIL.Image.fromarray(bit8_green, "L")

.. figure:: ../images/ndvi.png
    
    Výsledný soubor s NDVI indexem.

.. task:: 
   Pokuste se podle stejného postupu vypočítat tzv. *Water
   index*. Jaké kanály použít najdete např. na
   :wikipedia-en:`wikipedii <Normalized difference water index>`.
