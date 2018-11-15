Komplexní příklad přístupu k datům RÚIAN
----------------------------------------

Tato kapitola prezentuje příklad použití knihovny GDAL pro čtení
online dat z *Registru územní identifikace, adres a nemovitostí*
(`RÚIAN <http://ruian.cz>`__) dostupných v rámci `Veřejného dálkové
přístupu <http://vdp.cuzk.cz>`__.

Pro zadanou obec (řádek :lcode:`8`) skript vypíše informace o
parcelách (parcelní číslo, výměru uloženou v atributech a vypočtenou z
geometrie). Parcely, u kterých je rozdíl výměr větší než tolerance
(řádek :lcode:`5`), uloží do nové vrstvy ve formátu Esri Shapefile do
aktuálního adresáře (řádek :lcode:`27`).

.. literalinclude:: ../../_static/skripty/gdal-ruian.py
   :language: python
   :linenos:
   :emphasize-lines: 5, 8, 27

.. note:: Skript ke stažení `zde <../../_static/skripty/gdal-ruian.py>`_.

.. tip:: Pro efektivní práci s daty RÚIAN existuje speciální knihovna
         `GDAL-VFR <https://github.com/ctu-geoforall-lab/gdal-vfr>`__
         a její konzolové nastroje, viz `dokumentace
         <http://freegis.fsv.cvut.cz/gwiki/RUIAN_/_GDAL#VFR_konverzn.C3.AD_skripty>`__.
         
