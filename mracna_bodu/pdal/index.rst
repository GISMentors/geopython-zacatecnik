Knihovna PDAL a Python
======================

Knihovna PDAL podporuje jazyk Python ve dvou způsobech použití:

1. Umožňuje vytvořit skript v jazyku Python, který pracuje s daty
pomocí ``filters.python``

2. PDAL nabízí rozšíření, které je možné integrovat v aplikacích napsaných v jazyku Python

.. important:: Data knihovna PDAL poskytuje jako Numpy pole.

Skript pro filters.python
-------------------------

Lze vestavět Python funkce do procesních operací (tzv. `Pipelines
<https://pdal.io/en/2.6.0/pipeline.html#pipeline>`__) bez znalosti
jazyka C++ (ve kterém je PDAL implementován), které umožňují
modifikovat mračna bodů ve formě Numpy polí.

Funkce musí mít dva argumenty Numpy polí: body před aplikací
``filters.python`` a body po aplikaci filru. Příklad funkce:

.. literalinclude:: ../../_static/skripty/multiply_z.py
   :language: python

V případě úspěšné operace musí funkce vratit hodnotu ``True``. Pokud by funkce vratila hodnotu ``False`` tak by pracovní proces (pipeline) skončil chybou.

Příklad pracovního procesu:

.. literalinclude:: ../../_static/skripty/pdal-pipeline.json
   :language: json

Více ukázek najdete v dokumentace `filters.python
<https://pdal.io/en/2.6.0/stages/filters.python.html#filters-python>`__.

Rozšíření
---------

Dokumentace: https://pdal.io/en/2.6.0/python.html
