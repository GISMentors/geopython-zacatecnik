Třídy a objekty
===============
Python je *objektově - orientovaný programovací jazyk (OOP)* i když jeho
objektové vlastnosti nemusíte moc využívat, sem tam na vás vykouknou a dobré o
tom něco vědět. 

Téma objektově orientovaného programovaní dosti přesahuje smysl tohoto
tutoriálu, budeme se snažit jím projít co možná po povrchu, abychom byli schopni
pracovat s knihovnami pro prostorová data.

Objekty
-------
Když se řekne *objekt*, znamená v Pythonu všechno co můžete uložit do proměnné
(tedy i funkce, pole, data). V Pythonu není rozdíl mezi objektem a hodnoutou. 

Objekt je "něco", co má nějaké vlastnosti (data) a nějaká chování (metody),
které s daty pracují. Objekty spojují data a funkčnost do jednoho celku.

Jak zjistíte, jaké má objekt vlastnosti (atributy) a funkce (metody)? Samozřejmě
z dokumentace, např. pomocí programu `pydoc`

.. code-block:: bash    

    $ pydoc list

    Help on class list in module __builtin__:

    class list(object)
     |  list() -> new empty list
     |  list(iterable) -> new list initialized from iterable's items
     |  
     |  Methods defined here:
     |  
     |  __add__(...)
     |      x.__add__(y) <==> x+y
     |  
     |  __contains__(...)
     |      x.__contains__(y) <==> y in x
     |  
     |  __delitem__(...)
     ...

Rychlá pomoc je funkce `dir()`, která vrátí všechny atributy a metody daného
objektu

.. code-block:: python

    >>> dir([])
    ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__',
    '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
    '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__',
    '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__',
    '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__',
    '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__',
    'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop',
    'remove', 'reverse', 'sort']

z tohoto výpisu sice nepoznáte, jedná-li se o data (atributy) nebo metody
(funkce) daného objektu, ale pro základní přehled to stačí a odhadnout se to
podle názvu většinou dá. K podtržítkám v názvech některých vlastností se
dostaneme níže.

Pole prvků jako objekt
----------------------

Pojďme se podívat v rychlosti na objekt, který už známe, akorát jsme nevěděli,
že je to objekt, na *seznam prvků*. Jaké má vlastnosti zjistíme pomocí funkce
`dir()`:

.. code-block:: python

    dir([]) # vypíše vlastnosti prázdného pole
    ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__',
    '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
    '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__',
    '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__',
    '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__',
    '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__',
    'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop',
    'remove', 'reverse', 'sort']

