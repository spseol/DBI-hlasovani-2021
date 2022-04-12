#!/usr/bin/env python3
# Soubor:  cratedb.py
# Datum:   11.04.2022 18:49
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL
# Úloha:   Vytvoří prázdnou DB a příslušné tabulky
############################################################################

import sqlite3

dbfile = "database.sqlite"

SQL = """
CREATE TABLE "hlas" (
    "id"	INTEGER,
    "rocnik" INTEGER NOT NULL,
    "znamka" INTEGER NOT NULL,

    PRIMARY KEY("id" AUTOINCREMENT)
);

"""

with sqlite3.connect(dbfile) as conn:
    conn.executescript(SQL)
