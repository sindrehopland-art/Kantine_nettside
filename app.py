from flask import Flask, render_template
from data import alle_varer, ukesmeny

app = Flask(__name__)


@app.route('/')
def hjemmeside():
    return render_template("index.html")

@app.route('/kontakt')
def kontakt():
    return render_template("kontakt.html")

@app.route('/meny')
def meny():
    return render_template("meny.html",ukesmeny = ukesmeny)

@app.route('/varer')
def varer():
    return render_template("varer.html", alle_varer = alle_varer)

if __name__ == '__main__':
    app.run()
