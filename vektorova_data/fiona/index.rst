.. _fiona:

Knihovna Fiona
==============

`Knihovna Fiona <http://toblerity.org/fiona/>`_ jako nadstavba nad
knihovnou *OGR* (součást knihovny `GDAL <http://gdal.org>`__)
představuje objektově orientovaný způsob práce s vektorovými
daty. Načtená vektorová data knihovna přemapovává do datové struktury
:wikipedia-en:`GeoJSON` a stejné struktury zapisuje zpět do výstupních
souborů. Uživatel se nemusí zabývat kurzory, vrstvami, geometrickými
operacemi a dalšími *odbornými* termíny.

Fiona **není** nástroj vhodný na **všechny** operace - jednoduchost práce
je vykoupena poněkud pomalejším během kódu a omezením velikosti
zpracovávaných dat.  Tam kde OGR používá pointery, Fiona zkopíruje
vektorová data do objektů jazyka Python, což samozřejmě vede k
intenzivnějšímu využívání paměti. Pokud potřebujete filtrovat
geoprvky, knihovna OGR je asi vhodnější. Pokud potřebujete zpracovat
postupně všechny geoprvky ve vrstvě, měla by být rychlejší Fiona.

.. note::
   
   Pro práci s daty ve formátu (Geo)JSON můžete použít knihovnu jazyka
   Python ``json``. Pokud budete pracovat s daty uloženými v
   databázích je vhodnější použít jejich vlastní knihovny.

Knihovna Fiona se stará o manipulaci atributových dat a správu souborů. Pro
práci s geometriemi je potřeba data "dostat" do knihovny `shapely`, o které je
další část tohoto tutoriálu.

.. note:: Jak se projeví nově postavěná dálnice na území CHKO České středohoří?

        Vytvořte mapu území v CHKO České středohoří, které bude zasaženo novou
        dálnicí D8 z Prahy do Drážďan.

        Jako vstupní data použijte:

        * Mapu velkoplošných chráněných území z `AOPK <http://www.ochranaprirody.cz/>`_
        * Mapu dálnic z datasetu `OpenStreetMap <http://openstreetmap.org>`_

.. toctree::
   :maxdepth: 2

   data_source
   cteni_prvku
   geometrie
   highway_over_protected_area

