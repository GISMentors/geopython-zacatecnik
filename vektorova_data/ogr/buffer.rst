Příklad vytvoření obalové zóny
------------------------------

Na tomto příkladu si ukážeme, jak otevřít vektorová data ve formátu
Esri Shapefile, načíst datovou vrstvu, zobrazit atributy geoprvků a
vytvořit obalovou zónu nad načtenými geoprvky.

Nejprve otevření souboru s daty:

.. literalinclude:: ../../_static/skripty/ogr-buffer.py
   :language: python
   :lines: 1-3

::
   
   <osgeo.ogr.DataSource; proxy of <Swig Object of type 'OGRDataSourceShadow *' at 0x7f98d8152a50> >

.. literalinclude:: ../../_static/skripty/ogr-buffer.py
   :language: python
   :lines: 4
    
::
   
   1

Práce s vrstvou, její otevření:

.. literalinclude:: ../../_static/skripty/ogr-buffer.py
   :language: python
   :lines: 5-6
           
::
   
   <osgeo.ogr.Layer; proxy of <Swig Object of type 'OGRLayerShadow *' at 0x7f98d80fa870> >

.. literalinclude:: ../../_static/skripty/ogr-buffer.py
   :language: python
   :lines: 7

::
   
    5626

Schéma vrstvy - definice typu geometrie a jednotlivých atributových polí:

.. literalinclude:: ../../_static/skripty/ogr-buffer.py
   :language: python
   :lines: 9-10

::
   
   3
   True

.. literalinclude:: ../../_static/skripty/ogr-buffer.py
   :language: python
   :lines: 11-12

::
   
   [<osgeo.ogr.FieldDefn; proxy of <Swig Object of type 'OGRFieldDefnShadow *' at 0x7f98d80fa9f0> >,
   <osgeo.ogr.FieldDefn; proxy of <Swig Object of type 'OGRFieldDefnShadow *' at 0x7f98d80fa8...
   'NAZEV'

Vypsání názvu geoprvku (atribut ``NAZEV``):

.. literalinclude:: ../../_static/skripty/ogr-buffer.py
   :language: python
   :lines: 14-17

::
   
    Český ráj
    ...

Vypsání vlastnosti geometrické složky popisu geoprvků (minimálního
ohraničujícího obdélíku a centroidu polygonu, vytvoření obálky):

.. literalinclude:: ../../_static/skripty/ogr-buffer.py
   :language: python
   :lines: 20-22

::

    Český ráj

.. literalinclude:: ../../_static/skripty/ogr-buffer.py
   :language: python
   :lines: 24-25

::
   
    (-683329.1875, -681265.625, -993228.75, -991528.0)

.. literalinclude:: ../../_static/skripty/ogr-buffer.py
   :language: python
   :lines: 27-28

::
   
    (-682407.4126500859, -992433.3498782327, 0.0)

.. literalinclude:: ../../_static/skripty/ogr-buffer.py
   :language: python
   :lines: 30-31

::
   
    True
