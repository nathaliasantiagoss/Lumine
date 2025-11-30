LUMINE – Sistema de Gestão de Humor e Recompensas

O LUMINE é um sistema em Python focado na gestão do bem-estar emocional de colaboradores, permitindo que usuários registrem seu humor, resgatem recompensas e visualizem relatórios.
Possui dois tipos de acesso:

    - Colaborador (usuário comum)
    - Administrador

O sistema utiliza arquivos .txt para armazenamento simples e acessível.

Estrutura do Projeto

/LUMINE
│
├── main.py
├── funcoes/
│   ├── utils.py
│   └── armazenamento.py
│
├── cadastro.txt
├── humor.txt
└── pontuacao.txt

Funcionalidades Principais

1. Cadastro de Usuário

    O usuário informa:

        - Nome
        - Idade
        - Gênero
        - Setor
        - Cargo
        - Email
        - Senha

    Dados são armazenados em cadastro.txt.

2. Login

    Autenticação feita com:

        - Email
        - Senha

    Se o login for bem-sucedido, o sistema identifica se o usuário é admin ou colaborador.

    Admin padrão:

        - Email: admin@admin.com
        - Senha: admin

Menu Administrador

1. Visualizar Lista de Cadastrados

    - Exibe todos os colaboradores e seus dados.

2. Relatório de Humor por Setor

    Gera um resumo com:

        - Total de registros por setor
        - Frequência de cada humor
        - Contextos mais apresentados

    Usa os dados de humor.txt.

3. Atualizar Setor/Cargo

    Permite modificar informações de:

        - Setor
        - Cargo

    de qualquer usuário.

4. Deletar Colaborador

    Remove usuário do arquivo cadastro.txt com base no email.

Menu Usuário (Colaborador)

1. Registrar Humor

    Usuário seleciona:

        Humor (Muito bem, Bem, Neutro, Estressado, Irritado, Triste)

    Contexto do dia

    O sistema salva:

        - Setor
        - Humor
        - Contexto
        - Data/hora

    Além disso, o colaborador ganha +10 pontos.

2. Resgatar Recompensas

    O usuário pode trocar seus pontos por premiações como:

        - Spa
        - Vale-snack
        - Saída antecipada
        - Brinde da empresa
        - Dia de folga

    Pontuação é lida e atualizada em pontuacao.txt.

3. Atualizar Cadastro

    Usuário pode alterar:

        - Nome
        - Idade
        - Gênero
        - Senha

    As alterações são aplicadas diretamente no arquivo de cadastro.

4. Sair

    Retorna ao menu inicial.

Arquivos do Sistema

    - cadastro.txt

        Armazena usuários no formato:

            nome|idade|genero|setor|cargo|email|senha

    - humor.txt

        Armazena registros de humor:

            setor|humor|contexto|data_hora

    - pontuacao.txt

        Armazena pontuação de colaboradores:

            nome|pontos

Como Executar

    - Certifique-se de ter Python 3 instalado.
    - Coloque todos os arquivos na estrutura indicada.
    - Execute o programa principal:
        python main.py