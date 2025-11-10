from funcoes.utils import *

def salvar_usuario(dados_usuario):
    delimitador = '|'
    usuario = []
    for dado in dados_usuario:
        dado_convertido = str(dado)
        usuario.append(dado_convertido)
    linha_dados = delimitador.join(usuario) + '\n'
    arquivo_cadastro = open("cadastro.txt", "a", encoding="utf-8")
    arquivo_cadastro.write(linha_dados)
    arquivo_cadastro.close()


def salvar_humor(dados_humor):
    delimitador = '|'
    humor_registro = []
    for dado in dados_humor:
        humor_registro.append(str(dado))

    linha_dados = delimitador.join(humor_registro) + '\n'
    arquivo_humor = open("humor.txt", "a", encoding="utf-8")
    arquivo_humor.write(linha_dados)
    arquivo_humor.close()


def ler_usuarios():
    lista_usuarios = [] 
    arquivo_cadastro = None
    try:
        arquivo_cadastro = open("cadastro.txt", "r", encoding="utf-8")      
        for linha in arquivo_cadastro:
            campos_usuario = linha.strip().split('|')
            if len(campos_usuario) == 7:
                usuario_dict = {
                    'nome': campos_usuario[0],
                    'idade': int(campos_usuario[1]),
                    'genero': campos_usuario[2],
                    'setor': campos_usuario[3],
                    'cargo': campos_usuario[4],
                    'email': campos_usuario[5],
                    'senha': campos_usuario[6]
                }
                lista_usuarios.append(usuario_dict)
        return lista_usuarios
    except Exception as e:
        print(f"Erro ao ler o arquivo de cadastro: {e}")
    finally:
        arquivo_cadastro.close()
        

