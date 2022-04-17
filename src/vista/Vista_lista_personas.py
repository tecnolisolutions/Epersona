from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from functools import partial


class Vista_lista_personas(QWidget):
    # Ventana que muestra la lista de carreras

    def __init__(self, interfaz):
        """
        Constructor de las ventanas
        """
        super().__init__()

        self.interfaz = interfaz

        # Se establecen las características de la ventana
        self.title = 'Epersona'
        self.width = 720
        self.height = 750
        self.inicializar_GUI()

    def inicializar_GUI(self):
        # inicializamos la ventana
        self.setWindowTitle(self.title)
        self.setFixedSize(self.width, self.height)
        self.setWindowIcon(QIcon("src/recursos/smallLogo.png"))

        self.distribuidor_base = QVBoxLayout(self)

        # Creación del logo de encabezado
        self.logo = QLabel(self)
        self.pixmap = QPixmap("src/recursos/EpersonaHeader.png")
        self.pixmap = self.pixmap.scaled(400, 150, Qt.KeepAspectRatio)
        self.logo.setPixmap(self.pixmap)
        self.logo.setAlignment(Qt.AlignCenter)
        self.distribuidor_base.addWidget(self.logo, alignment=Qt.AlignCenter)



        # Hacemos la ventana visible
        self.show()

