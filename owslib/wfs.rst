.. _OWSLibWFS:

OGC WFS
-------

.. index::
    single: WFS
    single: OGC OWS

Služba `OGC Web Feature Service
<http://opengeospatial.org/standards/wfs>`__ slouží ke stahování a
sdílení vektorových dat. Nejčastějším výměnným formátem je `OGC GML
<http://opengeospatial.org/standards/gml>`__.

.. note::

   Více informací na :skoleni:`školení Úvod do GIS
   <open-source-gis/standardy/ogc/wfs.html>`.

.. note:: Předpokládáme, že máme naimportováno vše potřebné pro práci
   s katalogovou službou, pokud ne, vraťte se prosím výše, viz
   :ref:`OWSLibCSW`.

Nejprve najdeme nějaké WFS v katalogové službě:

.. literalinclude:: ../_static/skripty/owslib-csw-example.py
   :language: python
   :lines: 33-38

.. code-block:: python

    {'matches': 9, 'nextrecord': 0, 'returned': 9}

.. literalinclude:: ../_static/skripty/owslib-csw-example.py
   :language: python
   :lines: 40-42

.. code-block:: bash

    ... 
    53e37222-89a0-472b-9781-5bfc0a02080a WFS Soustava území Natura 2000
    53e37cd6-5cb8-4ee9-b862-62e10a02080a WFS Památné stromy
    5473579f-fb08-48ab-893d-3d3e0a02080a WFS Chráněná území
    54735935-a88c-4c58-99bc-3dee0a02080a WFS Mezinárodní ochrana přírody
    53e47f1f-1bb8-405f-9254-514a0a02080a WFS Údaje o území
    53f3708e-9d1c-4da6-983c-086e0a02080a WFS Průchodnost krajiny pro velké savce
    ...


Podíváme se, jaká data mají v `Agentuře ochrany přírody a krajiny
<http://www.ochranaprirody.cz/>`_ (AOPK):

.. literalinclude:: ../_static/skripty/owslib-csw-example.py
   :language: python
   :lines: 44-45

.. code-block:: python

    Služba zpřístupňuje geografická data soustavy území Natura 2000 v České republice; © AOPK ČR
    https://gis.nature.cz/arcgis/services/UzemniOchrana/Natura2000/MapServer/
    WFSServer?service=WFS&request=GetCapabilities&version=1.1.0

Načteme WFS AOPK:

.. literalinclude:: ../_static/skripty/owslib-wfs-example.py
   :language: python
   :lines: 1-3

Zjistíme vlastnosti služby (Capabilities):

.. literalinclude:: ../_static/skripty/owslib-wfs-example.py
   :language: python
   :lines: 5-6

.. code-block:: python

    'https://gis.nature.cz/arcgis/services/UzemniOchrana/Natura2000/MapServer/WFSServer?service=WFS&request=GetCapabilities&version=1.1.0'

.. literalinclude:: ../_static/skripty/owslib-wfs-example.py
   :language: python
   :lines: 8-12

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
   :lines: 14-15

.. code-block:: python

    ...
    UzemniOchrana_Natura2000:Ptačí_oblast
    UzemniOchrana_Natura2000:Forma_ochrany_EVL_-_stav_k_24._5._2013
    UzemniOchrana_Natura2000:Evropsky_významná_lokalita__EVL_
    ..
    
Načteme ještě službu chránených území:

.. literalinclude:: ../_static/skripty/owslib-wfs-example.py
   :language: python
   :lines: 17-20

.. code-block:: python
    
    ... 
    UzemniOchrana_ChranUzemi:Maloploplošná_zvláště_chránená_oblast
    UzemniOchrana_ChranUzemi:Smluvní_chránené_území
    UzemniOchrana_ChranUzemi:Zákonem_chránené_pásmo_MZCHU
    UzemniOchrana_ChranUzemi:Velkoplošné_zvláště_chránené_území
    UzemniOchrana_ChranUzemi:Zonace_velkoplošného_zvláště_chráneného_území
    ...
    
.. literalinclude:: ../_static/skripty/owslib-wfs-example.py
   :language: python
   :lines: 22-23

.. code-block:: bash

   <owslib.feature.wfs100.ContentMetadata instance at 0x7f90a1ec3e60>

.. literalinclude:: ../_static/skripty/owslib-wfs-example.py
   :language: python
   :lines: 25-26

.. code-block:: bash

    (12.13496541407338, 48.40534103216736, 18.82327290073213, 51.27775263472881, urn:ogc:def:crs:EPSG::5514)
    [urn:ogc:def:crs:EPSG::5514]

Stažení dat
"""""""""""

.. literalinclude:: ../_static/skripty/owslib-wfs-example.py
   :language: python
   :lines: 28-29

.. code-block:: python

   <owslib.util.ResponseWrapper object at 0x7f697152df90>

.. literalinclude:: ../_static/skripty/owslib-wfs-example.py
   :language: python
   :lines: 31

.. code-block:: python
                
    <wfs:FeatureCollection xsi:schemaLocation='https:gis.nature.cz:6443/arcgis/services/UzemniOchrana/Ch...

VUV
"""

.. literalinclude:: ../_static/skripty/owslib-wfs-example.py
   :language: python
   :lines: 41-47

.. code-block:: bash
                
    <wfs:FeatureCollection xsi:schemaLocation='...

CUZK WFS
""""""""

.. todo:: Nutnost autentizace pro kraj.read()

.. literalinclude:: ../_static/skripty/owslib-wfs-example.py
   :language: python
   :lines: 33-36

.. code-block:: bash

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
   :lines: 38-39

.. code-block:: bash
                    
   <gmgml:FeatureCollection xsi:schemaLocation="http://www.intergraph.com/geomedia/gml http://geopor....
