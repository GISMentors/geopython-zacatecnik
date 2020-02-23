=============================
Instalace potřebných knihoven
=============================

Jazyk Python lze provozovat na všech běžných desktopových platformách
(Linux, Windows, MacOS), i těch méně běžných. Existují i porty Pythonu
do malých jednoprocesorových počítačů `Micropython
<https://micropython.org/>`__, stejně tak ho lze využít k programování
např. vývojové desky `Micro:bit <https://microbit.org/>`__.

Je dobré i uvědomit, že Python, jako takový je vlastně pouze specifikace jazyka
-  předpis, jak se má daný zápis kódu interpretovat. Existuje řada intepretů
jazyka Python, naprogramových ovšem v jiných programovacích jazycích, jako jsou

* `CPython <http://python.org>`_ - základní interpret v jazyce C. Když se řekně
  "python", myslí se tím obvykle jazyk + tento výchozí interpreter.
* `IronPython <https://ironpython.net/>`_ - interpret jazyka z prostředí .NET
* `Jython <https://www.jython.org/>`_ - interpret jazyka Python naprogramovaný
  v jazyce Java
* `PyPy <https://www.pypy.org/>`_ - Python interpreter napsaný v Pythonu
* `PythonNet <https://github.com/pythonnet/pythonnet>`_ nebo `Stackless
  <https://github.com/stackless-dev/stackless/wiki>`_ Python (ty jsou více
  okrajové).

Každá implementace má nějaký důvod - např. pomocí Jython můžete zaintegrovat
kusy kódu do jinak javového prostředí. Můžete si "z jazyka Python" dosáhnout pro
potřebné knihovny do prostředí Java. PyPy se zase zdá být rychlejší, než výchozí
CPython. 

Bohužel ne všechny implementace dokáží držet krok s vývojem a tak jazyk Python a
jeho interpret CPython jsou momentálně ve verzi 3.7 (jaro 2020), Jython ustrnul
ve verzi 2.7 a nezdá se, že by se posouval.

Součástí programování je ale i využívání externích knihoven - a ty jsou mezi
různými jazyky (programovacími platformami) spíš nepřenositelné. Nelze na úrovni
kódu využívat funkce programu v jazyce Java v jazyce C (tedy ... jsou na to
techniky, ale ty patří mezi hodně pokročilé). Proto je potřeba používat takový
interpert jazyka, který je použitý s požadovanými knihovnami.

Proto se budeme držet referenční implementace CPython.

Verze jazyka Python
-------------------

V současné době se ještě stále nacházíme v přechodné fázi, mezi verzí jazyka 2 a
3. Naše kurzy již využívají Python3, stejně tak všechny námi doporučené
knihovny a programy. Pokud vám ale někdo dá "na výběr" nebo si nejste jisti,
jakou verzi zvolit, berte 3. Pokud přijdete k projektu, který využívá Pyhon 2
(poslední verze je 2.7), syntaxe je na 99% stejná, takže vše, co se naučíte pro
Python 3 bude použitelné i pro Python 2. 

V poslední době ale většina projektů přestává Python 2 podporovat.

Návody pro vybrané platformy
----------------------------

.. toctree::
        :maxdepth: 2

        linux
        windows
