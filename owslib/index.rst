Načítání dat pomocí webových služeb OGC
#######################################

`Open Geospatial Consortium <http://opengeospatial.org>`_ (OGC) je mezinárodní
standardizační organizace. Její členové se zabývají vývojem a údržbou standardů
pro prostorová data a služby. Mezi nejznámnější OGC standardy patří formát `Geography
Markup Language <http://opengeospatial.org/standards/gml>`_, `Keyhole Markup
Language <http://opengeospatial.org/stanards/kml>`_ a tzv. *Otevřené webové
služby* (OGC OWS), mezi které patří `Web Mapping Service (OGC WMS)
<http://opengeospatial.org/standards/wms>`_, `Web Feature Service (OGC WFS)
<http://opengeospatial.org/standards/wfs>`_, `Web Coveradge Service (OGC WCS)
<http://opengeospatial.org/standards/wcs>`_ a další.

Standardy OGC OWS jsou postaveny na komunikaci mezi serverem a
klientem (:wikipedia:`client-server protocol <Klient-server>`), kdy
klient (váš počítač) posílá serveru (počítači, ze kterého chcete
získat data či na něm spusit službu) požadavky. Server odpovídá
prostřednictvím souboru ve formátu XML. Požadavek může mít buď podobu
speciálního URL, kdy jednotlivé paramery jsou od sebe odděleny znakem
``&``, například::

    http://server/sluzba?request=GetCapabilies&service=WMS

V tomto případě posíláme 2 parametry: ``request`` má hodnotu
``GetCapabilities`` a parametr ``service`` má hodnotu ``WMS``.

Další možností je poslat serveru požadavek jako soubor ve formátu XML,
například:

.. code-block:: xml
   
   <wps:GetCapabilities xmlns:wps="http://www.opengis.net/wps/1.0.0" ...>
        <ows:Identifier>Buffer</ows:Identifier>
   </wps:Execute> 

Práce s těmito dotazy a zpracovávání odpovědí může být komplikovaná. Jednotlivé
zápisy se liší každou verzi standardů. Také proto vznikla knihovna *OWSLib*, která
život programátorů značně usnadňuje.

OWSLib
======

Knihovna `OWSLib <http://geopython.github.io/OWSLib/>`_ je Python
rozhraní pro otevřené webové služby *OGC OWS*. Knihovna umožňuje se
připojit k různým službám a pracovat s nimi z pozice *klienta* a to
bez ohledu na serverovou implementaci. Knihovna momentálně podporuje
standardy WMS, WFS, WCS, CSW, WPS, SOS, WMC a další (seznam se stále
rozšiřuje). 

Dokumentace: http://geopython.github.io/OWSLib/

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
<http://cenia.cz>`_ udržován `Národní geoportál INSPIRE
<http://geoportal.gov.cz>`_, který obsahuje informace o všech
dostupných webových službách a datových souborech poskytovaných
veřejnou správnou. Umožňuje v nich vyhledávat pomocí stanardu `OGC CSW
<http://opengeospatial.org/standards/csw>`_.

Webové rozhraní k tomuto serveru najdete na adrese
http://geoportal.gov.cz/web/guest/catalogue-client. Rozhraní pro webovou službu
je dostupné na adrese http://geoportal.gov.cz/php/micka/csw/index.php.

.. literalinclude:: ../_static/skripty/owslib-example.py
   :language: python
   :lines: 1-3

.. code-block:: python

    'CSW'

Vyhledávání záznamů:

.. literalinclude:: ../_static/skripty/owslib-example.py
   :language: python
   :lines: 5-6

.. code-block:: python

    {'matches': 2621, 'nextrecord': 11, 'returned': 10}

Zjištění hodnot nalezených záznamů:

.. literalinclude:: ../_static/skripty/owslib-example.py
   :language: python
   :lines: 8-9

.. code-block:: python

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

Vyhledávání s omezením na záznamy obsahující slovo *WMS* a minimální
ohraničující obdélník Prahy:

.. literalinclude:: ../_static/skripty/owslib-example.py
   :language: python
   :lines: 11-16

.. code-block:: python

    {'matches': 113, 'nextrecord': 11, 'returned': 10}

.. literalinclude:: ../_static/skripty/owslib-example.py
   :language: python
   :lines: 18-21

.. code-block:: python           

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
    >>>

Vlastnosti záznamu:

.. literalinclude:: ../_static/skripty/owslib-example.py
   :language: python
   :lines: 23-26

.. code-block:: python

    'service'

.. literalinclude:: ../_static/skripty/owslib-example.py
   :language: python
   :lines: 28
    
