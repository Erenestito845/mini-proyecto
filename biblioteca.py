# Importar cliente en la libreria de mongo
from pymongo import MongoClient
# Establecer conexion de mongo
client = MongoClient("mongodb://localhost:27017/")
# Acceder a la base de datos Biblioteca
db = client["Biblioteca"]
# seleccionar la colección "libros" dentro de la base de datos
coleccion = db["libros"]

''' 
Para mostrar todos los libros almacenados en la colección, 
puedes iterar sobre el resultado de la consulta find() y acceder a los campos deseados.

for libro in coleccion.find():
    print(libro["codigo"])
    print(libro["titulo"])
    print("----------------")
'''

# Buscar por categoría
'''
categoria = input("Ingresar categoría:")
resultado = coleccion.find({"categoria": categoria})
for libro in resultado:
    print(libro["titulo"])
'''
# Eliminiar un libro 
'''
coleccion.delete_one({"codigo": "LIB006"})
print("Libro eliminado") 
'''
#hola que tal