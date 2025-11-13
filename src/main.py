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
            while True:
                print("=== Menu Principal ===")
                opcao_menu = input("O que deseja fazer?\n" \
                "1 - Registrar Humor\n" \
                "2 - Resgatar recompensas\n" \
                "3 - Sair\n"
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
                        "5": ("Dia de folga", 300)
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
                elif opcao_menu == '3':
                        print(f'Até breve, {usuario_logado["nome"]}')
                        break
                else:
                    print("Opção inválida. Tente novamente.")
    elif menu_inicial == '3':
        print("Saindo do LUMINE. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
            
            




