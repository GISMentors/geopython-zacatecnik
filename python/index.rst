Úvod do jazyka Python
#####################

Psát programy v jazyce Python lze buď *interaktivně* nebo do souboru. Při
interaktivním způsobu práce spustíme interpret jazyka Python přímo v terminálu a
postupně do něj píšeme příkazy a potvrzujeme klávesou *Enter*. Interpret jazyka
Python spustíme příkazem ``python``:

.. note:: V těchto letech (!) procházíme složitou fází přechodu mezi dvěma
        ne-zcela kompatibilními verzemi jazyka Python - 2 a 3. Další text se
        bude opírat o Python 3. Na některých systémech jej musíte pustit
        příkazem ``python3``.

.. code-block:: bash

        $ python3


.. code-block:: python

    Python 3.4.3+ (default, Oct 14 2015, 16:03:50)
    [GCC 5.2.1 20151010] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

Virtualenv
==========

Python `virtualenv <https://docs.python.org/3/library/venv.html>`_ je způsob,
jak vytvořit lehké virtuální prostředí pro běh aplikací napsaných v Pythonu.
Každý program má určité závislosti (potřebné knihovny, programy třetích stran),
časem zjistíte, že potřebujete další verze těchto závislostí, které jsou pro
různé projekty různé a navzájem nekompatibilní.

*Virtualenv* vám umožní do tohoto chaosu přivézt trochu struktury. Virtualenv je
adresář s kopiemi knihoven (v patřičných verzích). Adresář je většinou uložený
přímo u programu.

.. note:: Pro pokročilejší použití ``virtualenv`` je určitě vhodné použít
        `virtualenv wrapper
        <https://virtualenvwrapper.readthedocs.io/en/latest/>`_, který vám
        umožní ukládat virtuální prostředí do centrálního jednoho adresáře.


.. code-block:: bash

    virtualenv -p /usr/bin/python3 program_venv

::
       
    Running virtualenv with interpreter /usr/bin/python3
    Using base prefix '/usr'
    New python executable in program_venv/bin/python3
    Also creating executable in program_venv/bin/python
    Installing setuptools, pip...done.

Vytvoří pro *Python-3* virtuální prostředí v adresáři ``program_venv``. Následně
musíme virtuální prostředí *aktivovat*:

.. code-block:: bash

   source program_venv/bin/activate

Od této chvíle pracujeme ve virtuálním prostředí a cokoliv nainstalujeme
(prostřednictvím ``pip install``) bude uloženo do ``./program_venv/lib/python3.5/``.
Většinou nám to indikuje i prompt v příkazové řádce upozorňujícím textem.

Virtuální prostředí opustíme příkazem

.. code-block:: bash

   deactivate

První program
=============

V interpretu jazyka Python můžeme napsat první krátký program. Tradice velí začít pozdravem "Ahoj světe!" vypsaným do terminálu. Interpret jazyka Python
*interpretuje* námi napsaný program:

.. code-block:: python
    
    >>> print('Ahoj, světe!')
    Ahoj, světe!
    >>>

Stejný program můžeme uložit do souboru s koncovou ``.py`` a vykonat jej jako
celek (o ukládání programů do souborů ale bude další část).


.. code-block:: python
    
    #!/usr/bin/env python

    print('Ahoj, světe!')

**Obsah**

.. toctree::
   :maxdepth: 2

   print
   errors
   variables
   comments
   input
   operators
   conditions
   arrays
   loops
   functions
   exceptions
   modules
   files
   classes

Licence
-------
Tato část cituje z kurzů `PyLadies <http://pyladies.cz/>`_ a je šířena pod
kompatibilní licencí (`CC BY-SA 4.0 <http://creativecommons.org/licenses/by-sa/4.0/>`_).

.. todo::
   
   * Předělat příklady, aby více odpovídaly prostředí prostorových dat
