from . import app
from flask import render_template, request, redirect, url_for

import sqlite3

dbfile = "database.sqlite"


@app.route("/", methods=["GET"])
def index():
    with sqlite3.connect(dbfile) as conn:
        prumer = list(conn.execute("SELECT AVG(znamka), COUNT(znamka) FROM hlas"))
    with sqlite3.connect(dbfile) as conn:
        prumery = conn.execute(
            "SELECT rocnik, AVG(znamka), COUNT(znamka) FROM hlas "
            "GROUP BY rocnik ORDER BY rocnik"
        )
    pokus = "<em>neco</em>"
    return render_template(
        "base.html.j2",
        prumer=prumer[0][0],
        pocet=prumer[0][1],
        prumery=prumery,
        pokus=pokus,
    )


@app.route("/add/", methods=["POST"])
def add():
    rocnik = request.form.get("rocnik")
    znamka = request.form.get("znamka")
    if all((rocnik, znamka)):
        with sqlite3.connect(dbfile) as conn:
            conn.execute(
                "INSERT INTO hlas (rocnik, znamka) VALUES (?, ?)", (rocnik, znamka)
            )
    return redirect(url_for("index"))
