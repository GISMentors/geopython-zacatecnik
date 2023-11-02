Knihovna PDAL a Python
======================

Knihovna PDAL podporuje jazyk Python ve dvou způsobech použití:

1. umožňuje vytvořit skript v jazyku Python, který pracuje s daty
   pomocí ``filters.python``
2. nabízí rozšíření, které je možné integrovat v aplikacích
   napsaných v jazyku Python

.. important:: Data knihovna PDAL poskytuje jako NumPy pole.

               
Dokumentace: https://pdal.io/en/2.6.0/python.html

1. filters.python
-----------------

Tímto způsobem lze vestavět Python funkce do zpracování dat sekvencí operací
(tzv. `Pipelines <https://pdal.io/en/2.6.0/pipeline.html#pipeline>`__)
bez znalosti jazyka C++ (ve kterém je PDAL implementován), které
umožňují modifikovat mračna bodů ve formě NumPy polí.

.. note:: Pipeline je reprezentována v knihovně PDAL :wikipedia:`JSON`
          datovou strukturou.
          
Funkce musí mít dva argumenty datového typu NumPy polí: (1) mračno
bodů před aplikací ``filters.python`` a (2) mračno bodů po aplikaci
filru. Příklad funkce:

.. literalinclude:: ../../_static/skripty/multiply_z.py
   :language: python

V případě úspěšné operace musí funkce vratit hodnotu ``True``. Pokud
by funkce vratila hodnotu ``False`` tak by pipeline
skončil chybou.

Příklad pipeline:

.. literalinclude:: ../../_static/skripty/pdal-pipeline.json
   :language: json

Více ukázek najdete v dokumentaci `filters.python
<https://pdal.io/en/2.6.0/stages/filters.python.html#filters-python>`__.

Příklad spuštění pipeline z příkazové řádky (pod Windows použijte
*OSGeo4W Shell*):

.. code-block:: bash

   pdal pipeline ./pdal-pipeline.json

.. note:: Je nutné doinstalovat balíček ``pdal-plugins``

   .. code-block:: bash

      python3 -m pip install pip pdal-plugins
   
2. Rozšíření
------------

Pomocí rozšíření lze spouštět pipeline přímo v Python skriptu a
zpracovat výsledky zpracování dat dále v podobě NumPy polí. Příklad:

.. literalinclude:: ../../_static/skripty/pdal-pipeline.py
   :language: python
