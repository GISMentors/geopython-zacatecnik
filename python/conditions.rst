Podmínky
========

Pokud potřebujeme vykonat určitou část kódu pouze pokud je splněna nějaká
podmínka (tedy nějaký výraz je vyhodnocený jako pravivý - ``True``), potřebujeme
podmínky.

Základní konstrukce podmínky je

.. code-block:: python

    if výraz:
        co se má stát

Pokud chceme přidat část, která se má splnit pokud podmínka neplatí, přidáme
blok ``else``:

.. code-block:: python

    if výraz:
        co se má stát
    else:
        co se má stát v opačním případě

Často může nastat potřeba řetězení více podmínek - za klíčové slovo ``else``
můžeme přidat okamžitě další ``if``, ale Python nám umožňuje tento zápis zkrátit:


.. code-block:: python
    
    if výraz:
        co se má stát, když je výraz pravda
    elif jiný_výraz:
        co se má stát, když platí něco jiného
    elif další_výraz:
        takto můžeme pokračovat až do nekonečna
    else:
        konečný výchozí kód, který je vykonán, pokud vše ostatní selže

Podmíněné příkazy lze samozřejmě zanořovat

.. code-block:: python

    if výraz:
        if další_výraz:
            co se má stát, stane se
        else:
            něco jiného se stane
    else:
        původní podmínka nesplněna

Zkusíme napsat program, který se na začátku zeptá na věk za davatele a po té
nabídne vhodné občerstvení:

.. code-block:: python

        vek = int(input('Kolik ti je let? '))

        if vek >= 150:
            print('A ze kterépak jsi planety?')
        elif vek >= 18:
            print('Můžeme nabídnout: víno, cider, nebo vodku.')
        elif vek >= 1:
            print('Můžeme nabídnout: mléko, čaj, nebo vodu')
        elif vek >= 0:
            print('Sunar už bohužel došel.')
        else:
            print('Návštěvníky z budoucnosti tady nevidíme rádi.')

Ucelené bloky v Pythonu
=======================

Určitě jste si všimli, že na rozdíl od jiných populárních jazyků Python
nepoužívá k vymezení ucelených bloků kódu složené závorky, ale bloky strukturuje
pomocí *odsazení*. A na konci řádků není potřeba dávat znak ``;`` (středník).
Je v celku jedno, jestli používáte mezery nebo tabulátory a
jestli používáte 4 mezery nebo 2 tabulátory. Různé stupně odsazení dokonce
můžete měnit uprostřed programu.

.. note:: Že něco jde, neznamená, že byste to tak měli dělat. Praxe ukazuje, že
        používat tabulátory pro odsazení v kódu je zlo - každý textový editor má
        nastavenu jinou šířku tabulátoru.

        Jako nečastější se v Pythonních programech používají pro odazení bloku
        kódu *4 mezery*. Je dobrou praxí, nastavit v textovém editoru šířku
        tabulátoru na 4 znaky a automatické nahrazování tabulátorů za mezery.

Poprvé se nám bloky kódu objevují právě v podmínkách, budeme se s nimi ale
setkávat i dále.

Pro srovnání kód v jazyce JavaScript by s podmínkami a bloky kódu vypadal asi
takto:

.. code-block:: javascript

    if (a == 1) {
        console.log("'a' je jedna");
    } else {
        console.log("'a' není jedna");
    }

A to samé v Pythonu

.. code-block:: python

    if a == 1:
        print("'a' je jedna")
    else:
        print"'a' není jedna")

Vidíte, že je to méně psaní a Python vás nutí k čitelné struktuře kódu.


Jednořádková forma zápisu podmínky ``if``
=========================================
Programátoři jsou velice lenivý národ a často vytvářejí zkratky, aby ušetřili
řádek kódu nebo deset znaků na řádku. Často potřebujeme pouze krátkou formu
zápisu podmínky ``if`` (z Jazyka C hojne využívaný zápis ``vysledek = (podminka ? splneno :
nespleno);`` v Pythonu bohužel neexistuje. Ale jde to:

.. code-block:: python

    >>> fruit = 'Apple'
    >>> result = True if fruit == 'Apple' else False
    >>> print result
    True

    >>> fruit = 'Pear'
    >>> result = True if fruit == 'Apple' else False
    >>> print result
    False
