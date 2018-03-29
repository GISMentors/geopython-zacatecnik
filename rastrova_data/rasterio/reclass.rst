.. _rasterio-reklasifikace:

Reklasifikace
-------------

Reklasifikace je proces nahrazení hodnot pixelů vstupní mapy novými
hodnotami na základě reklasifikačních pravidel.

V našem případu reklasifikujeme rastrovou mapu NDVI, kterou jsme
vytvořili v předchozím kapitole :ref:`ndvi-algebra`.

Rozdělíme NDVI do tříd podle jejich hodnoty. NDVI nabývá hodnot od -1
do 1, rozdělíme je na 3 skupiny "od oka":

.. cssclass:: border

+---+----------------+---------------+
| 1 | Vegetace       | 1 - 0.3       |
+---+----------------+---------------+
| 2 | Suchá půda     | 0.3 - -0.35   |
+---+----------------+---------------+
| 3 | Voda           | -0.35 - -1    |
+---+----------------+---------------+

.. literalinclude:: ../../_static/skripty/rasterio-reclass.py
   :language: python

Výsledný soubor obsahuje pouze 3 hodnoty reprezentující jednotlivé
třídy.

.. figure:: ../images/ndvi-classes.png
    
    Výsledný soubor se třemi třídami.
