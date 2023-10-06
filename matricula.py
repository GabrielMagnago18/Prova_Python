import time


def confere_ultima_matricula():
    arq = open(r"C:\Usuários\Usuario\matriculas.txt", 'r')
    matricula = 0000
    for line in arq:
        matricula += 0o1
    arq.close()
    return str(matricula)


def dados_dos_aluno(line):
    print(f"Matrícula: {line[0]}")
    print(f"Nome Completo: {line[1]}")
    print(f"Sexo: {line[2]}")
    print(f"Endereço: {line[3]}")
    print(f"Contato: {line[4]}")
    print(f"Email: {line[5]}")
    print(f"Curso: {line[6]}")
    print("\n")



def consultas(valor):
    #valor 0 = matricula
    #valor 1 = nome
    #valor 6 = curso
    if valor == 0:
        texto = 'matricula'
    elif valor == 1:
        texto = 'nome'
    elif valor == 6:
        texto = 'curso'
    consulta = input(f"Coloque {texto} desejado: ")
    arq = open(r"C:\Usuários\Usuario\matriculas.txt", 'r')
    for line in arq:
        dados = line.split(';')
        search = line.split(';')[valor]
        if consulta == search:
            dados_dos_aluno(dados)            
    arq.close()





while True:
    print("___________")
    print("SISTEMA DE CADASTRO DE ALUNOS")
    print("Cadastrar novo usuário [0]")
    print("Fazer consulta de aluno [1]")
    print("Sair do sistema [2]")
    opcao = input("ESCOLHA UMA OPCAO: ")
    if opcao == '0':
        print("___________")
        nome = input("Insira o nome completo: ")
        sexo = input("Insira seu sexo, M ou F: ")
        endereco = input("Rua e numero: ")
        contato = input("Insira seu contato: ")
        email = input("Insira seu email: ")
        curso = input("""
        1.0 Ingles
        1.1 Ingles e frances
        1.2 Ingles e espanhol
        1.3 Ingles frances e espanhol
        -------------------------------
        2.0 Frances
        2.1 Frances e ingles
        2.2 Frances e espanhol
        2.3 Frances e ingles e espanhol
        -------------------------------
        3.0 Espanhol
        3.1 Espanhol e Ingles
        3.2 Espanhol e Frances
        3.3 Espanhol Ingles e Frances
        
        ESCOLHA A OPÇÃO DO CURSO: """)
        arq = open(r"C:\Usuários\Usuario\matriculas.txt", 'a')
        cadastro=nome+';'+sexo+';'+endereco+';'+contato+';'+email+';'+curso+';'
        ultima_matricula = confere_ultima_matricula()
        arq.write(ultima_matricula+';'+cadastro+'\n')
        arq.close()
        print("Cadastrando aluno....")
        time.sleep(2)
        print("Aluno cadastrado com sucesso!")
        print("\n")
        continue
        
        
    elif opcao == '1':
        print("___________")
        print("DIGITE O TIPO DE COLSULTA")
        print("""
        Por Matrícula [0]
        Por Nome [1]
        Por Curso [2]
        Retornar [3]
        """)
        
        consulta = input("ESCOLHA A OPÇÃO DE CONSULTA: ")
        if consulta == '0':
            consultas(0)
            continue
        
        elif consulta == '1':
            consultas(1)
            continue
            
        elif consulta == '2':
            consultas(6)
            continue
            
        elif consulta == '3':
            continue
            
        
    elif opcao == '2':
        print("Fechando programa....")
        time.sleep(2)
        break

