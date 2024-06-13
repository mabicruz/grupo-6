-- MOSTRAR Listado de bases de datos
SHOW DATABASES;

-- USO de bases de dato
USE melodist;

--- MOSTRAR TABLAS en base de datos melodist
SHOW tables;

-- CREAR TABLA artistas
CREATE TABLE artistas(
	id_artista INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(30)
    );

-- CREAR TABLA albums
CREATE TABLE albums(
	id_album INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(30),
    fecha_lanzamiento DATE NOT NULL,
    id_artista INT NOT NULL,
    FOREIGN KEY(id_artista) REFERENCES artistas(id_artista)
    );
    
-- CREAR TABLA generos(
CREATE TABLE generos(
	id_genero INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(30)
    );

-- CREAR TABLA canciones
CREATE TABLE canciones(
	id_cancion INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(30),
    id_genero INT NOT NULL,
    FOREIGN KEY(id_genero) REFERENCES artistas(id_genero),
    id_artista INT NOT NULL,
    FOREIGN KEY(id_artista) REFERENCES artistas(id_artista)
    );
    
-- Mostrar todos los datos de una tabla
SELECT * FROM canciones;

-- Mostrar una sola columna de una tabla
Select titulo FROM albums;

-- Mostrar valores con Where
Select nombre FROM generos WHERE id_genero = 3;

-- Mostrar valores con Where y between
SELECT titulo FROM albums WHERE fecha_lanzamiento between '2019-01-01' and '2022-12-31';

-- Mostrar valores con Where y limit
Select * FROM canciones WHERE id_genero = 1 LIMIT 4;


-- Mostrar mas de 1 tabla con inner join
SELECT a.nombre AS 'artista', c.titulo AS 'cancion' FROM canciones AS c
INNER JOIN artistas AS a ON a.id_artista = c.id_artista;
