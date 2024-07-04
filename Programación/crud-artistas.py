import mysql.connector 
import os

    def Insertar(self):
        print("========================================================================")
        print("-------------------CREAR ARTISTA----------------------------------------")
        print("========================================================================")
        nombre = input("Ingrese el nombre del artista: \n")
        sql = "insert into artistas(nombre) values('{}')".format(nombre)
        self.cursor.execute(sql)
        print("nombre del artista ingresado correctamete \n")
        self.conexion.commit()
        os.system('pause')
        
    def Mostrar(self):
        print("========================================================================")
        print("-------------------LISTA DE ASTISTAS------------------------------------")
        print("========================================================================")
        sql= "select * from artistas"
        self.cursor.execute(sql)
        artistas = self.cursor.fetchall()
        """ print(artistas) """
        for i in artistas:
            print("Nombre del artista: ", i[1])
            
    def Actualizar(self):
        print("========================================================================")
        print("-------------------EDITAR ARTISTA---------------------------------------")
        print("========================================================================")
        nombre = input("Ingrese el nombre del artista a editar \n")
        nuevo_nombre = input("Ingrese el nuevo nombre \n")
        sql = "update artistas set nombre = '{}' where nombre= '{}'".format(nuevo_nombre, nombre)
        self.cursor.execute(sql)
        print("Artista actualizado! \n")
        self.conexion.commit()
        
app = App()
""" app.Insertar() 
app.Mostrar() 
app.Actualizar() 
app.Mostrar() """
