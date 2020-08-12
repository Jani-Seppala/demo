import sqlite3


conn = sqlite3.connect(':memory:')

cur = conn.cursor()

cur.execute("""CREATE TABLE tulokset(
                        id integer PRIMARY KEY,
                        ottelupari text,
                        tulos text
                        )""")


cur.execute("""CREATE TABLE osallistujat(
                        id integer PRIMARY KEY,
                        osallistuja text,
                        pisteet int)
                        """)


cur.execute("""CREATE TABLE veikkaukset(
                        FOREIGN KEY (osallistujat.id) REFERENCES osallistujat (id),
                        FOREIGN KEY (tulokset.id) REFERENCES tulokset (id),
                        veikkaus, text""")

# Tulos_lista = [('rus-sau', '2-1'), ('egt-uru', '1-1'), ('mor-ira', '1-2')]
tulos1 = '2-1'
pari = 'rus-sau'

cur.execute("INSERT INTO tulokset VALUES ('{}', '{}')".format(tulos1, pari))


conn.commit()