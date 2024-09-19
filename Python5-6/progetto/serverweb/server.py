from flask import Flask, render_template, request
utenti = [['franco','Rossi','M','0'],
          ['Nico','Bonnetti','M','0'],
          ['Gianna','Berti','M','0'],
          ['Nico','Giraldi']]
        

api = Flask("__name__")


@api.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@api.route('/registrati', methods=['GET'])
def form():
    nome = request.args.get('fname')
    cognome = request.args.get('lname')
    for utente in utenti:
        if nome == utente[0] and cognome == utente[1]:
            return render_template('risposta.html', nome=nome, cognome= cognome)
    
    return render_template('ko.html')


api.run(host="0.0.0.0", port=8085)
