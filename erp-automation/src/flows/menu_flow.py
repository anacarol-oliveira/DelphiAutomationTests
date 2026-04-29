from pages.menu_page import MenuPage
from flows.cliente_flow import cadastrar_cliente
from flows.categoria_flow import cadastrar_categoria
import os


CONTADOR_PATH = "contador_cadastros.txt"


def _obter_proximo_contador():
    # Cria o arquivo automaticamente se não existir
    if not os.path.exists(CONTADOR_PATH):
        with open(CONTADOR_PATH, "w") as f:
            f.write("0")

    # Lê o último valor
    with open(CONTADOR_PATH, "r") as f:
        conteudo = f.read().strip()
        ultimo = int(conteudo) if conteudo.isdigit() else 0

    proximo = ultimo + 1

    # Salva o novo valor
    with open(CONTADOR_PATH, "w") as f:
        f.write(str(proximo))

    return proximo


def iniciar_cadastros(janela_principal, app):
    menu_page = MenuPage(janela_principal)

    contador = _obter_proximo_contador()

    nome_cliente = f"CLIENTE {contador} AUTOMACAO TESTE"
    nome_categoria = f"CATEGORIA {contador} AUTOMACAO TESTE"

    abrir_clientes(menu_page, app, nome_cliente)
    abrir_categorias(menu_page, app, nome_categoria)


def abrir_clientes(menu_page, app, nome_cliente):
    menu_page.abrir_cadastros_clientes()

    janela_clientes = app.window(title_re=".*Cadastro de Clientes.*")
    janela_clientes.wait("exists enabled visible", timeout=40)
    janela_clientes.set_focus()

    cadastrar_cliente(janela_clientes, nome_cliente)


def abrir_categorias(menu_page, app, nome_categoria):
    menu_page.abrir_cadastros_categorias()

    janela_categoria = app.window(title_re=".*Cadastro de Tipos/Categorias de Produtos.*")
    janela_categoria.wait("exists enabled visible", timeout=40)
    janela_categoria.set_focus()

    cadastrar_categoria(janela_categoria, nome_categoria)