.. code-block:: python
    
    Prohlížecí služba WMS - ZM 10
    Prohlížecí služba WMS-ZM10-P je poskytována jako veřejná prohlížecí
    služba nad daty Základní mapy ČR 1:10 000.  Služba splňuje Technické
    pokyny pro INSPIRE prohlížecí služby v. 3.11 a zároveň splňuje
    standard OGC WMS 1.1.1. a 1.3.0.

.. literalinclude:: ../_static/skripty/owslib-example.py
   :language: python
   :lines: 30
                
.. code-block:: python
                
    'http://geoportal.cuzk.cz/WMS_ZM10_PUB/WMService.aspx?service=WMS&request=getCapabilities'

.. _OWSLibWMS:

OGC WMS
-------

.. index::
    single: WMS
    single: OGC OWS

`OGC Web Map Service <http://opengeospatial.org/standards/wms>`_ slouží ke
stahování a sdílení mapových dat. Ke klientovi nejsou posílána vlastní data, ale
pouze náhled (obrázek) těchto dat.

.. note::

   Více informací na :skoleni:`školení Úvod do GIS
   <open-source-gis/standardy/ogc/wms.html>`.

.. literalinclude:: ../_static/skripty/owslib-wms-example.py
   :language: python
   :lines: 1,3-7
   
.. code-block:: python

    Prohlížecí služba WMS - ZM 10
    Prohlížecí služba WMS-ZM10-P je poskytována jako veřejná prohlížecí
    služba nad daty Základní mapy ČR 1:10 000.
    Zeměměřický úřad
    Pod Sídlištěm 9

Dostupné mapové vrstvy:

.. literalinclude:: ../_static/skripty/owslib-wms-example.py
   :language: python
   :lines: 9

.. code-block:: python

    {'GR_ZM10': <owslib.wms.ContentMetadata instance at 0x7f1d7bc1b8c0>}

Rozsah vrstvy:

.. literalinclude:: ../_static/skripty/owslib-wms-example.py
   :language: python
   :lines: 11-13

.. code-block:: python
   
    (-950003.175021186, -1250003.1750036045, -399990.474995786, -899996.8249909044, 'EPSG:5514')
    (11.214011580382529, 47.96491460125967, 19.40766262309513, 51.691664934538636)

Stažení a uložení dat:

.. literalinclude:: ../_static/skripty/owslib-wms-example.py
   :language: python
   :lines: 14-23

.. important:: Možné problémy při připojení ke službě. V minulosti končilo připojení chybou
          ``requests.exceptions.TooManyRedirects: Exceeded 30
          redirects.`` Vysvětlení hledejte na našem `blogu <http://gismentors.cz/blog/user-agent-hlavicka-requestu-na-wms-server/>`__.
          
.. task:: Vyzkoušejte připojení ke službě:

          .. code-block:: python

             url='http://gis.nature.cz/arcgis/services/UzemniOchrana/Natura2000/MapServer/WmsServer'
             layer='1' # Evropsky významné lokality (EVL)


          Výše zmíněna služba AOPK podporuje pouze WMS verze
          1.3.0. Vzhledem k tomu, že OWSLib používá ve výchozím
          nastavení verzi služby 1.1.1, je třeba verzi vynutit:

          .. code-block:: python

             wms = WebMapService(url, version='1.3.0')

.. _OWSLibWFS:

OGC WFS
-------

.. index::
    single: WFS
    single: OGC OWS

Služba `OGC Web Feature Service <http://opengeospatial.org/standards/wfs>`_ slouží ke
stahování a sdílení vektorových dat. Nejčastějším výměnným formátem je `OGC GML
<http://opengeospatial.org/standards/gml>`_.

.. note:: Předpokládáme, že máme naimportováno vše potřebné pro práci s
    katalogovou službou, pokud ne, vraťte se prosím výše, viz :ref:`OWSLibCSW`.

Nejprve najdeme nějaké WFS v katalogové službě:

.. literalinclude:: ../_static/skripty/owslib-example.py
   :language: python
   :lines: 32-37

.. code-block:: python

    {'matches': 6, 'nextrecord': 0, 'returned': 6}

.. literalinclude:: ../_static/skripty/owslib-example.py
   :language: python
   :lines: 39-41

.. code-block:: python

    ... 
    53e37222-89a0-472b-9781-5bfc0a02080a WFS Soustava území Natura 2000
    53e37cd6-5cb8-4ee9-b862-62e10a02080a WFS Památné stromy
    5473579f-fb08-48ab-893d-3d3e0a02080a WFS Chráněná území
    54735935-a88c-4c58-99bc-3dee0a02080a WFS Mezinárodní ochrana přírody
    53e47f1f-1bb8-405f-9254-514a0a02080a WFS Údaje o území
    53f3708e-9d1c-4da6-983c-086e0a02080a WFS Průchodnost krajiny pro velké savce


