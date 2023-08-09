## Algumas anotações da aulas

<br>

| 🪧  | Vitrine.Dev |                                                        |
|-----|-------------|--------------------------------------------------------|
| ✨   | Nome        | 	Jogoteca                                              |
| 🏷️ | Tecnologias | 	Python, Flask, PyCharm                                |
| 🚀  | URL         | 	#                                                     |
| 🤿  | Desafio     | 	Criar uma aplicação com listagem de jogo, a jogoteca. |
| 🏅  | Curso       | 	Alura - Flask: crie uma webapp com Python             |

<br>

### 01. Criando uma aplicação web super rápido

-  Preparação do ambiente:
    - Instalação do python3
    - Instalação do PyCharm


- O que é flask?
  - É um microframework para aplicações web de código aberto.Conhecido por sua facilidade, praticidade e eficiência.


- Criação do projeto:
  - Criar um projeto no pycharm (com a virtualenv)
  - Importar o flask com `from flask import Flask` e instalar com `pip install flask`
  - Para iniciar a aplicação inserir `app = Flask(__name__)`
  - Parar criar uma rota `@app.route('/')` e abaixo definir a função
  - Para renderizar um arquivo html utilizar `render_template('arquivo.html')` e `from flask import Flask, render_template`
  - E no final do arquivo usar o `@app.run()` para levantar a aplicação

    
### 02. Listando jogos usando o Flask

- Para adicionar arquivos dinâmicos no html, utilizamos `{{variavel}}` e passar por parâmetro `render_template('arquivo.html', variavel='valor')` 
- Parar criar uma estrutura de repetição dentro do arquivo html utiliza-se `{% for jogo in jogos %} bloco_de_repeticao {% endfor %}`