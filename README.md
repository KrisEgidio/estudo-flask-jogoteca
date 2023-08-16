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