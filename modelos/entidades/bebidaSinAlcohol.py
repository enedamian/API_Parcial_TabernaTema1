from modelos.entidades.bebida import Bebida

class BebidaSinAlcohol(Bebida):
    def __init__(self, nombre:str, costo:float, stock:int, mililitros:int, sabor: str, natural: bool):
        super().__init__(nombre, costo, stock, mililitros)
        if not isinstance(sabor, str) or not sabor.strip():
            raise ValueError("El sabor debe ser un string y no puede estar vacío")
        if not isinstance(natural, bool):
            raise ValueError("El atributo natural debe ser booleano")
        self.__sabor = sabor
        self.__natural = natural
    
    
    def obtenerSabor(self):
        return self.__sabor
    
    def obtenerNatural(self):
        return self.__natural
    
    def establecerSabor(self, sabor:str):
        if not isinstance(sabor, str) or sabor == "":
            raise ValueError("El sabor no puede ser vacío")
        self.__sabor = sabor
    
    def establecerNatural(self, natural:bool):
        if not isinstance(natural, bool):
            raise ValueError("El atributo natural debe ser booleano")
        self.__natural = natural

    def obtenerPrecio(self):
        return self._costo * 1.5
    