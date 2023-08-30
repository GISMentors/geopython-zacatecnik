Načítání dat pomocí webových služeb OGC
#######################################

`Open Geospatial Consortium <http://opengeospatial.org>`_ (OGC) je
mezinárodní standardizační organizace. Její členové se zabývají
vývojem a údržbou standardů pro prostorová data a služby (viz
:skoleni:`školení Úvod do GIS
<open-source-gis/standardy/ogc/index.html>`). Mezi nejznámnější OGC
standardy patří formáty *Geography Markup Language* (:skoleni:`OGC GML
<open-source-gis/standardy/ogc/gml.html>`), *GeoPackage*
(:skoleni:`OGC GPKG <open-source-gis/standardy/ogc/gpkg.html>`) a
tzv. *Otevřené webové služby* (:skoleni:`OGC OWS
<open-source-gis/standardy/ogc/index.html#index-1>`), mezi které patří
*Web Mapping Service* (:skoleni:`OGC WMS
<open-source-gis/standardy/ogc/wms.html>`), *Web Feature
Service* (:skoleni:`OGC WFS <open-source-gis/standardy/ogc/wfs.html>`),
*Web Coverage Service* (:skoleni:`OGC WCS
<open-source-gis/standardy/ogc/wcs.html>`) a další.

Standardy OGC OWS jsou postaveny na komunikaci mezi serverem a
klientem (viz :skoleni:`školení Úvod do GIS
<open-source-gis/server/index.html>`), kdy klient (váš počítač) posílá
serveru (počítači, ze kterého chcete získat data či na něm spustit
službu) požadavky. Server odpovídá prostřednictvím souboru ve
formátu :wikipedia:`XML`. Požadavek může mít buď podobu speciálního URL, kdy
jednotlivé paramery jsou od sebe odděleny znakem ``&``, například::

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
zápisy se liší každou verzí standardů. Také proto vznikla knihovna *OWSLib*, která
život programátorů značně usnadňuje.

Knihovna `OWSLib <http://geopython.github.io/OWSLib/>`_ představuje
Python rozhraní pro otevřené webové služby *OGC OWS*. Knihovna
umožňuje se připojit k různým službám a pracovat s nimi z pozice
*klienta* a to bez ohledu na serverovou implementaci. Knihovna
momentálně podporuje standardy WMS, WFS, WCS, CSW, WPS, SOS, WMC a
další (seznam se stále rozšiřuje).

Dokumentace: http://geopython.github.io/OWSLib/


.. toctree::
   :maxdepth: 1

   csw
   wms
   wfs
   wps
