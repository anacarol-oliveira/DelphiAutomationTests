from pywinauto.application import Application
from config.settings import ERP_EXE_PATH, DEFAULT_TIMEOUT

def iniciar_erp():
    app = Application(backend="uia").start(ERP_EXE_PATH)
    janela = app.window(title_re=".*")
    janela.wait("visible", timeout=DEFAULT_TIMEOUT)
    return app, janela