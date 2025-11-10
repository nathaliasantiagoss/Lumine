from funcoes.armazenamento import *   

def cadastro():
    print("=== Cadastro de Usuário ===")
    nome = input("Nome completo: ")
    idade = int(input("Idade: "))
    genero = input("Gênero: ")
    setor = input("Setor: ")
    cargo = input("Cargo: ")    
    email = input("Email: ")
    senha = input("Senha: ")
    print("Cadastro realizado com sucesso!")
    return nome,idade,genero,setor,cargo,email,senha

def login():
    print("=== Login de Usuário ===")
    email = input("Email: ")
    senha = input("Senha: ")

    lista_usuarios = ler_usuarios()

    if not lista_usuarios:
        print("Nenhum usuário cadastrado. Por favor, faça o cadastro primeiro.")
        return None, False

    for usuario in lista_usuarios:
        if usuario['email'] == email and usuario['senha'] == senha:
            print("Login bem-sucedido! Bem-vindo(a),", usuario['nome'])
            return usuario, True
    print("Email ou senha incorretos. Tente novamente.")
    return None, False

def registrar_humor():
    print("=== Registro de Humor ===")
    opcoes_humor = {
        "1": "Muito bem",
        "2": "Bem",
        "3": "Neutro",
        "4": "Estressado",
        "5": "Irritado",
        "6": "Triste"
    }

    opcoes_contexto = {
        "1": "Dia excelente",
        "2": "Tudo tranquilo, normal",
        "3": "Regular",
        "4": "Tarefas ou ambiente pesado",
        "5": "Conflituoso",
        "6": "Desmotivado ou cansado emocionalmente"
    }
    humor = input("Como você está se sentindo hoje?\n" \
    "1 - Muito bem\n2 - Bem\n3 - Neutro\n4 - Estressado\n5 - Irritado\n6 - Triste\n" \
    "Opção: ")
    contexto_humor = input("Como está seu dia hoje?\n" \
    "1 - Dia Excelente\n2 - Tudo tranquilo, normal\n3 - Regular\n4 - Tarefas ou ambiente pesado\n" \
    "5 - Conflituoso\n6 - Desmotivado ou cansado emocionalmente\n" \
    "Opção: ")

    humor_texto = opcoes_humor.get(humor, "Opção inválida")
    contexto_texto = opcoes_contexto.get(contexto_humor, "Opção inválida")

    print("Registro de humor salvo com sucesso!")

    return humor_texto, contexto_texto