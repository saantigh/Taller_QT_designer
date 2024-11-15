# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setStyleSheet("QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:repeat, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(79, 78, 78, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 81, 16))
        self.label.setStyleSheet("font: 87 10pt \"Arial Black\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 290, 81, 16))
        self.label_2.setStyleSheet("font: 87 10pt \"Arial Black\";")
        self.label_2.setObjectName("label_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 30, 781, 251))
        self.frame.setStyleSheet("QWidget#frame{\n"
"background-color: rgb(204, 204, 200);}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 131, 16))
        self.label_3.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(20, 70, 131, 16))
        self.label_4.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(20, 120, 131, 16))
        self.label_5.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.label_5.setObjectName("label_5")
        self.lineEdit_CC = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_CC.setGeometry(QtCore.QRect(160, 20, 211, 20))
        self.lineEdit_CC.setObjectName("lineEdit_CC")
        self.lineEdit_Nombre = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_Nombre.setGeometry(QtCore.QRect(160, 70, 211, 20))
        self.lineEdit_Nombre.setObjectName("lineEdit_Nombre")
        self.lineEdit_Telefono = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_Telefono.setGeometry(QtCore.QRect(160, 120, 211, 20))
        self.lineEdit_Telefono.setObjectName("lineEdit_Telefono")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(390, 70, 71, 16))
        self.label_6.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(390, 120, 71, 16))
        self.label_7.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.label_7.setObjectName("label_7")
        self.lineEdit_Apellidos = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_Apellidos.setGeometry(QtCore.QRect(450, 70, 191, 20))
        self.lineEdit_Apellidos.setObjectName("lineEdit_Apellidos")
        self.lineEdit_Correo = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_Correo.setGeometry(QtCore.QRect(450, 120, 191, 20))
        self.lineEdit_Correo.setObjectName("lineEdit_Correo")
        self.boton_agregar_propietario = QtWidgets.QPushButton(self.frame)
        self.boton_agregar_propietario.setGeometry(QtCore.QRect(580, 210, 161, 23))
        self.boton_agregar_propietario.setObjectName("boton_agregar_propietario")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 310, 781, 241))
        self.frame_2.setStyleSheet("QWidget#frame_2{\n"
"background-color: rgb(204, 204, 200);}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(20, 10, 71, 16))
        self.label_8.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.label_8.setObjectName("label_8")
        self.lineEdit_Municipio = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_Municipio.setGeometry(QtCore.QRect(100, 50, 211, 20))
        self.lineEdit_Municipio.setObjectName("lineEdit_Municipio")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(20, 50, 71, 16))
        self.label_9.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(330, 10, 111, 16))
        self.label_10.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.label_10.setObjectName("label_10")
        self.lineEdit_RegistroCastral = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_RegistroCastral.setGeometry(QtCore.QRect(450, 10, 191, 20))
        self.lineEdit_RegistroCastral.setObjectName("lineEdit_RegistroCastral")
        self.comboBox = QtWidgets.QComboBox(self.frame_2)
        self.comboBox.setGeometry(QtCore.QRect(100, 10, 211, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.BotonFinca = QtWidgets.QPushButton(self.frame_2)
        self.BotonFinca.setGeometry(QtCore.QRect(580, 140, 161, 23))
        self.BotonFinca.setObjectName("BotonFinca")
        self.BotonSalir = QtWidgets.QPushButton(self.frame_2)
        self.BotonSalir.setGeometry(QtCore.QRect(360, 200, 75, 23))
        self.BotonSalir.setStyleSheet("border-radius:10px;\n"
"background-color: qlineargradient(spread:repeat, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(79, 78, 78, 255), stop:1 rgba(255, 255, 255, 255));")
        self.BotonSalir.setObjectName("BotonSalir")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Propietario"))
        self.label_2.setText(_translate("MainWindow", "Finca"))
        self.label_3.setText(_translate("MainWindow", "Documento Identidad"))
        self.label_4.setText(_translate("MainWindow", "Nombre"))
        self.label_5.setText(_translate("MainWindow", "Tel/Cel"))
        self.label_6.setText(_translate("MainWindow", "Apellidos"))
        self.label_7.setText(_translate("MainWindow", "Correo"))
        self.boton_agregar_propietario.setText(_translate("MainWindow", "Agregar Propietario"))
        self.label_8.setText(_translate("MainWindow", "Cultivo"))
        self.label_9.setText(_translate("MainWindow", "Municipio"))
        self.label_10.setText(_translate("MainWindow", "Registro Castral"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Café"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Platano"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Caña de azucar"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Maiz"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Marihuana"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Frijol"))
        self.BotonFinca.setText(_translate("MainWindow", "Agregar Finca"))
        self.BotonSalir.setText(_translate("MainWindow", "SALIR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
