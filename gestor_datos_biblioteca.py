import sys
import pickle

# Ruta fija establecida manualmente
sys.path.append(r"C:\americo\BackEnd\clase_aitor\docu\B-POO")  # Ajusta la ruta según tu ubicación

DATA_PATH = r"C:\americo\BackEnd\clase_aitor\docu\B-POO\materiales_biblioteca.pkl"

print("Ruta completa del archivo:", DATA_PATH)

class GestorBiblioteca:
    def __init__(self):
        self.materiales = self.cargar_materiales()
    
    def almacenar_materiales(self):
        with open(DATA_PATH, "wb") as archivo:
            pickle.dump(self.materiales, archivo)
        #for material in self.materiales:
        #    print(f"Material '{material.titulo}' almacenado correctamente.")
    
    def cargar_materiales(self):
        try:
            with open(DATA_PATH, "rb") as archivo:
                materiales = pickle.load(archivo)
            print("Materiales cargados desde el archivo.")
            return materiales
        except FileNotFoundError:
            print("No se encontró el archivo de materiales.")
            return []
