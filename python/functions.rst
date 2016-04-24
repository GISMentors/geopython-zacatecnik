Funkce
======

Až do této chvíle jsme používali funkce (`print, range, input, ...`), které
napsal někdo jiný. Nyní si ukážeme, jak napsat funkce vlastní a jak funkce
fungují.

Funkce jsou bloky kódu v logickém celku. Funkce se používají buď pro kód, který
plánujeme vykonávat opakovaně, především ale pro přehlednější členění kódu v
souboru.

Příklad nové funkce 

.. code-block:: python

    def obvod_obdelnika(sirka, vyska):
        "Vrátí obvod obdélníka daných rozměrů"
        return 2 * (sirka + vyska)

    # použití funkce obvod_obdelnika
    print(obvod_obdelnika(4, 2))

Funkce má následující rozepsanou strukturu

.. code-block:: text


            jméno funkce
               │
        +──────+──────+
        |             |
    def obvod_obdelnika(sirka, vyska):
                        |          |
                        +────+─────+
                             |
                        seznam argumentů

        "Vrátí obvod obdélníka daných rozměrů"  
        |                                    |
        +────── Dokumentační řetězec. ───────+

        return 2 * (sirka + vyska)
               |                 |
               +────────+────────+
                        |
                    návratová hodnota

Každá funkce je uvozena klíčovým slovem `def`, následuje její jméno a v závorce
seznam argumentů. Za dvojtečkou následuje *odsazený* blok kódu.

Je dobrým zvykem ihned po definici funkce přidat *dokumentační řetězec* a funkci
ukončit nějakou *návratovou hodnotou*

.. note:: Dokumentační řetězec ani `return` výraz na konci funkce nejsou nijak
    povinné, nicméně patří k dobré praxi je dodržovat. Dokumentování funkci
    (tříd, metod) nemá v Pythonu závazná pravidla, je však dobré dodržovat
    některý ze `stylů <https://docs.python.org/devguide/documenting.html>`_. Tím
    zároveň zajistíte možnost někdy v budoucnu automaticky generovat dokumentaci
    přímo z kódu.

Tělo funkce může obsahovat libovolný kód (dokonce i jinou vnořenou funkci),
podmínky, smyčky a podobně.

.. code-block:: python

    def napis_hlasku(nazev, skore):
        "Popíše skóre. Název má být přivlastňovací přídavné jméno."

        print(nazev, 'skóre je', str(skore))
        if skore > 1000:
            print('Světový rekord!')
        elif skore > 100:
            print('Skvělé!')
        elif skore > 10:
            print('Ucházející.')
        elif skore > 1:
            print('Aspoň něco')
        else:
            print('Snad příště.')

    napis_hlasku('Tvoje', 256)
    napis_hlasku('Protivníkovo', 5)

Když funkce voláme, předáváme jim argumenty. Ty musí být ve stejném pořadí, v
jakém jsou definovány v hlavičce funkce - tedy v tomto příkladě nejprve *název*
a potom *skóre*.

.. note:: Není to tak úplně pravda, argumenty můžeme zapsat i ve zpřeházeném
    pořadí, musíme je však explicitně pojmenovat, např. `napis_hlasku(skore=15,
    nazev='Naše')`.

Návratová hodnota `return`
--------------------------
Obsahuje-li funkce příkaz `return`, přestane se okamžitě vykonávat a *vrátí*
tuto hodnotu tomu, kdo funkci zavolal. Použijeme-li `return` uprostřed smyčky,
chová se podobně jako `break` příkaz.

Funkce, která nemá žádný příkaz `return` automaticky vrací hodnotu `None`

.. note:: A máme tady další datový typ, vedle čísel, textových řetězců a
    booleanovských hodnot máme datový typ *žádná hodnota* -- `None`

Platnost proměnných ve funkcích
-------------------------------

Proměnné v Pythonu mají platnost v blocích kódu a ve všech vnořených blocích.

.. code-block:: python

    coordinates = [100, 200]

    def move(x, y):
        orig_value = coordinates
        coordinates[0] = coordinates[0] + x
        coordinates[1] += y # zkrácená forma "přičti proměnnou y k původní hodnotě

    print(coordinates)
    move(5, 4)
    print(coordinates)

Po vykonání bychom měli dostat následující výstup:

.. code-block:: text

    [100, 200]
    [105, 104]

pokud bychom ale zkusili vytisknout hodnoty proměné `orig_value`, která je
definována uvnitř těla funkce, se zlou se potážeme:

.. code-block:: python

    print(orig_value)

    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'orig_value' is not defined

`orig_value` je *lokální proměnná*


