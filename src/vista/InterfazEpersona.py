from PyQt5.QtWidgets import QApplication

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

