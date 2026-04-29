from pages.categoria_page import CategoriaPage

def cadastrar_categoria(janela_categoria, nome_texto):
    print("Iniciando novo cadastro...")

    categoria_page = CategoriaPage(janela_categoria)

    categoria_page.iniciar_novo_cadastro()
    categoria_page.preencher_nome(nome_texto)

    categoria_page.salvar()
    categoria_page.fechar()

    print("Categoria cadastrada com sucesso!")
