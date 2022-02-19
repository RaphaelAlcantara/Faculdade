# coding: utf-8
#Digite no terminal python pip install mysql-connector-python
import mysql.connector
import time
     
#def exibirNaTela():

#FUNCOES      
def sucesso(str):
    time.sleep(2)
    print(f"{str} criado!")
      
def exibeTuplas(str):
    print(f"Exibindo os {str} na tela...")
    time.sleep(2)
    sqlExibir = f"SELECT * FROM {str}"
    cursor.execute(sqlExibir)
    resultadoConsulta = cursor.fetchall()
    for x in resultadoConsulta:
        print(x) 
     
print("Iniciando conexão")
time.sleep(1)
print("Inserindo credenciais...")

banco = mysql.connector.connect(
  host="localhost",
  port="3306",
  username="root",
  password="",
  #database="Infortech"
)

time.sleep(1)
cursor = banco.cursor()
print("Banco conectado")
time.sleep(1)

#DATABASE
database = "CREATE DATABASE IF NOT EXISTS infortech"
#TABELA CARGOS
cargos = "CREATE TABLE IF NOT EXISTS cargos(\
      id int NOT NULL auto_increment,\
      id_dpt int NOT NULL,\
      id_func int NOT NULL,\
      nome VARCHAR(64) NOT NULL,\
      quantidade INT, \
      PRIMARY KEY(id),\
      FOREIGN KEY (id_dpt)\
      REFERENCES departamentos(id),\
      FOREIGN KEY (id_func)\
      REFERENCES funcionarios(id))"
#TABELA DEPARTAMENTOS
departamentos = "CREATE TABLE IF NOT EXISTS departamentos(\
      id int NOT NULL auto_increment,\
      id_func int NOT NULL,\
      nome VARCHAR(64) NOT NULL,\
      descricao VARCHAR(64) NOT NULL,\
      quantidade INT NOT NULL,\
      PRIMARY KEY(id),\
      FOREIGN KEY (id_func) REFERENCES funcionarios(id))"
#TABELA FUNCIONARIOS
funcionarios = "CREATE TABLE IF NOT EXISTS funcionarios(\
      id int NOT NULL auto_increment,\
      nome VARCHAR(64) NOT NULL,\
      DATA_NASC DATE NOT NULL,\
      logradouro VARCHAR(64) NOT NULL,\
      BAIRRO VARCHAR(32) NOT NULL,\
      CIDADE VARCHAR(64) NOT NULL,\
      CEP VARCHAR(32) NOT NULL,\
      COMPLEMENTO VARCHAR(64),\
      ESTADO VARCHAR(32) NOT NULL,\
      PRIMARY KEY(id))"
#TABELA ESTOQUE
estoque = "CREATE TABLE IF NOT EXISTS estoque(\
      id int NOT NULL auto_increment,\
      id_pedfor int NOT NULL,\
      nome VARCHAR(64) NOT NULL,\
      quantidade INT NOT NULL,\
      categoria VARCHAR(64) NOT NULL,\
      PRIMARY KEY(id),\
      FOREIGN KEY (id_pedfor) REFERENCES pedidofornecedor(id))"
#TABELA PEDIDOS FORNECEDOR
pedidofornecedor = "CREATE TABLE IF NOT EXISTS pedidofornecedor(\
      id int NOT NULL auto_increment,\
      CNPJ_FORNECEDOR VARCHAR(32) NOT NULL,\
      descricao VARCHAR(64) NOT NULL,\
      quantidade INT NOT NULL,\
      valor FLOAT NOT NULL,\
      PRIMARY KEY(id),\
      FOREIGN KEY (CNPJ_FORNECEDOR) REFERENCES fornecedores(CNPJ))" 
#TABELA SETOR
setor = "CREATE TABLE IF NOT EXISTS setor(\
      id int NOT NULL auto_increment,\
      id_prod int NOT NULL,\
      id_estq int NOT NULL,\
      nome VARCHAR(32) NOT NULL,\
      PRIMARY KEY(id),\
      FOREIGN KEY (id_prod) REFERENCES produtos(id),\
      FOREIGN KEY (id_estq) REFERENCES estoque(id))"
