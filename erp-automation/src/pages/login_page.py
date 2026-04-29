import time
from pywinauto.keyboard import send_keys


class LoginPage:
    def __init__(self, janela):
        self.janela = janela

    def _campo_usuario(self):
        return self.janela.child_window(
            control_type="Edit",
            found_index=1
        )

    def _campo_senha(self):
        return self.janela.child_window(
            control_type="Edit",
            found_index=0
        )

    def preencher_usuario(self, usuario):
        self.janela.set_focus()
        time.sleep(0.5)

        campo = self._campo_usuario()
        campo.click_input()
        campo.type_keys("^a{BACKSPACE}")
        campo.type_keys(usuario, with_spaces=True)

    def preencher_senha(self, senha):
        campo = self._campo_senha()
        campo.click_input()
        campo.type_keys("^a{BACKSPACE}")
        campo.type_keys(senha, with_spaces=True)

    def confirmar_login(self):
        time.sleep(0.3)
        send_keys("{ENTER}")
