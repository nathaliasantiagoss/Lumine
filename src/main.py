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
                "2 - Sair\n"
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
                    # Aqui você pode adicionar a funcionalidade para salvar o humor registrado
                    print(f"Humor: {humor}")
                    print(f"Contexto: {contexto}\n")
                elif opcao_menu == '2':
                        print(f'Até breve, {usuario_logado["nome"]}')
                        break
                else:
                    print("Opção inválida. Tente novamente.")
    elif menu_inicial == '3':
        print("Saindo do LUMINE. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
            
            