#TABELA PRODUTOS
produtos = "CREATE TABLE IF NOT EXISTS produtos(\
      id int NOT NULL auto_increment,\
      nome VARCHAR(64) NOT NULL,\
      descricao VARCHAR(128) NOT NULL,\
      valor FLOAT NOT NULL,\
      PRIMARY KEY(id))"
#TABELA PEDIDOS
pedidos = "CREATE TABLE IF NOT EXISTS pedidos(\
      id int NOT NULL auto_increment,\
      id_func int NOT NULL,\
      descricao VARCHAR(64) NOT NULL,\
      quantidade INT NOT NULL,\
      valor FLOAT NOT NULL,\
      PRIMARY KEY(id),\
      FOREIGN KEY (id_func) REFERENCES funcionarios(id))"
#TABELA FORNECEDOR
fornecedor = "CREATE TABLE IF NOT EXISTS fornecedores(\
      CNPJ VARCHAR(32) NOT NULL,\
      nome VARCHAR(64) NOT NULL,\
      logradouro VARCHAR(64) NOT NULL,\
      BAIRRO VARCHAR(64) NOT NULL,\
      CIDADE VARCHAR(32) NOT NULL,\
      CEP VARCHAR(32) NOT NULL ,\
      COMPLEMENTO VARCHAR(64),\
      ESTADO VARCHAR(32) NOT NULL,\
      PRIMARY KEY(CNPJ))"
#TABELA TELEFONE
telefone = "CREATE TABLE IF NOT EXISTS telefone(\
      id int NOT NULL auto_increment,\
      id_cli int NOT NULL,\
      CNPJ_FORNECEDOR VARCHAR(32) NOT NULL,\
      id_func int NOT NULL,\
      telefone VARCHAR(32) NOT NULL,\
      PRIMARY KEY(id),\
      FOREIGN KEY (id_cli) REFERENCES cliente(id),\
      FOREIGN KEY (CNPJ_FORNECEDOR) REFERENCES fornecedores(CNPJ),\
      FOREIGN KEY (id_func) REFERENCES funcionarios(id))"
#TABELA CLIENTES
clientes = "CREATE TABLE IF NOT EXISTS cliente(\
      id int NOT NULL auto_increment,\
      CPF VARCHAR(32) NOT NULL,\
      nome VARCHAR(64) NOT NULL,\
      DATA_NASC DATE NOT NULL,\
      logradouro VARCHAR(64) NOT NULL,\
      BAIRRO VARCHAR(32) NOT NULL,\
      CIDADE VARCHAR(64) NOT NULL,\
      CEP VARCHAR(32) NOT NULL,\
      COMPLEMENTO VARCHAR(64),\
      ESTADO VARCHAR(32) NOT NULL,\
      PRIMARY KEY(id, CPF))"
#TABELA STATUSPEDIDO
status = "CREATE TABLE IF NOT EXISTS statuspedido(\
      id int NOT NULL auto_increment,\
      id_ped int NOT NULL,\
      statuspedido VARCHAR(32) NOT NULL,\
      PRIMARY KEY(id),\
      FOREIGN KEY (id_ped) REFERENCES pedidos(id))"
#TABELA PAGAMENTOS
pagamentos = "CREATE TABLE IF NOT EXISTS pagamentos(\
      id int NOT NULL auto_increment,\
      id_status int NOT NULL,\
      id_func int NOT NULL,\
      id_cli int NOT NULL,\
      valor_total FLOAT NOT NULL,\
      data_hora DATE NOT NULL,\
      descricao VARCHAR(128) NOT NULL,\
      PRIMARY KEY(id),\
      FOREIGN KEY (id_status) REFERENCES statuspedido(id),\
      FOREIGN KEY (id_func) REFERENCES funcionarios(id),\
      FOREIGN KEY (id_cli) REFERENCES cliente(id))"
#TABELA METODOPAGAMENTO
mtdpagamento = "CREATE TABLE IF NOT EXISTS metodopagamento(\
      id int NOT NULL auto_increment,\
      id_pag int NOT NULL,\
      descricao VARCHAR(32) NOT NULL,\
      PRIMARY KEY(id),\
      FOREIGN KEY (id_pag) REFERENCES pagamentos(id))"

