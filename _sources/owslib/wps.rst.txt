.. _OWSLibWPS:

OGC WPS
-------

.. index::
    single: WPS
    single: OGC OWS

Služba `OGC Web Processing Service
<http://opengeospatial.org/standards/wps>`__ umožňuje spuštění
výpočetního nástoje na vzdáleném serveru.

.. note::

   Více informací na :skoleni:`školení Úvod do GIS
   <open-source-gis/standardy/ogc/wps.html>`.

Přípojíme se k výpočetní službě a vypíšeme její typ:

.. literalinclude:: ../_static/skripty/owslib-wps-example.py
   :language: python
   :lines: 1-4

Vypíšeme seznam výpočetních nástrojů, které služba poskytuje:

.. literalinclude:: ../_static/skripty/owslib-wps-example.py
   :language: python
   :lines: 7-8 

Vybeme nástroj s identifikátorem:

.. literalinclude:: ../_static/skripty/owslib-wps-example.py
   :language: python
   :lines: 10

Vyplníme seznam vstupních parametrů nástroje:

.. literalinclude:: ../_static/skripty/owslib-wps-example.py
   :language: python
   :lines: 12-18

Výpočet spustíme:

.. literalinclude:: ../_static/skripty/owslib-wps-example.py
   :language: python
   :lines: 20

Výsledek (v našem případě CSV soubor) uložíme na disk:

.. literalinclude:: ../_static/skripty/owslib-wps-example.py
   :language: python
   :lines: 21-22