Pomiňme pro chvíli vlastnosti začínající dvěma podtržítky `__` a všimněme si
těch, které začínají od `append`. Podíváme-li se do dokumentace pomocí nástroje
`pydoc` (`pydoc list`), zjistíme, že

        append(objekt)
            přidá nový element na konec pole

        count(hodnota)
            vrátí počet prvků, které odpovídají dané hodnotě

        extend(iterable)
            přidá další seznam na konec stávajícího seznamu

        index(hodnota)
            vrátí první index zadané hodnoty

        insert(index, objekt)
            vloží nový prvek na zadaný index (např. `pole.insert(0, 'elece pelce')`
            vloží nový prvek na první pozici pole

        pop()
            odebere poslední provek z pole

        remove(hodnota)
            smaže první prvek odpovídající zadané hodnotě

        reverse()
            otočí pořadí elementů v poli

        sort()
            seřadí elementy v poli

Příklad použití:

.. code-block:: python
    
    >>> pole = [10, 5, 'x', 'kecy v kleci', [7, 'a'], '+', -10]
    >>> print(pole)
    [10, 5, 'x', 'kecy v kleci', [7, 'a'], '+', -10]

    >>> pole.sort()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: unorderable types: str() < int()

    >>> pole.append('jeste neco')
    >>> print(pole)
    [10, 5, 'x', 'kecy v kleci', [7, 'a'], '+', -10, 'jeste neco']

    >>> pole.insert(3, 'neco na 4tou pozici')
    >>> print(pole)
    [10, 5, 'x', 'neco na 4tou pozici', 'kecy v kleci', [7, 'a'], '+', -10, 'jeste neco']
    >>>

A takto se s objekty pracuje - používáme jejich metody (v praxi funkce) a
atributy (data).

Objekt `Point` z modulu `shapely`
---------------------------------
Podíváme-li se do dokumentace třídy `shapely.geometry.Point`, uvidíme, že má
následující metody (vybírám ty zajímavé - použijte `pydoc
shapely.geometry.Point`):

    almost_equals()
        porovnává souřadnice až do přiměřeného počtu desetinných míst

    buffer()
        vrátí buffer podle zadaných parametrů

    contains()
        obsahuje jinou gemetrii

    crosses()
        kříží se s jinou geometrií

    difference()
        vrátí rozdíl s jinou geometrií

    distance()
        počítá vzdálenost k jiné geometrii

    overlaps, intersects, ...

    simplify()
        generalizeace

    to_wkb()
        vrátí *well known binary* representaci geometrie

    to_wkt()
        vrátí *well known text* representaci geometrie

    ...

Vybral jsem pouze některé metody, ale pojďme je trochu vyzkoušet:

.. code-block:: python

    from shapely.geometry.import Point

    bod1 = Point(10, 20) # vyrobíme nový bod, předpis pro parametry je ve funkci
                        # __init__
    print(bod1)

    bod2 = Point(10, 10)
    print(bod2)

    # měly by vzniknout 2 kruhy, které se vzájemně dotýkají svých středů
    buffer1 = bod1.buffer(10)
    buffer2 = bod2.buffer(10)

    # a jdeme si hrát
    buffer1.almost_equals(buffer2) # vrátí False

    myunion = None # inicializace prázdné proměnné
    if buffer1.intersects(buffer2): # pokud spolu geometrie souvisí
        myunion = buffer1.union(buffer2) # udělej jejich spojení

    # ověření, že střed je střed
    centroid = buffer2.centroid()

    centroid.almost_equals(bod2) # -> True


Vlastní třídy (po povrchu)
--------------------------
Jak si vytvářet vlastní objekty vytvoříme tak, že nejprve definujeme *třídu* a
následně budeme vytvářet její *instance*. 

Třída je jakýsi předpis pro objekt. Jeho instance je od třídy odvozený konkrétní
objekt. 

Příkladem třídy může být `Clovek`, který má atributy (vlastnosti) `ruka, noha,
zuby, jmeno` a metody (funkce) `mluv(), jez(), podej()`. Od této třídy pak můžeme
odvodit *instanci* konkrétního člověka jménem "Patrik Jouda", který bude mít
ruku, nohu, několik zubů a funkce že "mluví", "jí" a je schopen něco podat.

Nebo v případě rastrovýc souborů se shodneme na tom, že je potřeba mít třídu
*rastr*, která bude předepisovat co všechno takový rastrový objekt má mít -
Transformační matici (což je instance jiného objektu), počet řádků, počet
sloupců, rozlišení a metodu pro čtení a zápis vlastních dat.

Už jsme se seznámili se třídou Point, která reprezentuje obecnou bodovou
geometrii, která má vlastnosti (souřadnice) bodu a spoustu metod pro práci s
geometriemi.

Vlastní třídu vytvoříme tak, ji uvedeme kláčovým slovek `class` a případně jako
parametr přidáme "rodičovský objekt" (třídy od sebe mohou navzájem vlastnosti
dědit, např. člověk může dědit vlastnosti od třídy `Živočich`).

Pokud musíme nastavit nějaké proměnné hned na počátku inicializace třídy,
použijeme k tomu speciální metodu `__init__`, které můžeme předat inicializační
parametry (např. v případě našeho bodu `Point` jsme předávali souřadnice `x` a
`y`').

V rámci třídy musíte odkazovat slovem **self** na vlastnosti dané třídy. `self`
obsahuje odkaz "sám na sebe".

Vyzkoušejme si malý příklad vlastní třídy:

.. code-block:: python

    # definice vlastní třídy
    class MyClass():
        pass # 'pass' znamená "nedělej nic"

    moje_trida = MyClass()
    print(moje_trida)

Tento krátý program vytiskne adresu v paměti počítače *instance třídy*
`MyClass`, kterou jsme uložili do proměnné `moje_trida`::

        <__main__.MyClass object at 0x7f5b72e0fd30>

Pokusme se naši třídu trochu rozšířit - a pojďme si vyrobit vlastní model
rastrového souboru:

.. code-block:: python

    class Raster(object): # je vhodné odvodit třídu od základního objektu 'object'
        """Třída reprezentující rastrová data
        """

        def __init__(self, columns, rows, transformation=None):
            """Konstruktor třídy - tato funkce se zavolá při vzniku nové
            instance třídy. Máme zde dva povinné parametry:

            columns - počet sloupců
            rows - počet řádků

            a jeden nepovinný parametr

            transformation - transformační matice, jak ji známe např. z formátu
                    GeoTIFF. Výchozí hodnota tohoto parametru je nastavena na
                    None, můžeme ho při zadání přeskočit

            """

            # nastavíme atributy (data) třídy
            self.columns = columns
            self.rows = rows
            self.transforamtion = transformation

            # inicializace prázdného pole 'data'
            self.data = None

        def set_data(self, data):
            """Metoda (funkce), která nám umožní nastavit data,
            data jsou očekávána jako pole polí - pole řádků, obsahující pole
            sloupců
            """

            self.data = data # jsme důvěřiví a nebudeme ověřovat, že vstupní
                             # data jsou opravdu sloupce a řádky

        def averadge_filter(self, size):
            """Funkce, která vrátí nový rastr (pouze data), obsahující původní
            hodnoty, které prošly filtrem o velikosti 3x3, kdy prostřední
            hodnota odpovídá průměru všech buněk okolo sum(matice)/(size * size)

            size = 3
            +---+---+---+      +---+---+---+
            | 1 | 2 | 4 |      |   |   |   |
            +---+---+---+      +---+---+---+
            | 1 | 3 | 2 | -->  |   |2.3|   |
            +---+---+---+      +---+---+---+
            | 2 | 3 | 3 |      |   |   |   |
            +---+---+---+      +---+---+---+
            """
            # size musí být liché číslo
            if size%2 == 0:
                size += 1

            # tohle bude komplikovanější a už na to napsali funkce jiní, zkusíme
            # si to ale naiplementovat sami. Až budete něco dělat s maticemi,
            # použijte dostupné funkce z balíčku numpy

            result = [ ]
            for row in range(self.data):
                if row < int(size/2):
                    continue
                elif row > len(self.data)-int(size/2):
                    continue
                result.append([])
                for col in range(self.data[row]):
                    if col < int(size/2):
                        continue
                    elif col > len(self.data)-int(size/2):
                        continue

                    for  # TODO - pro kazdou bunku



Slovo o podtržítkách
--------------------
Některé vlastnosti objektů mají název uvozený dvěma podtržíky, např.
`__sizeof__` a některé ne, jaký je v tom rozdíl? Pokud nějaká vlastnost objektu
začíná jedním podtržítkem, znamená to, že se jedná o *privátní* vlastnost.

Pokud je podtržítko na začátku jenom jedno, *neměli* byste tuto funkci používat
(ale technicky vzato je to povoleno a občas člověk musí v kódu trochu
"zaprasit").

Pokud vlastnost začíná dvěma podtržítky, je zcela privátní a *použít nejde*.
Zkusíme to oddemonstrovat na následujícím příkladu a pozor, vytvoříme naši první
*třídu* (objekt našeho vlastního typu):

.. code-block:: python

    >>> # nova trida
    >>> class MyClass(object):
    ...
    ...     def __init__(self):
    ...         """Konstruktor třídy - funkce, která se zavolá pouze při
    ...         inicializaci třídy"""
    ...         self.atribut = "veřejná vlastnost"
    ...         self._private_atribute = "privátní vlastnost"
    ...         self.__super_private_attribute = "na tohle už si nešáhneme
    ...
    ...     def _castecne_privatni(self):
    ...         """Částečně privátní metoda - není "vidět", ale můžeme ji použít
    ...         """
    ...
    ...         return "Castecne privatni funkce"
    ...
    ...     def __uplne_privatni(self):
    ...         """Zcela privátní metoda - z "venku" objektu není spustitelná
    ...         """
    ...
    ...         return "Uplne privatni funkce"
    ...
    ...     def uplne_verejna(self):
    ...         """Úplně veřejná metoda - můžeme ji spouštět
    ...         """
    ...
    ...         # "uvnitř" objektu na privátní funkce dosáhneme
    ...         return "Uplne verejna funkce a vola privatni: " + self.__uplne_privatni()

    >>> # a ted ji pouzijeme
    >>> moje_trida = MyClass()
    >>> c._castecne_privatni()
    Castecne privatni funkce

    >>> c.__uplne_privatni()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: 'MyClass' object has no attribute '__uplne_privatni'

    >>> c.uplne_verejna()
    Uplne verejna funkce a vola privatni: Uplne privatni funkce
