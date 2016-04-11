Program uložený v souboru
=========================
Psaní příkazů přímo v Pythonu, interaktivně, má jednu velkou nevýhodu: to, co
napíšeme, se ztratí, jakmile zavřeme okno příkazové řádky. Na jednoduché výpočty
to nevadí, ale až budou naše programy složitější, budeme je potřebovat nějak
uložit.

Otevřete textový editor a napište do něj následující řádky.

.. note:: Používejte textový editor dle volby svého sdrce. Na Linuxu např.
        editor `gedit` nebo `kate`. Na Windows populární `pspad` nebo na všech
        platformách dostupný `sublime`.

.. code-block:: python

        #!/usr/bin/env python3

        print('Ahoj světe!')
        print('Jedna a jedna jsou %s' % (1 + 1))

.. note:: Na operačním systému MS Windows použijte na prvním řádku cestu k
        interpretu jazyka Python, např.::

        #!c:\Python3\python.exe

Soubor uložte pod nějakým názvem a koncovkou `.py`, např.  `pocitani.py`.

V příkazovém řádku můžete spustit interpret jazyka a jako parametr mu dát
soubor, který chcete spustit.

.. code-block:: bash

        jachym@krovak:~$ python3 pocitani.py
        Ahoj světe!
        Jedna a jedna jsou 2
        jachym@krovak:~$

Alternativně můžete nastavit skriptu příznak spustiltenosti a spustit jej přímo

.. code-block:: bash

        jachym@krovak:~$ chmod 755 pocitani.py
        jachym@krovak:~$ ./pocitani.py
        
.. note:: Více o  nastavení příznaků souborů v systémech Unix se dočtete na
        příklad na `Wiki systému Ubuntu <http://wiki.ubuntu.cz/chmod>`_
