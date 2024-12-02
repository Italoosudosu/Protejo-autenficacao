from flask import Flask, render_template, redirect, request
import psycopg2 
from sqlalchemy import create_engine, text
import pg8000





engine = create_engine('postgresql+pg8000://postgres:postgres@127.0.0.1/crudProject')
app = Flask(__name__)
app.config['SECRET_KEY'] = 'ITALO_OGOMES'
 


@app.route('/')
def home():
    return render_template("login.html")

@app.route('/login', methods=['POST']) 
def login():
    
    nome = request.form.get('nome')
    senha = request.form.get('senha')
    print(nome, senha)
    try:
        with engine.connect() as connection:
            print("Conexão bem-sucedida!")
    except Exception as e:
        print("Erro ao conectar ao banco de dados:", e)
    with engine.connect() as connection:
        result = connection.execute(text(f"INSERT INTO public.users(nome, senha) VALUES('{nome}','{senha}')") )
        connection.commit()

    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)



