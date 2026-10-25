from datetime import datetime
from flask import Flask, render_template
from data import alle_varer, ukesmeny, drikke, snacks, bakevarer, frukt, varm_drikke, mat

app = Flask(__name__)


@app.route('/')
def hjemmeside():
    dager = [
        "Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag", "Lørdag", "Søndag"
    ]

    dagens_dag = dager[datetime.today().weekday()]
    dagens_rett = None

    for rett in ukesmeny:
        if rett["dag"] == dagens_dag:
            dagens_rett = rett
            break

    return render_template("index.html", dagens_dag = dagens_dag, dagens_rett = dagens_rett, drikke = drikke, snacks = snacks, bakevarer = bakevarer)


@app.route('/kontakt')
def kontakt():
    return render_template("kontakt.html")

@app.route('/meny')
def meny():
    return render_template("meny.html",ukesmeny = ukesmeny)

@app.route('/varer')
def varer():
    return render_template("varer.html", alle_varer = alle_varer, drikke = drikke, snacks = snacks, bakevarer = bakevarer, frukt = frukt, varm_drikke = varm_drikke, mat = mat)

if __name__ == '__main__':
    app.run()
