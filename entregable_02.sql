CREATE TABLE Alumnos (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(25),
    Apellido VARCHAR(25),
    DNI VARCHAR(8) UNIQUE
);

CREATE TABLE Instructor (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(25),
    Apellido VARCHAR(25),
    Curso VARCHAR(25),
    Correo VARCHAR(40)
);
CREATE TABLE usuarios (
    nombre VARCHAR(50),
    rol VARCHAR(20)
);

INSERT INTO Alumnos (Nombre, Apellido, DNI) VALUES ('Jean Carlos', 'Zapata Reyes', '75388910');
INSERT INTO Instructor (Nombre, Apellido, Curso, Correo) VALUES ('Carlos Alberto', 'Zapata Peña', 'Tec. Programacion', 'carloszapta@instituto.com');
INSERT INTO usuarios (nombre, rol) VALUES ('Juan', 'Admin');
INSERT INTO usuarios (nombre, rol) VALUES ('María', 'Usuario');
INSERT INTO usuarios (nombre, rol) VALUES ('Pedro', 'Moderador');
