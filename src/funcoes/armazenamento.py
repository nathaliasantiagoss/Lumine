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
        print(f"+10 pontos adicionados para {nome_usuario}!")
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
    finally:
        if arquivo_pontuacao:
            arquivo_pontuacao.close()
    
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
    arquivo_pontuacao.close()

def deletar_usuario(email):
    try:
        # Lê todas as linhas do arquivo
        arquivo_cadastro = open("cadastro.txt", "r", encoding="utf-8")
        linhas = arquivo_cadastro.readlines()
        arquivo_cadastro.close()

        novas_linhas = []
        usuario_deletado = False
        nome_usuario = ""

        # Procura o usuário na lista
        for linha in linhas:
            campos = linha.strip().split('|')

            if len(campos) == 7:
                if campos[5] == email:  # posição do email
                    usuario_deletado = True
                    nome_usuario = campos[0]  # nome do usuário
                    continue  # não adiciona esta linha → deleta
            novas_linhas.append(linha)

        # Reescreve o arquivo
        arquivo_cadastro = open("cadastro.txt", "w", encoding="utf-8")
        for linha in novas_linhas:
            arquivo_cadastro.write(linha)
        arquivo_cadastro.close()

        # Mensagens finais
        if usuario_deletado:
            print(f'\nCadastro do colaborador "{nome_usuario}" deletado com sucesso!\n')
        else:
            print("\nNenhum colaborador encontrado com esse email.\n")

        return usuario_deletado

    except Exception as e:
        print(f"Erro ao tentar deletar usuário: {e}")
        return False

    
def ler_humor():
    lista_registros = []
    try:
        arquivo_humor = open("humor.txt", "r", encoding="utf-8")
        for linha in arquivo_humor:
            campos = linha.strip().split('|')
            if len(campos) == 4:
                lista_registros.append({
                    "setor": campos[0],
                    "humor": campos[1],
                    "contexto": campos[2],
                    "data": campos[3]
                })
        return lista_registros
    except FileNotFoundError:
        return []
    finally:
        if arquivo_humor:
            arquivo_humor.close()

def relatorio_humor_por_setor():
    try:
        arquivo = open("humor.txt", "r", encoding="utf-8")
        linhas = arquivo.readlines()
        arquivo.close()

        if not linhas:
            print("\nNenhum registro de humor encontrado.\n")
            return

        relatorio = {}

        # Processa cada linha do arquivo
        for linha in linhas:
            campos = linha.strip().split('|')
            if len(campos) == 4:
                setor = campos[0]
                humor = campos[1]
                contexto = campos[2]

                # Se setor ainda não existe no relatório
                if setor not in relatorio:
                    relatorio[setor] = {
                        "total": 0,
                        "humores": {},
                        "contextos": {}
                    }

                # Atualiza total
                relatorio[setor]["total"] += 1

                # Contabiliza humor
                if humor not in relatorio[setor]["humores"]:
                    relatorio[setor]["humores"][humor] = 0
                relatorio[setor]["humores"][humor] += 1

                # Contabiliza contexto
                if contexto not in relatorio[setor]["contextos"]:
                    relatorio[setor]["contextos"][contexto] = 0
                relatorio[setor]["contextos"][contexto] += 1

        # Exibe relatório organizado
        print("\n=== RELATÓRIO DE HUMOR POR SETOR ===\n")

        for setor, dados in relatorio.items():
            print(f"Setor: {setor}")
            print(f"   Total de registros: {dados['total']}")

            print("\n   Humores registrados:")
            for humor, quantidade in dados["humores"].items():
                print(f"     {humor}: {quantidade}x")

            print("\n   Contextos registrados:")
            for contexto, quantidade in dados["contextos"].items():
                print(f"      {contexto}: {quantidade}x")

            print("\n" + "-"*50 + "\n")

    except Exception as e:
        print(f"Erro ao gerar relatório: {e}")

    finally:
        if arquivo:
            arquivo.close()

def atualizar_usuario(email, novos_dados):

    indices = {
        "nome": 0,
        "idade": 1,
        "genero": 2,
        "setor": 3,
        "cargo": 4,
        "senha": 5
    }

    try:
        arquivo_cadastro = open("cadastro.txt", "r", encoding="utf-8") 
        linhas = arquivo_cadastro.readlines()

        novas_linhas = []
        usuario_editado = False

        for linha in linhas:
            dados = linha.strip().split("|")

            # Identifica o usuário pelo email
            if len(dados) == 7 and dados[5] == email:
                for campo, valor in novos_dados.items():
                    if campo in indices:
                        dados[indices[campo]] = valor
                usuario_editado = True
                novas_linhas.append("|".join(dados) + "\n")
            else:
                novas_linhas.append(linha)

        # Reescreve o arquivo
        arquivo_cadastro = open("cadastro.txt", "w", encoding="utf-8") 
        arquivo_cadastro.writelines(novas_linhas)

        return usuario_editado

    except Exception as e:
        print(f"Erro ao editar usuário: {e}")
        return False

    finally:
        if arquivo_cadastro:
            arquivo_cadastro.close()
