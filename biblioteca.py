# biblioteca.py
from datetime import datetime  # Importamos la biblioteca para manejar fechas y horas
from datetime import time   
from abc import ABC, abstractmethod
import sys
sys.path.append(r"C:\americo\BackEnd\clase_aitor\docu\B-POO")  # Ajusta la ruta según tu ubicación
from validar_campo import validate_string, validate_date, validate_integer, validate_float

# Clase abstracta que representa un material de biblioteca
from abc import ABC, abstractmethod

class MaterialBiblioteca(ABC):
    def __init__(self, titulo, autor, codigo_inventario, ubicacion, tipo_material, disponible=True):
        self.__titulo = titulo
        self.__autor = autor
        self.__codigo_inventario = codigo_inventario
        self.__ubicacion = ubicacion
        self.__disponible = disponible
        self.__tipo_material = tipo_material

    # Propiedad para Título
    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, value):
        self.__titulo = value

    # Propiedad para Autor
    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, value):
        self.__autor = value

    # Propiedad para Código de Inventario
    @property
    def codigo_inventario(self):
        return self.__codigo_inventario

    @codigo_inventario.setter
    def codigo_inventario(self, value):
        self.__codigo_inventario = value

    # Propiedad para Ubicación
    @property
    def ubicacion(self):
        return self.__ubicacion

    @ubicacion.setter
    def ubicacion(self, value):
        self.__ubicacion = value

    # Propiedad para Disponible
    @property
    def disponible(self):
        return self.__disponible

    @disponible.setter
    def disponible(self, value):
        self.__disponible = value

    # Propiedad para Tipo de Material
    @property
    def tipo_material(self):
        return self.__tipo_material

    @tipo_material.setter
    def tipo_material(self, value):
        self.__tipo_material = value

    # Métodos de gestión
    def trasladar(self, nueva_ubicacion):
        self.ubicacion = nueva_ubicacion
        print(f"El item '{self.titulo}' ha sido trasladado a '{nueva_ubicacion}'.")

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"El item '{self.titulo}' ha sido prestado.")
        else:
            print(f"El item '{self.titulo}' no está disponible.")

    def devolver(self):
        self.disponible = True
        print(f"El item '{self.titulo}' ha sido devuelto.")

    @abstractmethod
    def mostrar_info(self):
        # Versión base corregida (puedes elegir implementarla o dejarla abstracta)
        info = (
            f"Tipo: {self.tipo_material}\n"
            f"Título: {self.titulo}\n"
            f"Autor: {self.autor}\n"
            f"Código de Inventario: {self.codigo_inventario}\n"
            f"Ubicación: {self.ubicacion}\n"
            f"Disponible: {self.disponible}\n"
        )
        print(info)


# Subclase para Libro

