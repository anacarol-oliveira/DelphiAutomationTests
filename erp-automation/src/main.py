from core.application import iniciar_erp
from flows.login_flow import realizar_login
from flows.menu_flow import iniciar_cadastros
from pywinauto.timings import wait_until
import time


def main():
    try:
        app, janela_login = iniciar_erp()
        realizar_login(janela_login, "USUARIO_TESTE", "SENHA_TESTE")

        janela_principal = app.window(title_re=".*Master.*")
        wait_until(40, 1, lambda: janela_principal.exists())
        janela_principal.set_focus()

        iniciar_cadastros(janela_principal, app)

        time.sleep(2)

    except Exception as e:
        print(f"\nErro no fluxo principal: {e}")

    input("\nPressione ENTER para sair...")


if __name__ == "__main__":
    main()
