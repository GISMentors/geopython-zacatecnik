Komentáře
=========

Program si nyní zpřehledníme přidáním komentářů. V Pythonu začíná
komentář dvojkřížkem (``#``). Vše uvedené od tohoto znaku až do konce
řádku bude Pythonem ignorováno.

Komentáře jsou důležité, protože programy neintepretuje pouze Python,
ale také lidé. V komentářích lze popsat co celý program dělá,
vysvětlit jak funguje nějaká složitější jeho část, nebo vyjasnit něco,
co není jasné přímo z jeho zápisu.

.. tip::
   
   Vždy když vytváříte nějaký program, snažte se vžít do role někoho, kdo
   jej bude vás číst, a všechno co by mohlo být nejasné upřesnit v
   komentářích. (Nejčastěji budete svůj program po sobě číst sami, třeba
   po několika měsících, takže tím pomáháte především sami sobě!)

.. note:: O tom *jak správně psát komentáře* byly napsány celé
        knihy. Při práci se dostanete do bodu, kdy si budete říkat
        "Mám tohle ještě komentovat a nebo je to zbytečné?" Snažte se
        především psát kód tak, aby ho *nebylo nutné komentovat*.
        Jasné názvy proměnných, spíše menší počet řádků, šířka řádků
        do 80 znaků a další ... to jsou zásady, které pomohou kód
        zpřehlednit. Pokud se už rozhodnete komentovat kód, držte se
        zásady *ne co program dělá, ale proč*. "Co" vyplývá z kódů,
        ale "proč" jste udělali něco zvláštního, pomohli jste si
        nějakým "hackem", tj. něco co není zcela jasné z kontextu.

        V těchto příkladech ale budeme z demonstračních důvodů tuto zásadu
        porušovat.

.. code-block:: python

        # Tento program počítá obvod a obsah čtverce.
        # Napsal Programátor Začátečník

        strana = 123  # v centimetrech

        # výtisk výpočtu obsahu a obvodu do konzole
        print('Obvod čtverce se stranou', strana, 'je', 4 * strana, 'cm')
        print('Obsah čtverce se stranou', strana, 'je', strana * strana, 'cm2')
