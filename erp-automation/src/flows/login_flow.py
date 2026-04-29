from pages.login_page import LoginPage


def realizar_login(janela_login, usuario, senha):
    login_page = LoginPage(janela_login)

    login_page.preencher_usuario(usuario)
    login_page.preencher_senha(senha)
    login_page.confirmar_login()
