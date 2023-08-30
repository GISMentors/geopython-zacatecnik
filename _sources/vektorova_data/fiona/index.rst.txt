.. _fiona:

Knihovna Fiona/Shapely
======================

`Knihovna Fiona <https://github.com/Toblerity/Fiona>`__ jako nadstavba
nad knihovnou *OGR* (součást knihovny `GDAL <http://gdal.org>`__)
představuje objektově orientovaný způsob práce s vektorovými
daty. Načtená vektorová data knihovna přemapovává do datové struktury
:wikipedia-en:`GeoJSON` a stejné struktury zapisuje zpět do výstupních
souborů. Uživatel se nemusí zabývat kurzory, vrstvami, geometrickými
operacemi a dalšími *odbornými* termíny.

Fiona **není** nástroj vhodný na **všechny** operace - jednoduchost
práce je vykoupena poněkud pomalejším během kódu a omezením velikosti
zpracovávaných dat.  Tam kde OGR používá pointery, Fiona zkopíruje
vektorová data do objektů jazyka Python, což samozřejmě vede k
intenzivnějšímu využívání paměti. Pokud potřebujete filtrovat
geoprvky, knihovna OGR je asi vhodnější. Pokud potřebujete zpracovat
postupně všechny geoprvky ve vrstvě (a máte dostatek operační paměti),
měla by být rychlejší Fiona. Fiona taktéž podporuje narozdíl od
"mateřské" knihovny OGR pouze omezený počet vektorových formátů.

.. note::
   
   Pro práci s daty ve formátu (Geo)JSON můžete použít knihovnu jazyka
   Python :python3:`json`. Pokud budete pracovat s daty uloženými v
   databázích je vhodnější použít jejich vlastní knihovny (jako
   např. :python3:`sqlite3`) či obecnější `GeoAlchemy
   <https://geoalchemy-2.readthedocs.io/en/latest/>`__.

Knihovna Fiona se stará o manipulaci atributových dat a správu
souborů. Pro práci s geometriemi je potřeba data "dostat" do knihovny
`Shapely <https://github.com/Toblerity/Shapely>`__, o které je další
část tohoto tutoriálu.

**Užitečné odkazy**

   * `dokumentace knihovny Fiona <https://fiona.readthedocs.io/en/latest/>`__
   * `dokumentace knihovny Shapely <https://shapely.readthedocs.io/en/latest/>`__
  
.. task::

   Jak se projeví nově postavená dálnice na území CHKO České středohoří?

   Vytvořte mapu území CHKO České středohoří, které bude zasaženo
   novou dálnicí D8 z Prahy do Drážďan.

   Jako vstupní data použijte (najdete v datové sadě pro školení
   :skoleni:`QGIS pro začátečníky <qgis-zacatecnik>`):

   * Vrstvu velkoplošných chráněných území z `AOPK <http://www.ochranaprirody.cz/>`__ (:file:`ochrana_uzemi/velkoplosna_uzemi`)
   * Vrstvu dálnic z datasetu `OpenStreetMap <http://openstreetmap.org>`__ (:file:`osm/silnice`; `typ = 1`)

.. toctree::
   :maxdepth: 2

   data_source
   cteni_prvku
   geometrie
   highway_over_protected_area
