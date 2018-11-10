Procházení geoprvků
-------------------

V této části si ukážeme, jak načíst vektorové prvky uložené v  datovém zdroji.

Nejprve dataset otevřeme

.. code-block:: python

    import fiona
    chko = fiona.open("data/chko.shp")


Nyní můžeme zjistit, kolik prvků je v datasetu obsaženo

.. code-block:: python

    print("Počet prvků: ", len(chko))

Sekvenční zpracování prvků
^^^^^^^^^^^^^^^^^^^^^^^^^^

Prvky v datovém souboru můžeme procházet postupně (sekvenčně):

.. literalinclude:: ../../_static/skripty/fiona-example.py
   :language: python
   :lines: 19-20

anebo si vybrat některý z geoprvků (náhodný přístup) a dále s ním
pracovat:

.. literalinclude:: ../../_static/skripty/fiona-example.py
   :language: python
   :lines: 22

.. note:: Vyfiltrujte prvky podle vlastnosti

    Vyfiltruje všechna chráněná území, která se nacházejí v Českém středohoří.
    O kolik prvků se jedná?

