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

        # Creación del área con la información de las personas
        self.tabla_personas = QScrollArea(self)
        self.tabla_personas.setWidgetResizable(True)
        self.tabla_personas.setFixedSize(700, 450)
        self.widget_tabla_actividades = QWidget()
        self.distribuidor_tabla_personas = QGridLayout()
        self.widget_tabla_actividades.setLayout(self.distribuidor_tabla_personas);
        self.tabla_carreras.setWidget(self.widget_tabla_actividades)
        self.distribuidor_base.addWidget(self.tabla_personas)

                # Hacemos la ventana visible
        self.show()

    def mostrar_personas(self, lista_personas):
        """
        Esta función puebla la tabla con las personas
        """
        self.personas = lista_personas

        #Este pedazo de código borra todo lo que no sean encabezados
        while self.distribuidor_tabla_personas.count()>2:
            child = self.distribuidor_tabla_personas.takeAt(2)
            if child.widget():
                child.widget().deleteLater()

        self.distribuidor_tabla_personas.setColumnStretch(0,1)
        self.distribuidor_tabla_personas.setColumnStretch(1,0)
        self.distribuidor_tabla_personas.setColumnStretch(2,0)
        self.distribuidor_tabla_personas.setColumnStretch(3,0)
        self.distribuidor_tabla_personas.setColumnStretch(4,0)
        self.distribuidor_tabla_personas.setColumnStretch(4,0)

        # Ciclo para llenar la tabla
        if (self.personas != None and len(self.personas) > 0):
            self.tabla_personas.setVisible(True)

            # Creación de las etiquetas

            etiqueta_nombre = QLabel("Nombre")
            etiqueta_nombre.setMinimumSize(QSize(0, 0))
            etiqueta_nombre.setMaximumSize(QSize(65525, 65525))
            etiqueta_nombre.setAlignment(Qt.AlignCenter)
            etiqueta_nombre.setFont(QFont("Times", weight=QFont.Bold))
            self.distribuidor_tabla_personas.addWidget(etiqueta_nombre, 0, 0, Qt.AlignCenter)

            etiqueta_acciones = QLabel("Acciones")
            etiqueta_acciones.setMinimumSize(QSize(0, 0))
            etiqueta_acciones.setMaximumSize(QSize(65525, 65525))
            etiqueta_acciones.setAlignment(Qt.AlignCenter)
            etiqueta_acciones.setFont(QFont("Times", weight=QFont.Bold))
            self.distribuidor_tabla_personas.addWidget(etiqueta_acciones, 0, 1, 1, 5, Qt.AlignCenter)

            numero_fila = 0
            for dic_persona in self.personas:
                numero_fila = numero_fila + 1

                etiqueta_nombre = QLabel(dic_persona['Nombre'])
                etiqueta_nombre.setWordWrap(True)
                self.distribuidor_tabla_personas.addWidget(etiqueta_nombre, numero_fila, 0)

                # Creación de los botones asociados a cada acción
                btn_ver_actividad = QPushButton("", self)
                btn_ver_actividad.setToolTip("Editar persona")
                btn_ver_actividad.setFixedSize(40, 40)
                btn_ver_actividad.setIcon(QIcon("src/recursos/004-edit-button.png"))
                btn_ver_actividad.clicked.connect(partial(self.mostrar_persona, numero_fila - 1))
                self.distribuidor_tabla_personas.addWidget(btn_ver_actividad, numero_fila, 1, Qt.AlignCenter)

                btn_eliminar = QPushButton("", self)
                btn_eliminar.setToolTip("Eliminar")
                btn_eliminar.setFixedSize(40, 40)
                btn_eliminar.setIcon(QIcon("src/recursos/005-delete.png"))
                btn_eliminar.clicked.connect(partial(self.eliminar_persona, numero_fila - 1))
                self.distribuidor_tabla_personas.addWidget(btn_eliminar, numero_fila, 4, Qt.AlignCenter)

        else:
            self.tabla_carreras.setVisible(False)

        # Elemento para ajustar la forma de la tabla (y evitar que queden muy espaciados)
        self.distribuidor_tabla_personas.layout().setRowStretch(numero_fila + 2, 1)

    def mostrar_persona(self,id_persona):
        """
        Esta función informa a la interfaz para desplegar la ventana de la carrera
        """
        self.hide()
        self.interfaz.mostrar_carrera(id_persona)

