from datetime import datetime
import funcoes.utils as utils
import funcoes.armazenamento as armazenamento 

while True:
    print("\n=== Bem-vindo(a) ao LUMINE ===")
    menu_inicial = input("O que deseja realizar?\n" \
    "1 - Cadastro\n" \
    "2 - Login\n"
    "3 - Sair\n"
    "Opção: ")

    if menu_inicial == '1':
        cadastro_realizado = utils.cadastro()
        sucesso_salvar = armazenamento.salvar_usuario(cadastro_realizado)
    elif menu_inicial == '2':
        usuario_logado, login_realizado = utils.login()

        if login_realizado:
            print(f'Olá, {usuario_logado["nome"]}')
            if usuario_logado["email"] == "admin@admin.com":
                while True:
                    print("\n=== MENU ADMIN ===")
                    opcao_admin = input(
                        "1 - Visualizar lista de cadastrados\n"
                        "2 - Relatório de humor\n"
                        "3 - Atualizar setor/cargo de um colaborador\n"
                        "4 - Deletar colaborador\n"
                        "5 - Sair\n"
                        "Opção: "
                    )

                    # Ver todos os cadastrados
                    if opcao_admin == "1":
                        usuarios = armazenamento.ler_usuarios()
                        print("\n=== Lista de Colaboradores ===")
                        for u in usuarios:
                            print(f"{u['nome']} - {u['idade']}anos - {u['email']} - {u['setor']} - {u['cargo']}")
                        print()

                    # Relatório de humor
                    elif opcao_admin == "2":
                        armazenamento.relatorio_humor_por_setor()
                        print()
                    elif opcao_admin == "3":
                        email_update = input("Digite o email do colaborador a deletar: ")
                        print("=== Editar minhas informações ===")

                        novos_dados = {}

                        setor = input("Novo setor (enter para manter): ").strip()
                        if setor:
                            novos_dados["setor"] = setor
                        cargo = input("Novo cargo (enter para manter): ").strip()
                        if cargo:
                            novos_dados["cargo"] = cargo

                        if novos_dados:
                            sucesso = armazenamento.atualizar_usuario_admin(email_update, novos_dados)

                            if sucesso:
                                print("Informações atualizadas com sucesso!")
                            else:
                                print("Erro ao atualizar suas informações.")
                        else:
                            print("Nenhuma alteração realizada.")

                    # Deletar colaborador
                    elif opcao_admin == "4":
                        email_del = input("Digite o email do colaborador a deletar: ")
                        armazenamento.deletar_usuario(email_del)

                    elif opcao_admin == "5":
                        break
                    else:
                        print("Opção inválida.\n")
            else:
                while True:
                    print("=== Menu Principal ===")
                    opcao_menu = input("O que deseja fazer?\n" \
                    "1 - Registrar Humor\n" \
                    "2 - Resgatar recompensas\n" \
                    "3 - Atualizar cadastro\n" \
                    "4 - Sair\n"
                    "Opção: ")

                    if opcao_menu == '1':
                        humor, contexto = utils.registrar_humor()
                        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        dados_humor = [
                            usuario_logado.get('setor', 'Setor não informado'),
                            humor,
                            contexto,
                            data_hora
                        ]
                        armazenamento.salvar_humor(dados_humor)
                        armazenamento.atualizar_pontuacao(usuario_logado["nome"])
                        print(f"Humor: {humor}")
                        print(f"Contexto: {contexto}\n")
                    elif opcao_menu == '2':
                        print("\n=== Resgate de Recompensas ===")

                        pontos = armazenamento.ler_pontuacao(usuario_logado["nome"])
                        print(f"Você possui {pontos} pontos.\n")

                        premios = {
                            "1": ("Spa", 15),
                            "2": ("Vale-snack", 50),
                            "3": ("Saída antecipada (30 min)", 100),
                            "4": ("Brinde da empresa", 150),
                            "5": ("Dia de folga", 200)
                        }

                        print("Prêmios disponíveis:")
                        for key, (nome, custo) in premios.items():
                            print(f"{key} - {nome} ({custo} pontos)")

                        escolha = input("Qual prêmio deseja resgatar? (ou 0 para voltar)\nOpção: ")

                        if escolha == "0":
                            continue

                        if escolha not in premios:
                            print("Opção inválida.")
                            continue

                        premio_escolhido, custo = premios[escolha]

                        if pontos < custo:
                            print(f"Você não tem pontos suficientes para resgatar '{premio_escolhido}'.")
                        else:
                            nova_pontuacao = pontos - custo
                            armazenamento.salvar_pontuacao(usuario_logado["nome"], nova_pontuacao)

                            print(f"Você resgatou: {premio_escolhido}!")
                            print(f"Novo saldo de pontos: {nova_pontuacao}\n")
                    elif opcao_menu == "3":
                        print("=== Editar minhas informações ===")

                        novos_dados = {}

                        nome = input("Novo nome (enter para manter): ").strip()
                        if nome:
                            novos_dados["nome"] = nome

                        idade = input("Nova idade (enter para manter): ").strip()
                        if idade:
                            novos_dados["idade"] = idade

                        genero = input("Novo gênero (enter para manter): ").strip()
                        if genero:
                            novos_dados["genero"] = genero

                        senha = input("Nova senha (enter para manter): ").strip()
                        if senha:
                            novos_dados["senha"] = senha

                        if novos_dados:
                            sucesso = armazenamento.atualizar_usuario(usuario_logado["email"], novos_dados)

                            if sucesso:
                                print("Informações atualizadas com sucesso!")
                            else:
                                print("Erro ao atualizar suas informações.")
                        else:
                            print("Nenhuma alteração realizada.")

                    elif opcao_menu == '4':
                        print(f'Até breve, {usuario_logado["nome"]}')
                        break
                    else:
                        print("Opção inválida. Tente novamente.")
    elif menu_inicial == '3':
        print("Saindo do LUMINE. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
            
            




