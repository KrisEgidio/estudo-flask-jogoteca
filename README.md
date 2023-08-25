## Algumas anotações da aulas

<br>

| 🪧  | Vitrine.Dev |                                                        |
|-----|-------------|--------------------------------------------------------|
| ✨   | Nome        | 	Jogoteca                                              |
| 🏷️ | Tecnologias | 	Python, Flask, PyCharm                                |
| 🚀  | URL         | 	#                                                     |
| 🤿  | Desafio     | 	Criar uma aplicação com listagem de jogo, a jogoteca. |
| 🏅  | Formação    | 	Alura - Começando com Flask: framework web de Python  |

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
  - O `Jinja2` é o motor que renderiza o template no Flask
     
      - `upper`: colocar os caracteres em caixa alta;
      - `round`: arredondar números;
      - `trim`: remover espaços do início e do fim do texto;
      - `default('texto exibido por padrão')` - quando queremos mostrar algo, caso a variável esteja vazia ou nula.
        
     <br>
    
      - Tipos de Delimitadores do Jinja2:

      - `{%....%}`: usado para inserir estruturas Python dentro de um arquivo html;
      - `{{....}}`: usado para facilitar a exibição de código python como um output em um template HTML. Alternativa: {% print(....) %};
      - `{#....#}`: usado para adicionar comentários que não serão exibidos no output do template HTML.
  

### 03. Criação de um novo jogo

- Usar o debug para não precisar reiniciar o servidor em toda alteração `@app.run(debuh=True)`
- Atribuir em uma rota o métodos com `@app.route('/nome-da-rota', methods=['POST',])`
- Importar e utilizar o helper do flask `request` para receber as informações enviadas do formulário

### 04. Melhorando o código e a usabilidade

- O helper `redirect` serve para redirecionar a página para outra rota
- A pasta `static` serve para guardar os arquivos css. Use a diretiva `url_for` para indicar o caminho do arquivo e criar uma url dinâmica
- Para melhorar o código, é possível utilizar templates e estender para outras páginas para não repetir código
  - Utilize as diretivas como as de exemplo `{% block conteudo %}{% endblock %}` e para estender um template `{% extends "template.html" %}`

### 05. Autenticando usuários com sessão do Flask

- O flask utiliza os `cookies` para armezar dados no client-side e para salvar os dados da sessão, necessário criar uma `secret_key` para criptografia desses dados
  - Importar o helper `session`
  - A `secret_key` deve ser inserida após a instância de criação do flash `app.secret_key = 'alura'`
  - Para salvar dados da sessão utilizar `session['usuario_logado'] = request.form['usuario']`
  - Parar remover dados da sessão `session['usuario_logado'] = None`
- Mensagens `flash`são ótimas para informar usuário sobre solicitações realizadas na aplicação
  - Importar o helper `flash`
  - Para criar a mensagem flash `flash('Logout efetuado com sucesso!')`
  - Para exibir a mensagem flash no html:
  

  ````python
  {% with messages = get_flashed_messages() %}
            {% if messages %}
                <ul id="messages" class="list-unstyled">
                {% for message in messages %}
                    <li class="alert alert-success">{{ message }}</li>
                {% endfor %}
                </ul>
            {% endif %}
        {% endwith %}
  ````

### 06. Implementando autorização para criar Jogos

- Para obter as querys strings da url deve-se utilizar `request.args.get('key')` 
- Boas práticas com url é utilizar elas de forma dinâmica com `url_for('nome_do_metodo')`


### 07. Persistência com MySQL

- Instalar o mysql com `pip3.exe install mysqlclient`
- Instalar o mysql conector para rodar o script para criar o banco de dados e suas tabelas `pip install mysql-connector-python==8.0.28`
- Utilizar o ORM `SQLALchemy` e instalar `pip install flask-sqlalchemy==2.5.1`
- Instanciar o banco de dados com `db = SQLAlchemy(app)` (não esqueça de importar a biblioteca)
- Conectar o banco de dados

```python
app.config['SQLALCHEMY_DATABASE_URI'] = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}?collation=utf8mb4_general_ci'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = 'admin',
        servidor = 'localhost',
        database = 'jogoteca'
    )
```

- Criar classes para se comunicar com as tabelas do banco de dados

````pyhton
class Jogos(db.Model)
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(40), nullable=False)
    console = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name
````

- Ambos os métodos internos __str__ e __repr__ são muito utilizados para a construção de classes na linguagem Python. Enquanto o __str__ tem como foco o usuário final daquela classe, o método __repr__ tem como objetivo mostrar uma versão em string para a pessoa programadora quando a classe é acessada em modo interativo.
- Para realizar querys `Jogos.query.order_by(Jogos.id)`
