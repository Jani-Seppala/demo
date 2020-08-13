import sqlite3


# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect(r"C:\Users\Kingi\Ohjelmointi\Bootcamp\demo\db\testi.db")

cur = conn.cursor()

cur.execute("""CREATE TABLE tulokset(
                        id INTEGER PRIMARY KEY,
                        ottelupari text,
                        tulos text NULL
                        )""")


cur.execute("""CREATE TABLE osallistujat(
                        id INTEGER PRIMARY KEY,
                        osallistuja text,
                        pisteet integer
                        )""")


cur.execute("""CREATE TABLE veikkaukset(
                        osallistujat_id integer,
                        tulokset_id integer,
                        veikkaus text,
                        FOREIGN KEY (osallistujat_id) REFERENCES osallistujat (osallistujat_id),
                        FOREIGN KEY (tulokset_id) REFERENCES tulokset (tulokset_id)
                        )""")


# Ottelu_lista = [('Rus-Sau'), ('Egt-Uru'), ('Mor-Ira'), ('Por-Spa'), ('Fra-Aus'), ('Arg-Ice'), ('Per-Den'), ('Cro-Nig'), ('Cos-Ser'), ('Ger-Mex')]
Ottelu_lista = [('Rus-Sau', None), ('Egt-Uru', None), ('Mor-Ira', None), ('Por-Spa', None), ('Fra-Aus', None), ('Arg-Ice', None), ('Per-Den', None), ('Cro-Nig', None), ('Cos-Ser', None), ('Ger-Mex', None)]
Osallistujat_lista = [('Kingis', 0), ('Matti', 0), ('Jussi', 0)]
# Veikkaukset_lista = [(1, 1, '2-0')]


# veikkaajaid = 1
# veikkaajanimi = 'Kingis'
# pisteet = 0


# cur.execute("INSERT INTO tulokset(ottelupari, tulos) VALUES ('{}', '{}')".format(pari, tulos1))
# cur.execute("INSERT INTO tulokset(ottelupari) VALUES ('{}')".format(pari))
# cur.execute("INSERT INTO osallistujat(osallistuja, pisteet) VALUES ('{}', '{}')".format(veikkaajanimi, pisteet))

cur.executemany("INSERT INTO tulokset(ottelupari, tulos) VALUES (?, ?)", Ottelu_lista)
cur.executemany("INSERT INTO osallistujat(osallistuja, pisteet) VALUES (?, ?)", Osallistujat_lista)
conn.commit()

# cur.execute("SELECT * FROM tulokset")
# print(cur.fetchall())

# cur.execute("UPDATE tulokset SET tulos = ('{}') WHERE tulokset.id = 1".format(tulos1))


# cur.execute("SELECT * FROM osallistujat")
# print(cur.fetchall())
# conn.commit()

# cur.execute("SELECT * FROM osallistujat")
#
# print(cur.fetchall())
