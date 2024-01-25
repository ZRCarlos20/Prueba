# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(576, 539)
        Login.setStyleSheet("background-color:\n"
"rgb(0, 85, 127)")
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 40, 481, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 75 italic 25pt \"Bahnschrift\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 180, 181, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 240, 161, 16))
        self.label_3.setObjectName("label_3")
        self.txt_usu = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_usu.setGeometry(QtCore.QRect(260, 180, 201, 20))
        self.txt_usu.setStyleSheet("BACKGROUNG-COLOR:rgb(0, 85, 0)")
        self.txt_usu.setText("")
        self.txt_usu.setObjectName("txt_usu")
        self.txt_pas = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_pas.setGeometry(QtCore.QRect(260, 240, 201, 20))
        self.txt_pas.setObjectName("txt_pas")
        self.btn_sesion = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sesion.setGeometry(QtCore.QRect(310, 300, 91, 23))
        self.btn_sesion.setObjectName("btn_sesion")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 390, 261, 16))
        self.label_4.setObjectName("label_4")
        self.btn_registrar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_registrar.setGeometry(QtCore.QRect(320, 420, 75, 23))
        self.btn_registrar.setObjectName("btn_registrar")
        Login.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Login)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 576, 21))
        self.menubar.setObjectName("menubar")
        Login.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Login)
        self.statusbar.setObjectName("statusbar")
        Login.setStatusBar(self.statusbar)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "MainWindow"))
        self.label.setText(_translate("Login", "BIENVENIDO AL LOGIN  DEL SISTEMA "))
        self.label_2.setText(_translate("Login", "INGRESE CORREO INSTITUCIONAL : "))
        self.label_3.setText(_translate("Login", "INGRESE SU CONTRASEÑA : "))
        self.btn_sesion.setText(_translate("Login", "INICIAR SESION"))
        self.label_4.setText(_translate("Login", "¿NO CUENTA CON UN CORREO? REGISTRESE AQUI"))
        self.btn_registrar.setText(_translate("Login", "REGISTRAR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())