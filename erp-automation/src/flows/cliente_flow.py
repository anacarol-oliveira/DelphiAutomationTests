from pages.cliente_page import ClientePage


def cadastrar_cliente(janela_clientes, nome_texto):
    print("Iniciando novo cadastro...")

    cliente_page = ClientePage(janela_clientes)

    cliente_page.iniciar_novo_cadastro()
    cliente_page.preencher_nome(nome_texto)

    cpf = cliente_page.preencher_cpf()
    print(f"Preenchendo CPF: {cpf}")

    cliente_page.salvar()
    cliente_page.fechar()

    print("Cliente cadastrado com sucesso!")
