import sqlite3

"""
SELVITÄ miksi otteluiden tuloksien muokkaus ei aktivoi pelattu switchiä oikein
SELVITÄ miksi switch ei toimi muutenkaan, liittynevät samaan asiaan
"""

def alusta_tietokanta():
    pass


conn = sqlite3.connect(':memory:')
# conn = sqlite3.connect(r"C:\Users\Kingi\Ohjelmointi\Bootcamp\demo\db\testi2.db")

cur = conn.cursor()
cur.executescript("""CREATE TABLE IF NOT EXISTS tulokset(
                        tulos_id INTEGER PRIMARY KEY,
                        ottelupari text,
                        tulos text NULL,
                        pelattu text NULL                        
            );

            CREATE TABLE IF NOT EXISTS osallistujat(
                        osallistuja_id INTEGER PRIMARY KEY,
                        osallistuja text UNIQUE,
                        pisteet integer

            );
            CREATE TABLE IF NOT EXISTS veikkaukset(
                        veikkaus_id INTEGER PRIMARY KEY,
                        osallistuja_id integer,
                        tulos_id integer,
                        veikkaus text,
                        FOREIGN KEY (osallistuja_id) REFERENCES osallistujat (osallistuja_id),
                        FOREIGN KEY (tulos_id) REFERENCES tulokset (tulos_id)
            );
            """)


# Ottelu_lista = [('Rus-Sau'), ('Egt-Uru'), ('Mor-Ira'), ('Por-Spa'), ('Fra-Aus'), ('Arg-Ice'), ('Per-Den'), ('Cro-Nig'), ('Cos-Ser'), ('Ger-Mex')]
# Ottelu_lista = [('Rus-Sau', None), ('Egt-Uru', None), ('Mor-Ira', None), ('Por-Spa', None), ('Fra-Aus', None), ('Arg-Ice', None), ('Per-Den', None), ('Cro-Nig', None), ('Cos-Ser', None), ('Ger-Mex', None)]
Ottelu_lista = [('Rus-Sau', '5-0'), ('Egt-Uru', '0-1'), ('Mor-Ira', '0-1'), ('Por-Spa', '3-3'), ('Fra-Aus', None),
                ('Arg-Ice', None), ('Per-Den', None), ('Cro-Nig', None), ('Cos-Ser', None), ('Ger-Mex', None)]
Osallistujat_lista = [('Kingis', 0), ('Matti', 0), ('Jussi', 0)]
Veikkaukset_lista = [(1, 1, '2-0'), (1, 2, '1-2'), (1, 3, '1-1'), (1, 4, '1-2'), (1, 5, '1-1'),
                     (2, 1, '2-0'), (2, 2, '1-3'), (2, 3, '1-1'), (2, 4, '2-1'), (2, 5, '2-0'),
                     (3, 1, '1-1'), (3, 2, '1-2'), (3, 3, '2-1'), (3, 4, '2-2'), (3, 5, '3-0')]

cur.executemany("INSERT INTO tulokset(ottelupari, tulos) VALUES (?, ?)", Ottelu_lista)
cur.executemany("INSERT INTO osallistujat(osallistuja, pisteet) VALUES (?, ?)", Osallistujat_lista)
cur.executemany("INSERT INTO veikkaukset(osallistuja_id, tulos_id, veikkaus) VALUES (?, ?, ?)", Veikkaukset_lista)
conn.commit()

tulokset = cur.execute("SELECT * FROM tulokset ORDER BY tulos_id")
tulokset = tulokset.fetchall()
print(tulokset)

# veikkaukset = cur.execute("SELECT * FROM veikkaukset ORDER BY osallistuja_id ASC, tulos_id ASC")
veikkaukset = cur.execute("SELECT * FROM veikkaukset")
veikkaukset = veikkaukset.fetchall()
print(veikkaukset)

osallistujat = cur.execute("SELECT * FROM osallistujat ORDER BY osallistuja_id")
osallistujat = osallistujat.fetchall()
print(osallistujat)


def laske_ottelu_pisteet(tulos, veikkaus):
    pisteet = 0

    if tulos[0] < tulos[2]:
        tulos_yksiristikaksi = "2"
    elif tulos[0] > tulos[2]:
        tulos_yksiristikaksi = "1"
    else:
        tulos_yksiristikaksi = "x"

    if veikkaus[0] < veikkaus[2]:
        veikkaus_yksiristikaksi = "2"
    elif veikkaus[0] > veikkaus[2]:
        veikkaus_yksiristikaksi = "1"
    else:
        veikkaus_yksiristikaksi = "x"

    if veikkaus_yksiristikaksi == tulos_yksiristikaksi:
        pisteet += 1

        if veikkaus[0] == tulos[0]:
            pisteet += 1
        if veikkaus[2] == tulos[2]:
            pisteet += 1

    return pisteet


