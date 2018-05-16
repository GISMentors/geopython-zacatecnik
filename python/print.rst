Program uložený v souboru
=========================

Interaktivní spouštění příkazů přímo v interpretu jazyka Python má
jednu velkou nevýhodu: to, co napíšeme se ztratí, jakmile zavřeme
okno příkazové řádky. Pro jednoduché výpočty to nevadí, ale až budou
naše programy složitější, budeme je potřebovat nějak uložit.

Otevřete textový editor a napište do něj následující řádky.

.. note:: Používejte textový editor dle volby svého sdrce. Na Linuxu
        např.  editor `geany`, `gedit` nebo `kate`. Na Windows
        populární `pspad` nebo na všech platformách dostupný
        `sublime <https://www.sublimetext.com/>`_ či `pycharm <https://www.jetbrains.com/pycharm/>`_.

.. code-block:: python

        #!/usr/bin/env python3

        print('Ahoj světe!')
        print('Jedna a jedna jsou {}'.format(1 + 1))

.. note:: Na operačním systému MS Windows použijte na prvním řádku cestu k
        interpretu jazyka Python, např.::

        #!c:\Python3\python.exe

        Při instalaci Pythonu do operačního systému Windows je dobré zaškrtnout
        volbu `dostupný pro všechny uživatele` a `přidat cestu do systémové
        proměnné $PATH` - tím zajistíte, že jednoduše přiřadíte soubory s
        koncovkou ".py" k interpretu Python

Soubor uložte pod nějakým názvem a koncovkou ``.py``, např. ``pocitani.py``.

V příkazovém řádku můžete spustit interpret jazyka a jako parametr mu předat
soubor, který chcete spustit.

.. code-block:: bash

        $ python3 pocitani.py
        Ahoj světe!
        Jedna a jedna jsou 2

Alternativně můžete nastavit skriptu příznak spustiltenosti a spustit jej přímo (návod pro OS GNU/Linux):

.. code-block:: bash

        $ chmod 755 pocitani.py
        $ ./pocitani.py
        
.. note:: Více o  nastavení příznaků souborů v systémech Unix se dočtete na
        příklad na `Wiki Ubuntu <http://wiki.ubuntu.cz/chmod>`_.
