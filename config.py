SECRET_KEY = 'alura'

SQLALCHEMY_DATABASE_URI = \
    "{SGBD}://{usuario}:{senha}@{servidor}/{database}?collation=utf8mb4_general_ci".format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = '',
        servidor = '127.0.0.1',
        database = 'jogoteca'
    )
