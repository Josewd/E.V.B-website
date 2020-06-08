from flask import Flask, render_template, request, session, redirect, url_for
from flask_session import Session
from cs50 import SQL
from random import choice
import smtplib



app = Flask(__name__, static_url_path='/static')

db = SQL("sqlite:///database.db")

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


app.config["TEMPLATES_AUTO_RELOAD"] = True

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/", methods=["GET", "POST"])
def index():
    textos = ["Nossos serviços: somos especialistas no transporte de alimentos, documentos e pacotes com peso de até (6kg) utilizando somente a BICICLETA como modal.",
                "Nossos ciclistas são experientes e muito cuidadosos, e não só nas ruas molhadas, são sempre!",
                "Chuva é vida! Promove limpeza no ar, rega as plantações, enche os rios e lagos, onde pode ser utilizada para diversos fins.",
                "Você só terá dor de cabeça com a logística da sua empresa se assim, escolher. Gaste as suas energias no seu negócio e deixe-nos resolver todos os desafios de logística."]
    frases = choice(textos)

    return render_template("homepage.html", frases=frases)

@app.route('/prices')
def price():
    return render_template('prices.html')
@app.route('/orcamento', methods=["GET", "POST"])
def orcamento():

    session.clear()

    if request.method == "POST":
        if not request.form.get("company_name"):
            return render_template('apology.html')
        elif not request.form.get("email"):
            return render_template('apology.html')
        elif not request.form.get('collector'):
            return render_template('apology.html')
        elif not request.form.get("delivery"):
            return render_template('apology.html')
        elif not request.form.get("km"):
            return render_template('apology.html')


        new_user = db.execute("INSERT INTO companys (company,email, collect_adress, delivery_adress, price, km) VALUES (:company_name,:email,:collector,:delivery,:price, :km)", company_name=request.form.get("company_name"), email=request.form.get("email"), collector=request.form.get("collector"), delivery=request.form.get("delivery"),price=request.form.get("price"), km=request.form.get("km"))

        session['user_id'] = new_user



        return redirect("/")
    else:
        return render_template('orcamento.html')

@app.route('/history', methods=['GET', 'POST'])
def history():

    session.clear()

    if request.method == 'POST':
        if not request.form.get('company'):
            return render_template('apology.html')
        history = db.execute("SELECT company, collect_adress, delivery_adress, price, km, register_at FROM companys WHERE company = :company", company=request.form.get('company'))
        return render_template('history.html', history=history)
    else:
        return render_template('history.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
