import time
from pywinauto.keyboard import send_keys
from utils.cpf_generator import gerar_cpf


class ClientePage:
    def __init__(self, janela_cliente):
        self.janela = janela_cliente

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

    def preencher_cpf(self):
        cpf = gerar_cpf()
        self._tab(8)

        send_keys("^a{BACKSPACE}")
        send_keys(cpf)

        return cpf

    def salvar(self):
        self._focar()
        self._tab(20)

        time.sleep(0.5)
        send_keys('{ENTER}')

        time.sleep(1.5)
        send_keys('{ENTER}')

    def fechar(self):
        self._focar()
        self._tab(15)

        send_keys('{ENTER}')
        time.sleep(2)
