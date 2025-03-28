import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'sua-chave-secreta-aqui'  # Substitua por uma chave segura

db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html', user_email="teste@example.com", frase="Bem-vindo ao site-simples!", user_type="client")

if __name__ == '__main__':
    app.run(debug=True)