def paivita_tulos():

    tulos_id = "."
    while tulos_id:
        cur.execute("SELECT * FROM tulokset")
        data = cur.fetchall()

        id_lista = []
        for rivi in data:
            print(rivi)
            if rivi[0] not in id_lista:
                id_lista.append(str(rivi[0]))

        print("Anna sen ottelun id numero, minkä haluat päivittää")
        print("Palaa alkuvalikkoon painamalla enteriä")
        tulos_id = input('Ottelun id numero:').strip()

        if tulos_id in id_lista:
            paivita_tulos_lista = tarkista_syote()

            cur.execute("UPDATE tulokset SET tulos = ('{}') WHERE tulos_id = ('{}')".format(paivita_tulos_lista, tulos_id))
            cur.execute("UPDATE tulokset SET pelattu = ('{}') WHERE tulos_id = ('{}')".format(0, tulos_id))
            conn.commit()
            print(f"Ottelu id {tulos_id} päivitetty tuloksella {paivita_tulos_lista}")

        elif tulos_id == "":
            return

        else:
            print("Ottelun id:tä ei löydy")


def tarkista_syote():
    print("Anna ensiksi kotijoukkueen maalimäärä, paina enteriä ja tämän jälkeen vierasjoukkueen maalimäärä")
    print("Maalimäärien täytyy olla positiivisia kokonaislukuja väliltä 0-99")

    while True:
        kotimaalit = input('Kotijoukkueen maalit:').strip()
        vierasmaalit = input('Vierasjoukkueen maalit:').strip()

        if kotimaalit.isdigit() and vierasmaalit.isdigit():
            if (int(kotimaalit) < 99 or int(kotimaalit) > 0) and (int(vierasmaalit) < 99 or int(vierasmaalit) > 0):
                tulos_str = f"{kotimaalit}-{vierasmaalit}"
                return tulos_str
            else:
                print('Maalimäärät virheellisiä')
        else:
            print('virheellinen syöte')


def laske_yhteispisteet():

    for tulosrivi in tulokset:
        for veikkausrivi in veikkaukset:
            # JOS ottelun id == osallistujan veikkaaman ottelun id
            if tulosrivi[0] == veikkausrivi[2]:
                print("------------")
                osallistujat_dict = {1: 'Kingis', 2: 'Matti', 3: 'Jussi'}
                tulos_id = tulosrivi[0]
                tulos = tulosrivi[2]
                pelattu_switch = tulosrivi[3]
                veikkaajan_id = veikkausrivi[1]
                veikkaus = veikkausrivi[3]

                print(f"{osallistujat_dict[veikkaajan_id]} veikkaus {veikkaus}, tulos {tulos}")

                if not tulos:
                    continue

                elif not pelattu_switch:
                    cur.execute("UPDATE tulokset SET pelattu = ('{}') WHERE tulos_id = ('{}')".format(1, tulos_id))
                    conn.commit()

                    pisteet = laske_ottelu_pisteet(tulos, veikkaus)

                    if pisteet > 0:
                        print(f"lisätään {pisteet} pistettä osallistuja id:lle {osallistujat_dict[veikkaajan_id]}")

                        # HAE tämän hetkisen osallistujan pistetiedot, sijoita ne vanhat_pisteet muuttujaan, lisää siihen uudet pisteet
                        cur.execute("SELECT pisteet FROM osallistujat WHERE osallistuja_id = ('{}')".format(veikkaajan_id))
                        vanhat_pisteet = cur.fetchone()
                        pisteet = vanhat_pisteet[0] + pisteet

                        # SIJOITA uudelleen lasketut pisteet takaisin tietokantaan saman osallistujan pistetietoihin
                        cur.execute(
                            "UPDATE osallistujat SET pisteet = ('{}') WHERE osallistuja_id = ('{}')".format(pisteet,
                                                                                                            veikkaajan_id))
                        conn.commit()

                    else:
                        print("Ei pisteitä...")

                else:
                    print("Ottelun pisteet on laskettu jo, siirrytään seuraavaan otteluun...")

    cur.execute("SELECT * FROM osallistujat")
    print(cur.fetchall())




def pistetilanne():
    cur.execute("SELECT * FROM osallistujat")
    print(cur.fetchall())


def main():
    # Ohjelma aloitetaan kysymällä käyttäjältä mitä tämä haluaa tehdä, '(U)usi peli' aloittaa uuden pelin,
    # '(T)ilastot' avaa pelattujen pelien tilastoja. '(L)opeta.' lopettaa ohjelman suorituksen.
    while True:
        print('Tervetuloa Futisveikkaukseen.')
        print('(A)lusta uusi tietokanta')
        print('(M)uokkaa ottelutuloksia')
        print('(L)aske yhteispisteet')

        print('(O)sallistu veikkaukseen')
        print('(P)istetilanne')
        print('(Q)uit')

        syote = input('Tee Valintasi.').lower()
        if syote == 'a':
            alusta_tietokanta()
        elif syote == 'l':
            laske_yhteispisteet()
        elif syote == 'p':
            pistetilanne()
        elif syote == 'm':
            paivita_tulos()
        elif syote == 'q':
            # exit()
            break
        else:
            print('Laiton valinta')


if __name__ == '__main__':
    main()