Podíváme se, jaká data mají v `Agentuře ochrany přírody a krajiny
<http://www.ochranaprirody.cz/>`_ (AOPK):

.. literalinclude:: ../_static/skripty/owslib-example.py
   :language: python
   :lines: 43-44

.. code-block:: python

    Služba zpřístupňuje geografická data soustavy území Natura 2000 v České republice; © AOPK ČR
    https://gis.nature.cz/arcgis/services/UzemniOchrana/Natura2000/MapServer/
    WFSServer?service=WFS&request=GetCapabilities&version=1.1.0

Načteme WFS AOPK:

.. literalinclude:: ../_static/skripty/owslib-wfs-example.py
   :language: python
   :lines: 2-5

Zjistíme vlastnosti služby (Capabilities):

.. literalinclude:: ../_static/skripty/owslib-wfs-example.py
   :language: python
   :lines: 7-8

.. code-block:: python

    'https://gis.nature.cz/arcgis/services/UzemniOchrana/Natura2000/MapServer/WFSServer?service=WFS&request=GetCapabilities&version=1.1.0'

.. literalinclude:: ../_static/skripty/owslib-wfs-example.py
   :language: python
   :lines: 10-14

.. code-block:: python

    Agentura ochrany přírody a krajiny České republiky
    Soustava chránených území evropského významu Natura 2000
    Natura 2000, Chráněné území
    žádné
    Služba zpřístupňuje geografická data soustavy chránených území evropského významu Natura 2000 v České republice

Metadata
""""""""

.. literalinclude:: ../_static/skripty/owslib-wfs-example.py
   :language: python
   :lines: 16-17

.. code-block:: python

    ...
    UzemniOchrana_Natura2000:Ptačí_oblast
    UzemniOchrana_Natura2000:Forma_ochrany_EVL_-_stav_k_24._5._2013
    UzemniOchrana_Natura2000:Evropsky_významná_lokalita__EVL_

Načteme ještě službu chránených území

.. literalinclude:: ../_static/skripty/owslib-wfs-example.py
   :language: python
   :lines: 19-22

.. code-block:: python
    
    ... 
    UzemniOchrana_ChranUzemi:Maloploplošná_zvláště_chránená_oblast
    UzemniOchrana_ChranUzemi:Smluvní_chránené_území
    UzemniOchrana_ChranUzemi:Zákonem_chránené_pásmo_MZCHU
    UzemniOchrana_ChranUzemi:Velkoplošné_zvláště_chránené_území
    UzemniOchrana_ChranUzemi:Zonace_velkoplošného_zvláště_chráneného_území

.. literalinclude:: ../_static/skripty/owslib-wfs-example.py
   :language: python
   :lines: 24-25

.. code-block:: python

   <owslib.feature.wfs100.ContentMetadata instance at 0x7f90a1ec3e60>

.. literalinclude:: ../_static/skripty/owslib-wfs-example.py
   :language: python
   :lines: 27-28

.. code-block:: python

    (12.13496541407338, 48.40534103216736, 18.82327290073213, 51.27775263472881, urn:ogc:def:crs:EPSG::5514)
    [urn:ogc:def:crs:EPSG::5514]

Data
""""

.. literalinclude:: ../_static/skripty/owslib-wfs-example.py
   :language: python
   :lines: 30-33

.. code-block:: python

   <owslib.util.ResponseWrapper object at 0x7f697152df90>

.. literalinclude:: ../_static/skripty/owslib-wfs-example.py
   :language: python
   :lines: 35

.. code-block:: python
                
    <wfs:FeatureCollection xsi:schemaLocation='https:gis.nature.cz:6443/arcgis/services/UzemniOchrana/Ch...

VUV
"""

.. literalinclude:: ../_static/skripty/owslib-wfs-example.py
   :language: python
   :lines: 45-51

.. code-block:: python
                
    <wfs:FeatureCollection xsi:schemaLocation='...

CUZK WFS
""""""""

.. todo:: Nutnost autentizace pro kraj.read()

.. literalinclude:: ../_static/skripty/owslib-wfs-example.py
   :language: python
   :lines: 37-40

.. code-block:: python

    ...
    gmgml:OKRES
    gmgml:KRAJ
    gmgml:OBLAST
    gmgml:MC
    gmgml:OPU
    gmgml:KU
    gmgml:ZSJ
    gmgml:SO
    gmgml:STAT
    gmgml:ORP
    gmgml:OBEC

.. literalinclude:: ../_static/skripty/owslib-wfs-example.py
   :language: python
   :lines: 42-43

.. code-block:: python
                    
   <gmgml:FeatureCollection xsi:schemaLocation="http://www.intergraph.com/geomedia/gml http://geopor....
