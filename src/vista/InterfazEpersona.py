from PyQt5.QtWidgets import QApplication
from src.vista.Vista_lista_personas import Vista_lista_personas

class App_EPersona(QApplication):
    """
    Clase principal de la interfaz que coordina las diferentes vistas/ventanas de la aplicación
    """

    def __init__(self, sys_argv, logica):
        """
        Constructor de la interfaz. Debe recibir la lógica e iniciar la aplicación en la ventana principal.
        """
        super(App_EPersona, self).__init__(sys_argv)

        self.logica = logica
        self.mostrar_vista_lista_personas()

    def mostrar_vista_lista_personas(self):
        """
        Esta función inicializa la ventana de la lista de personas
        """
        self.vista_lista_personas = Vista_lista_personas(self)
        self.vista_lista_personas.mostrar_personas(self.logica.dar_personas())
