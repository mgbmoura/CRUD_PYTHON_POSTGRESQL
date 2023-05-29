import psycopg2


# "C"| "R"| "U"|"D" = Com o SGBD: "POSTGRESQL", EM PYTHON: 
#  R |  E |  P | E    
#  E |  A |  D | L    **OBSERVAÇÔES:"Neste código, criei o Banco de dados ao meu modo, você pode criar ao seu e 
#  A |  D |  A | E      substituir valores, tals quais coloquei como exemplo."**
#  E |    |  E | E 




# CRIANDO CONEXÃO (Para conectar, digite os dados entre as aspas):
 conexao = psycopg2.connect(
 database='Nome de um banco de dados existente',
 user='Digite o nome de usuário (Sugestão: postgres)',
 password='Digite sua senha de acesso do SGBD'
)

# CRIANDO CURSOR:
cursor = conexao.cursor()

# COMANDOS

# COMANDO 1 e 2 (CREATE)
# Este comando cria uma tabela, considere comentar logo após executá-lo:
# comando1 = ("""
#         CREATE TABLE NomeDaTabela (
#         id SERIAL PRIMARY KEY,
#         nome character varying(255),
#         sobrenome character varying(255),
#         email character varying(255),
#         telefone integer)""")

# cursor.execute(comando1)
# conexao.commit()
# print('Tabela criada com êxito.')

# VARIÁVEIS
id = "Digite um número ID"
nome = "Digite um nome"

# Este comando insere dados na tabela criada ou existente:
comando2 = f"INSERT INTO aluno (id, nome) VALUES ('{id}', '{nome}')"
cursor.execute(comando2)
conexao.commit()
print('Dados inseridos corretamente!')

# COMANDO 3 (READ)
# Este comando retorna uma lista de tuplas com dados da tabela selecionada:
# comando3 = "SELECT * FROM NomeDaTabela"
# cursor.execute(comando3)
# consulta = cursor.fetchall()

# COMANDO 4 (UPDATE)
# Este comando atualiza um dado específico da tabela:

# Variáveis:
# novo_nome = 'Digite um nome'
# novo_cpf = 11223344556

# comando4 = f"UPDATE aluno SET cpf = {novo_cpf} WHERE nome = '{novo_nome}'"
# cursor.execute(comando4)
# conexao.commit()

# COMANDO 5 (DELETE)
# Este comando exclui um dado existente na tabela:

# Variáveis:
# nome = 'Digite um nome'

# comando5 = f"DELETE FROM aluno WHERE nome = '{nome}'"
# cursor.execute(comando5)
# conexao.commit()

# Fechando a conexão e o cursor:
cursor.close()
conexao.close()
