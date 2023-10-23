Příklad vytvoření nové vrstvy
-----------------------------

Následující příklad ukazuje přístup k vektorovým datům *od A do Z*,
tedy vytvoření nové datové vrstvy, nastavení metadat, vytvoření a
zápis nového geoprvku, uložení změn do souboru. To celé by šlo vykonat
pomocí výše zmíněné knihovny :ref:`Fiona <fiona>` několikanásobně
jednodušeji. OGR přistupuje k datům na nižší úrovni, což může být
někdy výhodnější.

.. literalinclude:: ../../_static/skripty/ogr-zapis.py
   :language: python
   :lines: 1-31

Výsledek zkontrolujeme:

.. literalinclude:: ../../_static/skripty/ogr-zapis.py
   :language: python
   :lines: 34-37

::

   1
