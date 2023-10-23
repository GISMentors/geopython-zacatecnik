Procházení geoprvků
-------------------

V této části si ukážeme, jak načíst vektorové prvky uložené v datovém zdroji.

Nejprve dataset otevřeme

.. literalinclude:: ../../_static/skripty/fiona-example.py
   :language: python
   :lines: 1-3

Nyní můžeme zjistit, kolik prvků je v datasetu obsaženo

.. literalinclude:: ../../_static/skripty/fiona-example.py
   :language: python
   :lines: 37

Sekvenční čtení prvků
^^^^^^^^^^^^^^^^^^^^^

Prvky v datovém souboru můžeme procházet postupně (sekvenčně):

.. literalinclude:: ../../_static/skripty/fiona-example.py
   :language: python
   :lines: 39-40

Náhodné čtení prvků
^^^^^^^^^^^^^^^^^^^
           
Anebo si můžeme vybrat některý z geoprvků (náhodný přístup) a dále s
ním pracovat:

.. literalinclude:: ../../_static/skripty/fiona-example.py
   :language: python
   :lines: 43

----

.. task:: 

   Vyberte všechna chráněná území, která se nacházejí v Českém
   středohoří. O kolik prvků se jedná?
