from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
from DiseñoVentana.ventana_diseño import Ui_MainWindow  # Asegúrate de que este archivo se llame ventana.py o renómbralo si es necesario.

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # Conectar los botones a sus funciones correspondientes
        self.boton_agregar_propietario.clicked.connect(self.agregar_propietario)
        self.BotonFinca.clicked.connect(self.agregar_finca)
        self.BotonSalir.clicked.connect(self.salir)

    def mostrar_mensaje(self, titulo, mensaje,tipo="info"):
        """Muestra un pop-up con el mensaje especificado."""
        msg = QMessageBox()
        msg.setWindowTitle(titulo)
        msg.setText(mensaje)

        if tipo == "error":
            msg.setIcon(QMessageBox.Critical)
        else:
            msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def agregar_propietario(self):
        # Validar que todos los campos requeridos estén llenos
        if (self.lineEdit_CC.text() == "" or
            self.lineEdit_Nombre.text() == "" or
            self.lineEdit_Telefono.text() == "" or
            self.lineEdit_Apellidos.text() == "" or
            self.lineEdit_Correo.text() == ""):
            
            self.mostrar_mensaje("ERROR AL AGREGAR PROPIETARIO", "FALTAN CAMPOS POR COMPLETAR",tipo="error")
        else:
            # Si los campos están completos, mostrar un mensaje de éxito
            self.mostrar_mensaje("ÉXITO", "EL PROPIETARIO HA SIDO AGREGADO CORRECTAMENTE")

    def agregar_finca(self):
        # Validar que todos los campos requeridos para la finca estén llenos
        if (self.lineEdit_Municipio.text() == "" or
            self.lineEdit_RegistroCastral.text() == ""):
            
            self.mostrar_mensaje("ERROR AL AGREGAR FINCA", "FALTAN CAMPOS POR COMPLETAR.",tipo="error")
        else:
            # Si los campos están completos, mostrar un mensaje de éxito
            self.mostrar_mensaje("ÉXITO", "LA FINCA HA SIDO AGREGADA CORRECTAMENTE")
            self.lineEdit_Municipio.setText("")
            self.lineEdit_RegistroCastral.setText("")

    def salir(self):
        # Cierra la aplicación
        QtWidgets.QApplication.quit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
