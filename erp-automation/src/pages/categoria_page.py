import time
from pywinauto.keyboard import send_keys

class CategoriaPage:
    def __init__(self, janela_categoria):
        self.janela = janela_categoria

    def _focar(self):
        self.janela.set_focus()

    def _tab(self, n, delay=0.15):
        for _ in range(n):
            send_keys('{TAB}')
            time.sleep(delay)

    def iniciar_novo_cadastro(self):
        self._focar()
        time.sleep(0.5)
        send_keys('{INSERT}')
        time.sleep(4)

    def preencher_nome(self, nome_texto):
        self._focar()
        time.sleep(1)

        send_keys('%d')
        time.sleep(0.5)

        send_keys("^a{BACKSPACE}")
        send_keys(nome_texto, with_spaces=True)
        time.sleep(0.3)

    def salvar(self):
        self._focar()
        self._tab(19)

        time.sleep(0.5)
        send_keys('{ENTER}')

        time.sleep(1.5)
        send_keys('{ENTER}')

    def fechar(self):
        self._focar()
        self._tab(12)

        send_keys('{ENTER}')
        time.sleep(2)