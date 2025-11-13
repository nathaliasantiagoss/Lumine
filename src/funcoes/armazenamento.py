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

def atualizar_pontuacao(nome_usuario):
    delimitador = '|'
    arquivo_pontuacao = None
    linhas_pontuacao = []
    usuario_encontrado = False

    try:
        # Tenta abrir o arquivo de pontuação para leitura
        arquivo_pontuacao = open("pontuacao.txt", "r", encoding="utf-8")
        for linha in arquivo_pontuacao:
            campos = linha.strip().split(delimitador)
            if len(campos) == 2:
                nome = campos[0]
                pontos = int(campos[1])
                if nome == nome_usuario:
                    pontos += 10
                    usuario_encontrado = True
                linhas_pontuacao.append(f"{nome}{delimitador}{pontos}\n")
            else:
                # Mantém a linha original se estiver em formato inesperado
                linhas_pontuacao.append(linha)
    except FileNotFoundError:
        # Se o arquivo não existir, ele será criado depois
        pass
    except Exception as e:
        print(f"Erro ao ler o arquivo de pontuação: {e}")
    finally:
        if arquivo_pontuacao:
            arquivo_pontuacao.close()

    # Se o usuário ainda não estiver no arquivo, adiciona com 10 pontos
    if not usuario_encontrado:
        linhas_pontuacao.append(f"{nome_usuario}{delimitador}10\n")

    # Reescreve o arquivo com as pontuações atualizadas
    try:
        arquivo_pontuacao = open("pontuacao.txt", "w", encoding="utf-8")
        for linha in linhas_pontuacao:
            arquivo_pontuacao.write(linha)
        print(f"🏅 +10 pontos adicionados para {nome_usuario}!")
    except Exception as e:
        print(f"Erro ao salvar o arquivo de pontuação: {e}")
    finally:
        if arquivo_pontuacao:
            arquivo_pontuacao.close()
        
def ler_pontuacao(nome_usuario):
    try:
        arquivo_pontuacao = open("pontuacao.txt", "r", encoding="utf-8")    
        for linha in arquivo_pontuacao:
            nome, pontos = linha.strip().split('|')
            if nome == nome_usuario:
                return int(pontos)
        return 0  # se não encontrar o usuário
    except FileNotFoundError:
        return 0
    
def salvar_pontuacao(nome_usuario, nova_pontuacao):
    linhas = []
    try:
        arquivo_pontuacao = open("pontuacao.txt", "r", encoding="utf-8") 
        for linha in arquivo_pontuacao:
            nome, pontos = linha.strip().split('|')
            if nome == nome_usuario:
                linhas.append(f"{nome}|{nova_pontuacao}\n")
            else:
                linhas.append(linha)
    except FileNotFoundError:
        # se o arquivo não existir, cria um novo
        linhas.append(f"{nome_usuario}|{nova_pontuacao}\n")

    arquivo_pontuacao = open("pontuacao.txt", "w", encoding="utf-8") 
    for linha in linhas:
        arquivo_pontuacao.write(linha)
