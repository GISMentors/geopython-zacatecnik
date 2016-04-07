Komentáře
---------

Program si teď zpřehledníme komentářem. V Pythonu komentář začíná dvojkřížkem
(#), za který můžeš napsat úplně cokoliv – až do konce řádku bude Python všechno
ignorovat.

Komentáře jsou důležité, protože programy nečte jen Python, ale i lidé. Do
komentářů si můžeš poznamenat co dělá celý program, vysvětlit jak funguje nějaká
složitější část, nebo vyjasnit něco, co není jasné přímo z programu.

Vždycky když píšeš program, snaž se vžít do role někoho, kdo potom ten program
bude číst, a všechno co by mohlo být nejasné upřesnit v komentářích. (Nejčastěji
to budeš číst sama, třeba po několika měsících, takže tím pomáháš sama sobě!)

.. note:: O tom *jak správně komentovat* byly napsány knihy. Při práci se
        dostanete do bodu, kdy si budete říkat "Mám tohle ještě komentovat a
        nebo je to zbytečné?" 

        Snažte se především psát kód tak, aby ho *nebylo nutné komentovat*.
        Jasné názvy proměnných, spíše menší počet řádků, šířka řádků do 80 znaků
        a další ... to jsou zásady, které pomohou zpřehlednit kód. Pokud se už
        rozhodnete komentovat kód, držte se zásady *ne co program dělá, ale
        proč*. "Co" vyplývá z kódů, ale "proč" jste udělali něco zvláštního,
        pomohli jste si nějakým "hackem", proč to děláte jak to děláte a není to
        zcela jasné z kontextu.

        V těchto příkladech ale budeme z demonstračních důvodů tuto zásadu
        porušovat.

.. code-block:: python

        # Tento program počítá obvod a obsah čtverce.
        # Napsal Programátor Začátečník

        strana = 123  # v centimetrech

        # výtisk výpočtu obsahu a obvodu do konzole
        print('Obvod čtverce se stranou', strana, 'je', 4 * strana, 'cm')
        print('Obsah čtverce se stranou', strana, 'je', strana * strana, 'cm2')
