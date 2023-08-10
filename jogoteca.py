from flask import Flask, render_template

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome=nome
        self.categoria=categoria
        self.console=console

app = Flask(__name__)

@app.route('/inicio')
def ola():
    jogo1=Jogo('Tetris', 'Puzzle', 'Ataria')
    jogo2=Jogo('LOL', 'MMORPG', 'PC')
    lista=[jogo1, jogo2]
    return render_template('lista.html', titulo='Jogos', jogos=lista)

app.run()