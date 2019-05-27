Pole a slovníky
===============

V programovacích jazycích můžeme pracovat s poli (seznamy, množinami) prvků. V
Pythonu můžeme kombinovat různé datové typy jednotlivých prvků v poli.

Nejjednodušším případem pole může být pole celých čísel od 0 do 9:

.. code-block:: python

    >>> cisla = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(cisla)

Z výše uvedeného je patrné, že pole zapisujeme do *hranatých závorek*. Jak jsme
psali výše, neusíme se omezovat ja jeden datový typ:

.. code-block:: python

    >>> netrideny_srot = [1000, 'elce pelce do pekelce', 10/3]


K prvkům pole přistupujeme pomocí *indexů* - pomocí čísla pozice prvku v poli,
první index má hodnotu 0:

.. code-block:: python

    >>> print(netrideny_srot[0])
    1000
    >>> print(netrideny_srot[2])
    3.3333333333333335
    >>> print(cisla[5])
    4
    >>> print(cisla[10])
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    IndexError: list index out of range

Poslední příklad "vyhodil" ``IndexError`` - pokusili jsme se zobrazit hodnotu
*jedenáctého prvku* v poli (index 10, ale počítáme od 0!), pole ``cisla`` má ale
pouze 10 prvků (maximální index je proto 9).

Funkce ``len()`` nám vrátí celkovou délku pole (počet jeho prvků):

.. code-block:: python

    >>> len(cisla)
    10
    >>> len(netrideny_srot)
    3

Pole můžeme slučovat:

.. code-block:: python

    >>> jeste_vetsi_srot = cisla + netrideny_srot
    >>> print(jeste_vetsi_srot)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1000, 'elce pelce do pekelce', 3.3333333333333335]

K prvkům pole můžeme přistupovat "od zadu" používáním záporných indexů. Hodnotu
posledního prvku v poli můžeme získat následujícími dvěma způsoby:

.. code-block:: python

    >>> cisla[len(cisla)-1] # len() vrátí délku pole, nejvyšší index má ale hodnotu o 1 menší
    9
    >>> cisla[-1]
    9

"Vyzobnout" pouze určité prvky z pole můžeme pomocí zadání dvou krajních indexů:

.. code-block:: python

    >>> jeste_vetsi_srot[8:11]
    [8, 9, 1000, 'elce pelce do pekelce']

N-tice (tuple)
--------------
Uspořádané *n-tice* prvků (v Pythonu se jmenují `tuple`) se chovají stejně jako
pole, ale s tím rozdílem, že po jejich inicializaci je *nemůžeme nijak měnit*.
Použít se dají pro větší bezpečnost (nelze je přepsat) u vstupních hodnot v
prgramu (např. dny v týdnu, měsíce, senzam vstupních hodnot a pod.).

Chovají se stejně jako seznamy, akorát při inicializaci se nepoužívají závorky
hranaté, ale kulaté.

.. code-block:: python

    >>> tyden = ('pondeli', 'utery', 'streda', 'ctvrtek', 'patek', 'sobota', 'nedele')
    >>> print(tyden[3])
    ctvrtek

Slovníky (asociativní pole)
---------------------------
Slovníky jsou v podstatě pole s tím rozdílem, že k jednotlivým prvkům se
nepřistupuje pomocí číselných indexů, ale pomocí pojmenovaných odkazů. Při
jejich definici používáme složené závorky `{ }` a klíč od hodnoty oddělujeme
dvojtečkou `:`.

.. code-block:: python

    >>> telefonni_seznam = {
        'Petr': 728123432,
        'Pavel': 8344569870,
        'Klara': 9087354398,
        'Verca': 87698394,
    ...}

    >>> print(telefonni_seznam['Petr'])
    728123432

Zanořování polí
---------------

Jednotlivé prvky polí mohou být jakéhokoliv datového typu - číslo, text nebo i
*jiné pole*. Takto můžeme vytvářet matice (uspořádané n-tice řádků a sloupců)
jako *pole polí*:

.. code-block:: python

    >>> cerveny_kanal = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [5, 2, 3, 4, 2, 6, 7, 8, 8],
        [1, 2, 3, 4, 5, 8, 7, 8, 9],
        [3, 2, 8, 4, 0, 6, 3, 8, 10],
        [1, 5, 3, 4, 2, 6, 2, 8, 1],
        [8, 2, 7, 4, 5, 0, 7, 5, 9],
        [1, 8, 3, 3, 5, 9, 7, 1, 9],
        [2, 2, 3, 4, 7, 6, 2, 8, 0],
        [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ]

Zanořovat pole lze samozřejmě "prakticky" nekonečně:

.. code-block:: python

    >>> rastr = [
        cerveny_kanal,
        zeleny_kanal,
        modry_kanal
    ]

Stejně tak můžeme libovolně zanořovat slovníky. Ty se využívají v populární
datovém formátu `JSON <http://json.org>`_ a od něho odvozeného formátu `GeoJSON
<http://geojson.org>`_:

.. code-block:: python

    >>> vrstva = { "type": "FeatureCollection",
    "features": [
      { "type": "Feature",
        "geometry": {"type": "Point", "coordinates": [102.0, 0.5]},
        "properties": {"prop0": "value0"}
        },
      { "type": "Feature",
        "geometry": {
          "type": "LineString",
          "coordinates": [
            [102.0, 0.0], [103.0, 1.0], [104.0, 0.0], [105.0, 1.0]
            ]
          },
        "properties": {
          "prop0": "value0",
          "prop1": 0.0
          }
        },
      { "type": "Feature",
         "geometry": {
           "type": "Polygon",
           "coordinates": [
             [ [100.0, 0.0], [101.0, 0.0], [101.0, 1.0],
               [100.0, 1.0], [100.0, 0.0] ]
             ]
         },
         "properties": {
           "prop0": "value0",
           "prop1": {"this": "that"}
           }
         }
       ]
     }

Nyní můžeme zjistit první souřadnici druhého objektu a jeho geometrický typ:

.. code-block:: python

    >>> print(vrstva['features'][1]['geometry']['type'])
    LineString
    >>> print(vrstva['features'][1]['geometry']['coordinates'][0])
    [102.0, 0.0]
