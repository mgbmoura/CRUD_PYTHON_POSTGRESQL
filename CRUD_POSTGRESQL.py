import psycopg2


# "C"| "R"| "U"|"D" = Com o SGBD: "POSTGRESQL", EM PYTHON: 
#  R |  E |  P | E    
#  E |  A |  D | L    **OBSERVAÇÔES:"Neste código, criei o Banco de dados ao meu modo, você pode criar ao seu e 
#  A |  D |  A | E      substituir valores, tals quais coloquei como exemplo."**
#  E |    |  E | E 




#CRIANDO CONEXÃO(Para conectar, digite os dados entre as áspas):
conexao = psycopg2.connect(
    database=#'Nome de um banco de  dados existente',
    user=#'Digite o nome de usuário(Sugestão:Postgres',
    password=#'Digite sua senha de acesso do SGBD'
)
#CRIANDO CURSOR:
C = conexao.cursor()







#                                     _________________________
                                       
                                        ## C O M A N D O S ##
#                                     _________________________




# COMANDO 1 e 2 ( C R E A T E ) **OBS: CONSIDEREI O COMANDO INSERT, JUNTAMENTE COM O CREATE**:

# Este comando cria uma tabela, considere comentar ele logo após commita-lo:
# comando1 = ("""CREATE TABLE Digite o nome da tabela(
# id integer NOT NULL,
# nome character varying(255),
# sobrenome character varying(255),
# email character varying(255),
# telefone integer)""")
# print('tabela criada com exito')
# C.execute(comando1)
# conexao.commit() 

# #VARIÁVEIS
id = "Digite um nº ID"
nome = 'Digite um nome'

# Este comando insere dados na tabela criada ou existente:
comando2 = (f"INSERT INTO aluno values({id}, '{nome}')")
print('dados inseridos corretamente')
c.execute(comando2)
conexao.commit()


# COMANDO 3 ( R E A D )
# Este comando retorna uma lista de tuplas com dados da tabela selecionada:
#comando3 = ('SELECT * FROM Digite o nome da tabela')
#c.execute(comando)
#consulta=cursor01.fetchall()


# COMANDO 4 ( U P D A T E ):
# Este comando atualiza um específico dado da tabela:

# Variáveis:
#nome = 'Digite um nome'
#cpf = 11223344556

#comando4 = (f"UPDATE aluno SET cpf = {cpf} WHERE nome = '{nome}'")
#cursor01.execute(comando)
#conexao.commit()


# COMANDO 5 ( D E L E T E ):
# Este comando exclui um dado existente na tabela:

# Variáveis:
# nome = 'Digite um nome'

# comando5 = (f"DELETE FROM aluno WHERE nome = '{nome}'")
# C.execute(comando)
# conexao.commit()




conexao.close
conexao.close
