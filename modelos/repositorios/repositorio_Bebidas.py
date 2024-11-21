from modelos.entidades.bebidaConAlcohol import BebidaConAlcohol
from modelos.entidades.bebidaSinAlcohol import BebidaSinAlcohol
from modelos.entidades.bebida import Bebida
import json

class RepositorioBebidas:
    ruta_archivo = "datos/bebidas.json"

    def __init__(self):
        self.__bebidas = []
        self.__cargarBebidas()

    def __cargarBebidas(self):
        try:
            with open(RepositorioBebidas.ruta_archivo, "r") as archivo:
                lista_dicc_bebidas = json.load(archivo)
                for bebida in lista_dicc_bebidas:
                    if "graduacionAlcoholica" in bebida:
                        self.__bebidas.append(BebidaConAlcohol.fromDiccionario(bebida))
                    else:
                        self.__bebidas.append(BebidaSinAlcohol.fromDiccionario(bebida))
        except FileNotFoundError:
            print("No se encontró el archivo de bebidas")
        except Exception as e:
            print("Error cargando las bebidas del archivo.\n" + str(e))

    def __guardarBebidas(self):
        try:
            with open(RepositorioBebidas.ruta_archivo, "w") as archivo:
                lista_dicc_bebidas = [bebida.toDiccionario() for bebida in self.__bebidas]
                json.dump(lista_dicc_bebidas, archivo, indent=4)
        except Exception as e:
            print("Error guardando las bebidas en el archivo.\n" + str(e))
    
    def obtenerBebidas(self):
        """Retorna una lista con todas las bebidas"""
        return self.__bebidas
    
    def obtenerBebidaPorNombre(self, nombre:str):
        """Retorna la bebida con el nombre indicado, None si no existe"""
        for bebida in self.__bebidas:
            if bebida.obtenerNombre() == nombre:
                return bebida
        return None
    
    def existeBebida(self, nombre:str):
        """Retorna True si existe una bebida con el nombre indicado, False en caso contrario"""
        return self.obtenerBebidaPorNombre(nombre) != None
    

    