# Se asume que MaterialBiblioteca ya está definida en otro módulo
class Libro(MaterialBiblioteca):
    def __init__(self, titulo, autor, codigo_inventario, ubicacion, disponible,
                 isbn, numero_paginas, editorial, fecha_publicacion, edicion, 
                 idioma, peso_libro, formato_libro, tipo_literatura, resena):
        # Se asignan los atributos comunes a través de la clase base
        super().__init__(titulo, autor, codigo_inventario, ubicacion, "Libro", disponible)
        # Atributos específicos de Libro (almacenados como privados con name mangling)
        self.__ISBN = isbn
        self.__numero_paginas = numero_paginas
        self.__editorial = editorial
        self.__fecha_publicacion = fecha_publicacion
        self.__edicion = edicion
        self.__idioma = idioma
        self.__peso_libro = peso_libro
        self.__formato_libro = formato_libro
        self.__tipo_literatura = tipo_literatura
        self.__resena = resena

    # Propiedad para ISBN
    @property
    def ISBN(self):
        return self.__ISBN

    @ISBN.setter
    def ISBN(self, value):
        self.__ISBN = value

    # Propiedad para Número de Páginas
    @property
    def numero_paginas(self):
        return self.__numero_paginas

    @numero_paginas.setter
    def numero_paginas(self, value):
        self.__numero_paginas = value

    # Propiedad para Editorial
    @property
    def editorial(self):
        return self.__editorial

    @editorial.setter
    def editorial(self, value):
        self.__editorial = value

    # Propiedad para Fecha de Publicación
    @property
    def fecha_publicacion(self):
        return self.__fecha_publicacion

    @fecha_publicacion.setter
    def fecha_publicacion(self, value):
        self.__fecha_publicacion = value

    # Propiedad para Edición
    @property
    def edicion(self):
        return self.__edicion

    @edicion.setter
    def edicion(self, value):
        self.__edicion = value

    # Propiedad para Idioma
    @property
    def idioma(self):
        return self.__idioma

    @idioma.setter
    def idioma(self, value):
        self.__idioma = value

    # Propiedad para Peso del Libro
    @property
    def peso_libro(self):
        return self.__peso_libro

    @peso_libro.setter
    def peso_libro(self, value):
        self.__peso_libro = value

    # Propiedad para Formato del Libro
    @property
    def formato_libro(self):
        return self.__formato_libro

    @formato_libro.setter
    def formato_libro(self, value):
        self.__formato_libro = value

    # Propiedad para Tipo de Literatura
    @property
    def tipo_literatura(self):
        return self.__tipo_literatura

    @tipo_literatura.setter
    def tipo_literatura(self, value):
        self.__tipo_literatura = value

    # Propiedad para Reseña
    @property
    def resena(self):
        return self.__resena

    @resena.setter
    def resena(self, value):
        self.__resena = value


    def mostrar_info(self):
        # Primero muestra la información común definida en MaterialBiblioteca
        super().mostrar_info()
        # Luego, la información específica de Libro
        print(f"ISBN: {self.__ISBN}")
        print(f"Número de páginas: {self.__numero_paginas}")
        print(f"Editorial: {self.__editorial}")
        print(f"Fecha de publicación: {self.__fecha_publicacion}")
        print(f"Edición: {self.__edicion}")
        print(f"Idioma: {self.__idioma}")
        print(f"Peso del libro: {self.__peso_libro}")
        print(f"Formato del libro: {self.__formato_libro}")
        print(f"Tipo de literatura: {self.__tipo_literatura}")
        print(f"Reseña: {self.__resena}")        



# Subclase para Revista

# Detalles del producto
# ASIN = B0BRN4MDQW
# Editorial = RBA Revistas
# Fecha de publicación = 22 diciembre 2022
# Idioma = Español
# Longitud de impresión = 204 páginas
# Peso del producto = 330 g
# Dimensiones = 27.2 x 0.8 x 20.6 cm
# tipo formato = Tapa blanda, digital

class Revista(MaterialBiblioteca):
    def __init__(self, titulo, autor,  ISBN, codigo_inventario, numero_edicion, fecha_publicacion):
        super().__init__(titulo, autor,  ISBN, codigo_inventario)
        self.__numero_edicion = numero_edicion
        self.__fecha_publicacion = fecha_publicacion

    def get_numero_edicion(self):
        return self.__numero_edicion

    def set_numero_edicion(self, numero_edicion):
        self.__numero_edicion = numero_edicion

    def get_fecha_publicacion(self):
        return self.__fecha_publicacion

    def set_fecha_publicacion(self, fecha_publicacion):
        self.__fecha_publicacion = fecha_publicacion

    def mostrar_info(self):
        info = (
            f"Tipo: Revista\n"
            f"Título: {self.get_titulo()}\n"
            f"Autor: {self.get_autor()}\n"
            f"ISBN: {self.ISBN}\n"
            f"Código de Inventario: {self.codigo_inventario}\n"
            f"Número de edición: {self.__numero_edicion}\n"
            f"Fecha de publicación: {self.__fecha_publicacion}"
        )
        print(info)


# Subclase para DVD
class DVD(MaterialBiblioteca):
    def __init__(self, titulo, autor,  ISBN, codigo_inventario, duracion, formato):
        super().__init__(titulo, autor,  ISBN, codigo_inventario)
        self.__duracion = duracion
        self.__formato = formato

    def get_duracion(self):
        return self.__duracion

    def set_duracion(self, duracion):
        self.__duracion = duracion

    def get_formato(self):
        return self.__formato

    def set_formato(self, formato):
        self.__formato = formato

    def mostrar_info(self):
        info = (
            f"Tipo: DVD\n"
            f"Título: {self.get_titulo()}\n"
            f"Autor: {self.get_autor()}\n"
            f"ISBN: {self.ISBN}\n"
            f"Código de Inventario: {self.codigo_inventario}\n"
            f"Duración: {self.__duracion} minutos\n"
            f"Formato: {self.__formato}"
        )
        print(info)

