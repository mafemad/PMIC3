from flask import Flask, render_template, url_for, request
from flask_mysqldb import MySQL


app = Flask("__name__")


#conexão ao banco 
app.config['MYSQL_Host'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Mafemad2005!'
app.config['MYSQL_DB'] = 'desafio3'

mysql = MySQL(app)



@app.route("/")
def home():
    return render_template("home.html", background= url_for('static', filename='imagens/fundo.png'))

@app.route("/quemsomos")
def quemsomos():
    return render_template("quemsomos.html", background= url_for('static', filename='imagens/fundo2.png'))

@app.route("/contato" , methods=['GET' , 'POST'])
def contato():
    if request.method == "POST":
        email = request.form['email']
        assunto = request.form['assunto']
        descricao = request.form['descricao']
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contatos(email, assunto, descricao) VALUES (%s, %s, %s)", (email, assunto, descricao))
       
        mysql.connection.commit()
        
        cur.close()

        return 'sucesso'
    return render_template('contato.html', background= url_for('static', filename='imagens/fundo2.png'))

@app.route("/usuarios")
def usuarios():
    cur = mysql.connection.cursor()

    users = cur.execute("SELECT * FROM contatos")

    if users > 0:
        userDetails = cur.fetchall()

        return render_template("usuarios.html", userDetails=userDetails, background= url_for('static', filename='imagens/fundo2.png'))


app.run(debug=True)