#CRIANDO DATABASE
print("Criando Database...")
cursor.execute(database)
cursor.execute("USE infortech")

#CRIAÇÃO DAS TABELAS

#Criar tabela funcionarios
cursor.execute(funcionarios)
#Criar tabela fornecedor
cursor.execute(fornecedor)
#Criar tabela telefone
cursor.execute(telefone)
#Criar tabela clientes
cursor.execute(clientes)
#Criar tabela produtos
cursor.execute(produtos)
#Criar tabela pedidofornecedor
cursor.execute(pedidofornecedor)
#Criar tabela departamentos
cursor.execute(departamentos)
#Criar tabela estoque
cursor.execute(estoque)
#Criar tabela setor
cursor.execute(setor)
#Criar tabela cargos
cursor.execute(cargos)
#Criar tabela pedidos
cursor.execute(pedidos)
#Criar tabela status
cursor.execute(status)
#Criar tabela pagamentos
cursor.execute(pagamentos)
#Criar tabela mtdpagamento
cursor.execute(mtdpagamento)
time.sleep(2)
print("Banco criado")

# Menu Principal
opcao = 0

while opcao != "6":
    opcao = input("O que deseja fazer?\n"
                "(1) Produtos\n"
                "(2) Clientes\n"
                "(3) Fornecedores\n"
                "(4) Estoque\n"
                "(5) Funcionários\n"
                "(6) Sair da Aplicação\n")

    # Menu Produtos
    if(opcao == "1"):
        opcaoProd = input("O que deseja fazer?\n"
                "(1) Inserir novo produto\n"
                "(2) Modificar produto\n"
                "(3) Remover produto\n"
                "(4) Exibir produtos\n"
                "(5) Retornar ao Menu Principal")
        
        if(opcaoProd == "1"): # Inserir novo produto
                nomeProd = input("Digite o nome do produto: ")
                descricaoProd = input("Digite uma breve descrição do produto: ")
                valorProd = input("Digite o valor do produto: ")
                sqlInserirProdutos = f"INSERT INTO PRODUTOS (nome, descricao, valor) VALUES ('{nomeProd}', '{descricaoProd}', '{valorProd}')"
                cursor.execute(sqlInserirProdutos)
                sucesso("Produto")
                
        elif(opcaoProd == "2"): # Modificar produto
                exibeTuplas("produtos")
                    
                idTupla = input("Digite o ID da tupla que deseja modificar: ")
                colunaParaModif = input("Insira o nome da coluna que deseja modificar: ")
                novoConteudo = input("Insira um novo conteúdo para essa tabela: ")
                
                sqlModificarTabela = (f"UPDATE PRODUTOS SET {colunaParaModif} = '{novoConteudo}' WHERE id = '{idTupla}'")
                
                cursor.execute(sqlModificarTabela)
                time.sleep(2)
                print(f"Coluna {colunaParaModif} da tabela PRODUTOS modificada com sucesso.")
                
        elif(opcaoProd == "3"): # Remover produto
                exibeTuplas("produtos")
                
                nomeProdRemover = input("Digite o nome do produto que você deseja remover.")
                sqlRemoverProd = f"DELETE FROM PRODUTOS WHERE nome = '{nomeProdRemover}'"
                decisaoRemover = input("Você tem certeza de que deseja fazer essa remoção na tabela PRODUTOS?[Y/N]")
                
                if(decisaoRemover == "Y" or "y"):
                    cursor.execute(sqlRemoverProd)
                    time.sleep(2)
                    print("Produto removido!")
                
                elif(decisaoRemover == "N" or "n"):
                    print("Você optou por não remover um produto da tabela PRODUTOS.")
                
                else:
                    print("Opção de decisão inválida! Era para ser Y ou N")
        
        elif(opcaoProd == "4"): # Exibir produtos
                exibeTuplas("produtos")
                
        else: # OpcaoProd Inválida
                print("Digitastes uma opção inválida do Menu de Produtos.\n")
                    

    # Menu Clientes
    elif(opcao == "2"):
        opcaoCli = input("O que deseja fazer?\n"
                "(1) Cadastrar Cliente\n"
                "(2) Modificar Dados do Cliente\n"
                "(3) Remover Cliente\n"
                "(4) Visualizar Lista de Clientes\n")
        
        if(opcaoCli == "1"): # Cadastrar Cliente
                nome = input("Digite o nome do novo cliente: ")
                CPF = input("Digite o CPF do cliente(000.000.000-00): ")
                dataNasc = input("Digite a data de nascimento(YYYY-MM-DD): ")
                logradouro = input("Digite a rua do cliente: ")
                bairro = input("Digite o bairro do cliente: ")
                cidade = input("Digite a cidade do cliente: ")
                CEP = input("Digite o CEP do cliente(00000-000): ")
                complemento = input("Digite o complemento, caso haja: ")
                estado = input("Digite a UF do cliente: ")
                
                sqlCadastrarCliente = "INSERT INTO CLIENTE (nome, CPF, DATA_NASC, logradouro, bairro, cidade,\
                                    CEP, COMPLEMENTO, ESTADO) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                varCadastrarCliente = (nome, CPF, dataNasc, logradouro, bairro, cidade, CEP, complemento, estado)
                cursor.execute(sqlCadastrarCliente, varCadastrarCliente)
                time.sleep(2)
                print("Cliente cadastrado!")            
        elif(opcaoCli == "2"): # Modificar Dados do Cliente
                True
        elif(opcaoCli == "3"): # Remover Cliente
                exibeTuplas("cliente")
                
                cpfIdentRemover = input("Digite o CPF do cliente o qual deseja remover da lista: ")
                decisaoRemover = input("Tem certeza de que deseja remover esse cliente? [Y/N]: ")
                if(decisaoRemover == "Y" or "y"):
                    sqlRemoverCli = "DELETE FROM CLIENTE WHERE CPF = %s"
                    cursor.execute(sqlRemoverCli, (cpfIdentRemover,))
                    time.sleep(2)
                    print("Cliente removido!")
                elif(decisaoRemover == "N" or decisaoRemover == "n"):
                    print("Você optou por não remover o cliente.")
                else:
                    print("Você digitou uma opção inválida, deveria ser Y ou N.")
                                
        elif(opcaoCli == "4"): # Visualizar Lista de Clientes
                exibeTuplas("Cliente")
        else: # OpcaoCli Inválida 
                print("Digitastes uma opção inválida do Menu de Clientes.\n")
        
    #Menu Fornecedores
    elif(opcao == "3"):
        opcaoForn = input("O que deseja fazer?\n"
                "(1) Cadastrar Fornecedor\n"
                "(2) Modificar Dados do Fornecedor\n"
                "(3) Remover Fornecedor\n"
                "(4) Visualizar Lista de Fornecedores\n")
        
        if(opcaoForn == "1"): # Cadastrar Fornecedor
                nome = input("Digite o nome do novo fornecedor: ")
                CNPJ = input("Digite o CNPJ do fornecedor(00.000.000/0001-00): ")
                logradouro = input("Digite a rua do fornecedor: ")
                bairro = input("Digite o bairro do fornecedor: ")
                cidade = input("Digite a cidade do fornecedor: ")
                CEP = input("Digite o CEP do fornecedor(00000-000): ")
                complemento = input("Digite o complemento, caso haja: ")
                estado = input("Digite a UF do fornecedor: ")
                
                sqlCadastrarFornecedor = "INSERT INTO FORNECEDORES (nome, CNPJ, logradouro, bairro, cidade,\
                                    CEP, COMPLEMENTO, ESTADO) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                varCadastrarFornecedor = (nome, CNPJ, logradouro, bairro, cidade, CEP, complemento, estado)
                cursor.execute(sqlCadastrarFornecedor, varCadastrarFornecedor)
                time.sleep(2)
                print("Fornecedor cadastrado!")
        elif(opcaoForn == "2"): # Modificar Dados do Fornecedor
                True
        elif(opcaoForn == "3"): # Remover Fornecedor
                exibeTuplas("FORNECEDORES")
                cnpjIdentRemover = input("Digite o CNPJ do fornecedor o qual quer excluir: ")
                decisaoRemover = input("Desejas mesmo remover esse fornecedor da lista? [Y/N]: ")
                if(decisaoRemover == "Y" or decisaoRemover == "y"):
                    sqlRemoverForn = "DELETE FROM FORNECEDORES WHERE CNPJ = %s"
                    cursor.execute(sqlRemoverForn, (cnpjIdentRemover,))
                    time.sleep(2)
                    print("Fornecedor removido!")
                elif(decisaoRemover == "N" or decisaoRemover == "n"):
                    print("Você optou por não remover o fornecedor.")
                else:
                    print("Opção inválida, deveria ter colocado Y ou N.")
                
        elif(opcaoForn == "4"): # Visualizar Lista de Fornecedores
                exibeTuplas("FORNECEDORES")
        else: # OpcaoForn Inválida
                print("Digitastes uma opção inválida do Menu de Fornecedores.\n")
        
    #Menu Estoque
    elif(opcao == "4"):
        opcaoEstq = input("O que deseja fazer?\n"
                "(1) Produtos\n"
                "(2) Clientes\n"
                "(3) Fornecedores\n"
                "(4) Estoque\n"
                "(5) Funcionários\n")
        if():
                True
        elif():
                True
        elif():
                True
        elif():
                True
        else:
                True
        
    #Menu Funcionários
    elif(opcao == "5"):
        opcaoFunc = input("O que deseja fazer?\n"
                "(1) Registrar funcionário\n"
                "(2) Modificar dados de um funcionário\n"
                "(3) Remover funcionário\n"
                "(4) Visualizar lista de funcionários\n")
        if(opcaoFunc == "1"): # Registrar funcionário
                nome = input("Digite o nome do novo funcionário: ")
                dataNasc = input("Digite a data de nascimento(YYYY-MM-DD): ")
                logradouro = input("Digite a rua do funcionário: ")
                bairro = input("Digite o bairro do funcionário: ")
                cidade = input("Digite a cidade do funcionário: ")
                CEP = input("Digite o CEP do funcionário(00000-000): ")
                complemento = input("Digite o complemento, caso haja: ")
                estado = input("Digite a UF do funcionário: ")
                
                sqlRegistrarFuncionario = "INSERT INTO FUNCIONARIOS \
                                        (nome, data_nasc, logradouro, bairro, cidade, CEP, complemento, estado) VALUES\
                                        (%s, %s, %s, %s, %s, %s, %s, %s)"
                varRegistrarFuncionario = (nome, dataNasc, logradouro, bairro, cidade, CEP, complemento, estado)
                cursor.execute(sqlRegistrarFuncionario, varRegistrarFuncionario)
                time.sleep(2)
                print("Funcionário registrado!")                                   
                                        
        elif(opcaoFunc == "2"): # Modificar dados de um funcionário
                True
        elif(opcaoFunc == "3"): # Remover funcionário
                exibeTuplas("FUNCIONARIOS")
                    
                idIdentRemover = input("Digite o ID do funcionário que deseja remover: ")
                decisaoRemover = input("Você realmente deseja remover esse funcionário?![Y/N]: ")
                if(decisaoRemover == "Y" or decisaoRemover == "y"):
                    sqlRemoverFunc = "DELETE FROM FUNCIONARIOS WHERE ID = %s"
                    cursor.execute(sqlRemoverFunc, (idIdentRemover,))
                    time.sleep(2)
                    print("Funcionário removido!")
                elif(decisaoRemover == "N" or decisaoRemover == "n"):
                    print("Você decidiu não remover o funcionário.")
                else:
                    print("Opção inválida. Deveria ter escolhido algo entre Y e N.")
        elif(opcaoFunc == "4"): # Visualizar lista de funcionários
                exibeTuplas("FUNCIONARIOS")
        else: # OpcaoFunc Inválida
                print("Digitastes uma opção inválida do Menu de Funcionários.\n")

    #Opção Inválida
    elif(opcao == "6"):
        print("Até logo!")
    else:
        print("Digitastes uma opção inválida do Menu Principal.\n")