from conexion import *
from login_ui import *
from menu_ui import *
from alumno_ui import *
from instructor_ui import *
from Classalumno import *

from PyQt5.QtWidgets import QMainWindow, QTableView, QApplication, QMessageBox
from PyQt5.QtGui import QStandardItem, QStandardItemModel


from PyQt5.uic import loadUi
import sys
import mysql.connector
cursor = mydb.cursor()
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('login.ui', self)
        self.btn_sesion.clicked.connect(self.validar)

    def validar(self):
        usu = self.txt_usu.text()
        pas = self.txt_pas.text()

        if not self.validar_credenciales(usu, pas):
            self.txt_usu.setText('')
            self.txt_pas.setText('')
        else:
            self.txt_usu.setText('')
            self.txt_pas.setText('')

            self.hide()

            vent2 = Ui_menu(self)
            vent2.show()

    def validar_credenciales(self, usuario, contrasena):
        try:
            cursor = mydb.cursor()
            
            sql = "SELECT * FROM usuarios WHERE nombre = %s AND rol = %s"
            cursor.execute(sql, (usuario, contrasena))
            result = cursor.fetchone()

            if result:
                return True
            else:
                return False
        except mysql.connector.Error as err:
            print("Error al validar credenciales:", err)
        finally:
            cursor.close()

class Ui_menu(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Ui_menu, self).__init__(parent)
        loadUi('menu.ui', self)

        self.btn_instructor.clicked.connect(self.abrir_instructor)
        self.btn_alumno.clicked.connect(self.abrir_alumno)
    
    def abrir_instructor(self):
        self.hide()
        self.instrutor = InstructorWindow(mydb, self)
        self.instrutor.show()

    def abrir_alumno(self):
        self.hide() 
        self.alumno = AlumnoWindow(mydb, self)
        self.alumno.show()
        
class InstructorWindow(QMainWindow):
    def __init__(self, mydb, parent=None):
        super().__init__(parent)
        self.mydb = mydb

        loadUi('instructor.ui', self)

        self.tabla = self.btn_listar  
        self.modelo = QStandardItemModel()
        self.tabla.setModel(self.modelo)

        self.btn_registrar.clicked.connect(self.registrar_instructor)
        self.btn_retornar.clicked.connect(self.cerrar)

        self.mostrar_instructores()

    def cerrar(self):
        self.hide()
        vent = Ui_menu(self)
        vent.show()

        self.mostrar_instructores()

    def registrar_instructor(self):
        id = self.txt_id.text()
        nombre = self.txt_nom.text()
        apellido = self.txt_ape.text()
        curso = self.txt_car.text()
        correo = self.txt_gmail.text()

        try:
            cursor = self.mydb.cursor()
            sql = "INSERT INTO Instructor (ID, Nombre, Apellido, Curso, Correo) VALUES (%s, %s, %s, %s, %s)"
            valores = (id, nombre, apellido, curso, correo)
            cursor.execute(sql, valores)
            self.mydb.commit()

            self.mostrar_instructores()
            QMessageBox.information(self, "Éxito", "Instructor registrado correctamente")

        except mysql.connector.Error as err:
            QMessageBox.warning(self, "Error", f"Error al registrar instructor: {err}")

    def mostrar_instructores(self):
        try:
            cursor = self.mydb.cursor()
            cursor.execute("SELECT * FROM Instructor")
            resultados = cursor.fetchall()

            self.modelo.clear()
            columnas = len(resultados[0])
            self.modelo.setColumnCount(columnas)
            self.modelo.setRowCount(len(resultados))

            for i, fila in enumerate(resultados):
                for j, dato in enumerate(fila):
                    celda = QStandardItem(str(dato))
                    self.modelo.setItem(i, j, celda)

        except mysql.connector.Error as err:
            QMessageBox.warning(self, "Error", f"Error al mostrar instructores: {err}")
 

class AlumnoWindow(QMainWindow):
    def __init__(self, mydb, parent=None):
        super().__init__(parent)
        self.mydb = mydb
        loadUi('alumno.ui', self)

        self.tabla = self.tb_listar
        self.modelo = QStandardItemModel()
        self.tabla.setModel(self.modelo)

        self.btn_ingresar.clicked.connect(self.registrar_alumno)
        self.btn_retornar.clicked.connect(self.cerrar)
        
    def cerrar(self):
        self.hide()
        vent=Ui_menu(self)
        vent.show() 

        self.mostrar_alumnos()

    def registrar_alumno(self):
        id = self.txt_id.text()
        nombre = self.txt_nom.text()
        apellido = self.txt_ape.text()  
        dni = self.txt_dni.text()      

        try:
            cursor = mydb.cursor()
            sql = "INSERT INTO Alumnos (ID, Nombre, Apellido, DNI) VALUES (%s, %s, %s, %s)"
            valores = (id, nombre, apellido, dni)
            cursor.execute(sql, valores)
            mydb.commit()

            self.mostrar_alumnos()
            QMessageBox.information(self, "Éxito", "Alumno registrado correctamente")

        except mysql.connector.Error as err:
            QMessageBox.warning(self, "Error", f"Error al registrar alumno: {err}")

    def mostrar_alumnos(self):
        try:
            cursor = mydb.cursor()
            cursor.execute("SELECT * FROM Alumnos")
            resultados = cursor.fetchall()

            self.modelo.clear()
            columnas = len(resultados[0])
            self.modelo.setColumnCount(columnas)
            self.modelo.setRowCount(len(resultados))

            for i, fila in enumerate(resultados):
                for j, dato in enumerate(fila):
                    celda = QStandardItem(str(dato))
                    self.modelo.setItem(i, j, celda)

        except mysql.connector.Error as err:
            QMessageBox.warning(self, "Error", f"Error al mostrar alumnos: {err}")

def main():
    app = QApplication(sys.argv)
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='entregable_02'
    )
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()