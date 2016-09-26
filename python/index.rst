Úvod do jazyka Python
#####################

Psát programy v jazyce Python lze buď *interaktivně* nebo do souboru. Při
interaktivním způsobu práce spustíme interpret jazyka Python přímo v terminálu a
postupně do něj píšeme příkazy a potvrzujeme klávesou *Enter*. Interpret jazyka
Python spustíme příkazem `python`:

.. note:: V těchto letech (!) procházíme složitou fází přechodu mezi dvěma
        ne-zcela kompatibilními verzemi jazyka Python - 2 a 3. Další text se
        bude opírat o Python 3. Na některých systémech jej musíte pustit
        příkazem `python3`.

.. code-block:: bash

        $ python3


.. code-block:: python

    Python 3.4.3+ (default, Oct 14 2015, 16:03:50)
    [GCC 5.2.1 20151010] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

První program
=============

V interpretu jazyka Python můžeme napsat první krátký program. Tradice velí začít pozdravem "Ahoj světe!" vypsaným do terminálu. Interpret jazyka Python
*interpretuje* námi napsaný program:

.. code-block:: python
    
    >>> print('Ahoj, světe!')
    Ahoj, světe!
    >>>

Stejný program můžeme uložit do souboru s koncovou `.py` a vykonat jej jako
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
