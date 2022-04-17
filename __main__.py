import sys
from PyQt5.QtWidgets import QApplication
from src.logica.Logica_mock import Logica_mock
from src.vista.InterfazEpersona import App_EPersona

if __name__ == '__main__':
    # Punto inicial de la aplicación

    logica = Logica_mock()
    print(logica.texto)
    print(logica.personas)

    app = App_EPersona(sys.argv, logica)
    sys.exit(app.exec_())

