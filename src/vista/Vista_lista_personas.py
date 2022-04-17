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

        # Creación de las etiquetas con textos de bienvenida
        self.etiqueta_bienvenida = QLabel("!!Bienvenido a E-Persona!!")
        self.etiqueta_bienvenida.setAlignment(Qt.AlignCenter)
        self.distribuidor_base.addWidget(self.etiqueta_bienvenida, Qt.AlignCenter)

        self.etiqueta_descripcion = QLabel("La manera más fácil e inteligente de registrar una persona")
        self.etiqueta_descripcion.setAlignment(Qt.AlignCenter)
        self.distribuidor_base.addWidget(self.etiqueta_descripcion, Qt.AlignCenter)

        # Creación del espacio de los botones
        self.widget_botones = QWidget()
        self.distribuidor_botones = QGridLayout()
        self.widget_botones.setLayout(self.distribuidor_botones)

        # Creación de los botones
        self.btn_aniadir_actividad = QPushButton("Agregar Persona", self)
        self.btn_aniadir_actividad.setFixedSize(200, 40)
        self.btn_aniadir_actividad.setToolTip("Agregar Persona")
        self.btn_aniadir_actividad.setIcon(QIcon("src/recursos/006-add.png"))
        self.btn_aniadir_actividad.setIconSize(QSize(120, 120))
        self.distribuidor_botones.addWidget(self.btn_aniadir_actividad, 0, 0, Qt.AlignLeft)
        self.btn_aniadir_actividad.clicked.connect(self.mostrar_ventana_crear_carrera)

        # Hacemos la ventana visible
        self.show()

