import sqlite3

"""
SELVITÄ miksi laske_yhteispisteet() pitää ajaa 2 kertaa jotta muutokset tulevat näkyviin konsoliin vaikka muutokset tulevat voimaan databaseen jo ekalla ajolla
auttaako IS NULL?
RATKAISE paivita_tulos() ottelutulosten päivitys niin että laske_yhteispisteet() laskee kaikki ottelut jotka on pelattu, eikä lopeta laskemista noneen
TEE nickin uniikkiudelle tarkastus databasesta ja tarkista veikkaukset tutki_syote() funktion kautta
"""

def alusta_tietokanta():
    pass


conn = sqlite3.connect(':memory:')
# conn = sqlite3.connect(r"C:\Users\Kingi\Ohjelmointi\Bootcamp\demo\db\testi2.db")

cur = conn.cursor()
cur.executescript("""CREATE TABLE IF NOT EXISTS tulokset(
                        tulos_id INTEGER PRIMARY KEY,
                        ottelupari text,
                        tulos text DEFAULT NULL,
                        pelattu text DEFAULT NULL                        
            );

            CREATE TABLE IF NOT EXISTS osallistujat(
                        osallistuja_id INTEGER PRIMARY KEY,
                        osallistuja text UNIQUE,
                        pisteet integer DEFAULT 0

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
Ottelu_lista = [('Rus-Sau', '5-0'), ('Egt-Uru', '0-1'), ('Mor-Ira', '0-1'), ('Por-Spa', '3-3'), ('Fra-Aus', None),
                ('Arg-Ice', None), ('Per-Den', None), ('Cro-Nig', None), ('Cos-Ser', None), ('Ger-Mex', None)]
# Ottelu_lista = [('Rus-Sau', '5-0'), ('Egt-Uru', '0-1'), ('Mor-Ira', '0-1'), ('Por-Spa', '3-3'), ('Fra-Aus', ),
#                 ('Arg-Ice', ), ('Per-Den', ), ('Cro-Nig', ), ('Cos-Ser', ), ('Ger-Mex', )]

Osallistujat_lista = [('Kingis', ), ('Matti', ), ('Jussi', )]
Veikkaukset_lista = [(1, 1, '2-0'), (1, 2, '1-2'), (1, 3, '1-1'), (1, 4, '1-2'), (1, 5, '1-1'),
                     (2, 1, '2-0'), (2, 2, '1-3'), (2, 3, '1-1'), (2, 4, '2-1'), (2, 5, '2-0'),
                     (3, 1, '1-1'), (3, 2, '1-2'), (3, 3, '2-1'), (3, 4, '2-2'), (3, 5, '3-0')]

cur.executemany("INSERT INTO tulokset(ottelupari, tulos) VALUES (?, ?)", Ottelu_lista)
cur.executemany("INSERT INTO osallistujat(osallistuja) VALUES (?)", Osallistujat_lista)
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

            sql_update_tulos_query = "UPDATE tulokset SET tulos = ? WHERE tulos_id = ?"
            tulos_data = (paivita_tulos_lista, tulos_id)
            cur.execute(sql_update_tulos_query, tulos_data)
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
            if 0 <= int(kotimaalit) <= 99 and 0 <= int(vierasmaalit) <= 99:
                tulos_str = f"{kotimaalit}-{vierasmaalit}"
                return tulos_str
            else:
                print('Maalimäärät virheellisiä')
        else:
            print('virheellinen syöte')


def laske_yhteispisteet():

    tulokset = cur.execute("SELECT * FROM tulokset")
    tulokset = tulokset.fetchall()

    veikkaukset = cur.execute("SELECT * FROM veikkaukset")
    veikkaukset = veikkaukset.fetchall()

    for tulosrivi in tulokset:
        for veikkausrivi in veikkaukset:
            # JOS ottelun id == osallistujan veikkaaman ottelun id
            if tulosrivi[0] == veikkausrivi[2]:
                print("------------")
                tulos_id = tulosrivi[0]
                tulos = tulosrivi[2]
                pelattu_switch = tulosrivi[3]
                veikkaajan_id = veikkausrivi[1]
                veikkaus = veikkausrivi[3]

                sql_osallistuja_nimi_query = "SELECT osallistuja FROM osallistujat WHERE osallistuja_id = ?"
                data = (veikkaajan_id, )
                sql_exe = cur.execute(sql_osallistuja_nimi_query, data)
                sql_exe = sql_exe.fetchone()

                print(f"{sql_exe} veikkaus {veikkaus} otteluun {tulosrivi[1]}, tulos {tulos}")

                if not tulos:
                    continue

                elif not pelattu_switch:
                    sql_update_pelattu_query = "UPDATE tulokset SET pelattu = ? WHERE tulos_id = ?"
                    pelattu_data = (True, tulos_id)
                    cur.execute(sql_update_pelattu_query, pelattu_data)

                    pisteet = laske_ottelu_pisteet(tulos, veikkaus)

                    if pisteet > 0:

                        print(f"lisätään {pisteet} pistettä osallistuja id:lle {sql_exe}")

                        # HAE tämän hetkisen osallistujan pistetiedot ja päivitä ne
                        sql_paivita_pisteet_query = "UPDATE osallistujat SET pisteet = pisteet + ? WHERE osallistuja_id = ?"
                        paivita_pisteet_data = (pisteet, veikkaajan_id)
                        cur.execute(sql_paivita_pisteet_query, paivita_pisteet_data)
                        conn.commit()

                    else:
                        print("Ei pisteitä...")

                else:
                    print("Ottelun pisteet on laskettu jo, siirrytään seuraavaan otteluun...")

    cur.execute("SELECT * FROM osallistujat")
    print(cur.fetchall())

    cur.execute("SELECT * FROM tulokset")
    print(tulokset)



def pistetilanne():
    cur.execute("SELECT * FROM osallistujat")
    print(cur.fetchall())


def luo_osallistuja():

    luotu_nimi = input("Anna nimi/nick jolla osallistut kisaan: ")
    sql_luo_osallistuja_query = "INSERT INTO osallistujat(osallistuja) VALUES (?)"
    osallistuja_data = (luotu_nimi, )

    cur.execute(sql_luo_osallistuja_query, osallistuja_data)
    conn.commit()

    sql_valitse_osallistuja_query = "SELECT osallistuja_id FROM osallistujat WHERE osallistuja = ?"
    cur.execute(sql_valitse_osallistuja_query, osallistuja_data)
    uusi_osallistuja_id = cur.fetchone()

    luo_veikkaus(uusi_osallistuja_id[0])


def luo_veikkaus(uusi_osallistuja_id):

    sql_hae_tulokset_query = "SELECT tulos_id, ottelupari FROM tulokset"
    cur.execute(sql_hae_tulokset_query)
    data = cur.fetchall()

    osallistujan_veikkaukset = []
    for ottelu in data:
        ottelupari = ottelu[1]
        otteluid = ottelu[0]
        print(ottelu[1])
        osallistujan_veikkaus = input(f"Anna veikkaus ottelulle {ottelupari}: ")

        osallistujan_veikkaukset.append((uusi_osallistuja_id, otteluid, osallistujan_veikkaus))

    sql_tallenna_veikkaukset_query = "INSERT INTO veikkaukset(osallistuja_id, tulos_id, veikkaus) VALUES (?, ?, ?)"
    # veikkaus_data = (osallistujan_veikkaukset, )
    cur.executemany(sql_tallenna_veikkaukset_query, osallistujan_veikkaukset)


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
        elif syote == 'o':
            luo_osallistuja()
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
