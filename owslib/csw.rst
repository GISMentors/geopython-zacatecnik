.. _OWSLibCSW:

OGC CSW
-------

.. index::
    single: CSW
    single: OGC OWS
    single: Cenia

Chceme-li nějakou OGC webovou službu začít využívat, musíme především
znát její adresu.  Také pro tento účel vznikají *katalogové služby*,
kdy specializované servery udržující metadatové záznamy webových
služeb a datových souborů. Pro Českou republiku je organizací `Cenia
<http://cenia.cz>`__ udržován `Národní geoportál INSPIRE
<http://geoportal.gov.cz>`__, který obsahuje informace o všech
dostupných webových službách a datových souborech poskytovaných
veřejnou správnou. Umožňuje v nich vyhledávat pomocí standardu
:skoleni:`OGC CSW <open-source-gis/standardy/ogc/csw.html>`.

Webové rozhraní k tomuto serveru najdete na adrese
http://geoportal.gov.cz/web/guest/catalogue-client. Rozhraní pro webovou službu
je dostupné na adrese http://geoportal.gov.cz/php/micka/csw/index.php.

.. literalinclude:: ../_static/skripty/owslib-csw-example.py
   :language: python
   :lines: 1-3

.. code-block:: python

    'CSW'

Vyhledávání záznamů:

.. literalinclude:: ../_static/skripty/owslib-csw-example.py
   :language: python
   :lines: 5-6

.. code-block:: python

    {'matches': 2621, 'nextrecord': 11, 'returned': 10}

Zjištění hodnot nalezených záznamů:

.. literalinclude:: ../_static/skripty/owslib-csw-example.py
   :language: python
   :lines: 8-9

.. code-block:: bash

    ...
    Olomouc
    Olomouc
    Dálniční exity GN
    Global Network - Jednotná georeferenční síť pozemních komunikací
    Železniční přejezd GN
    Kilometráž GN
    Osa železničních tratí
    Železniční tunely
    Železniční mosty a propustky
    Železniční přejezdy
    ...
    
Vyhledávání s omezením na záznamy obsahující slovo *WMS* a minimální
ohraničující obdélník Prahy:

.. literalinclude:: ../_static/skripty/owslib-csw-example.py
   :language: python
   :lines: 11-16

.. code-block:: python

    {'matches': 113, 'nextrecord': 11, 'returned': 10}

.. literalinclude:: ../_static/skripty/owslib-csw-example.py
   :language: python
   :lines: 18-22

.. code-block:: bash

    ...
    ÚP VÚC Adršpach: 48.20735042 11.86320935 51.37551609 19.0302868
    VÚC Hradecko-Pardubické aglomerace: 48.20735042 11.86320935 51.37551609 19.0302868
    ÚP VÚC okresu Jičín: 48.23303412 11.93768841 51.35407571 18.95542894
    ÚP VÚC Krkonoše: 48.20735042 11.86320935 51.37551609 19.0302868
    ÚP VÚC Orlické hory a podhůří: 48.20735042 11.86320935 51.37551609 19.0302868
    ÚP VÚC Trutnovsko - Náchodsko: 48.20735042 11.86320935 51.37551609 19.0302868
    Prognóza rozvoje území kraje: 48.20735042 11.86320935 51.37551609 19.0302868
    WMS služba Pardubického kraje - polohopis, ortofoto: 48.11130361 11.83822588 51.45351762 19.12784541
    Služba WMS Pardubického kraje - tematické vrstvy: 48.22866996 12.03230308 51.34271802 19.63025648
    Prohlížecí služba WMS - Data200: 48.55 12.09 51.06 18.86
    ...

Vyhledání služby obsahující v názvu "ZM10":

.. literalinclude:: ../_static/skripty/owslib-csw-example.py
   :language: python
   :lines: 24-27

.. code-block:: python

    'service'

.. literalinclude:: ../_static/skripty/owslib-csw-example.py
   :language: python
   :lines: 29
    
.. code-block:: python
    
    Prohlížecí služba WMS - ZM 10
    Prohlížecí služba WMS-ZM10-P je poskytována jako veřejná prohlížecí
    služba nad daty Základní mapy ČR 1:10 000.  Služba splňuje Technické
    pokyny pro INSPIRE prohlížecí služby v. 3.11 a zároveň splňuje
    standard OGC WMS 1.1.1. a 1.3.0.

.. literalinclude:: ../_static/skripty/owslib-csw-example.py
   :language: python
   :lines: 31
                
.. code-block:: python
                
    'http://geoportal.cuzk.cz/WMS_ZM10_PUB/WMService.aspx?service=WMS&request=getCapabilities'
