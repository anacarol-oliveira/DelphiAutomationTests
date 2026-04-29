import time


class MenuPage:
    def __init__(self, janela):
        self.janela = janela

    def _focar(self):
        self.janela.set_focus()
        time.sleep(0.5)

    def _coordenadas_menu(self):
        rect = self.janela.rectangle()
        y_menu = rect.top + 40
        x_cadastros = rect.left + 80
        return x_cadastros, y_menu

    def abrir_cadastros_clientes(self):
        self._focar()

        x_cadastros, y_menu = self._coordenadas_menu()
        self.janela.click_input(coords=(x_cadastros, y_menu))
        time.sleep(0.3)

        x_clientes_menu = x_cadastros + 30
        y_clientes_menu = y_menu + 80
        self.janela.click_input(coords=(x_clientes_menu, y_clientes_menu))
        time.sleep(0.3)

        x_clientes_final = x_clientes_menu + 180
        y_clientes_final = y_clientes_menu
        self.janela.click_input(coords=(x_clientes_final, y_clientes_final))

    def abrir_cadastros_categorias(self):
        self._focar()

        x_cadastros, y_menu = self._coordenadas_menu()
        self.janela.click_input(coords=(x_cadastros, y_menu))
        time.sleep(0.3)

        x_estoque_menu = x_cadastros + 30
        y_estoque_menu = y_menu + 40
        self.janela.click_input(coords=(x_estoque_menu, y_estoque_menu))
        time.sleep(0.3)

        x_tipos_categorias = x_estoque_menu + 200
        y_tipos_categorias = y_estoque_menu + 20
        self.janela.click_input(coords=(x_tipos_categorias, y_tipos_categorias))
