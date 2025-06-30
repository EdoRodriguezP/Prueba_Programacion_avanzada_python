
# Definición de clases para los diferentes tipos de anuncios
from abc import ABC, abstractmethod
from error import SubTipoInvalidoError

class Anuncio(ABC):
    # Clase base para anuncios
    def __init__(self, ancho, alto, url_archivo, url_clic, sub_tipo):
        # Validación de ancho y alto
        self.ancho = ancho
        self.alto = alto
        self.__url_archivo = url_archivo
        self.__url_clic = url_clic
        self.sub_tipo = sub_tipo

    @property
    def ancho(self):
        return self._ancho
    @ancho.setter
    def ancho(self, value):
        # Validar que el ancho sea mayor a 0
        self._ancho = value if value > 0 else 1

    @property
    def alto(self):
        return self._alto
    @alto.setter
    def alto(self, value):
        # Validar que el alto sea mayor a 0
        self._alto = value if value > 0 else 1

    @property
    def url_archivo(self):
        return self.__url_archivo
    @url_archivo.setter
    def url_archivo(self, value):
        
        self.__url_archivo = value

    @property
    def url_clic(self):
        return self.__url_clic
    @url_clic.setter
    def url_clic(self, value):
        # Asignación básica
        self.__url_clic = value

    @property
    def sub_tipo(self):
        return self._sub_tipo
    @sub_tipo.setter
    def sub_tipo(self, value):
        # Validar que el subtipo esté permitido
        if not hasattr(self.__class__, "SUB_TIPOS") or value not in getattr(self.__class__, "SUB_TIPOS", []):
            raise SubTipoInvalidoError(
                f"Subtipo '{value}' no permitido para formato {getattr(self.__class__, 'FORMATO', 'Desconocido')}"
            )
        self._sub_tipo = value

    @staticmethod
    def mostrar_formatos():
        # Mostrar formatos y subtipos disponibles
        for cls in Anuncio.__subclasses__():
            formato = getattr(cls, "FORMATO", None)
            sub_tipos = getattr(cls, "SUB_TIPOS", [])
            if formato and sub_tipos:
                print(f"FORMATO: {formato}\n==========")
                for subtipo in sub_tipos:
                    print(f"- {subtipo}")
                print()

    @abstractmethod
    def comprimir_anuncio(self):
        pass

    @abstractmethod
    def redimensionar_anuncio(self):
        pass

# Ejemplo de subclase correctamente definida
class AnuncioVideo(Anuncio):
    FORMATO = "Video"
    SUB_TIPOS = ["Corto", "Largo"]

class AnuncioImagen(Anuncio):
    FORMATO = "Imagen"
    SUB_TIPOS = ["Banner", "Cuadrado"]

class Video(Anuncio):
    FORMATO = "Video"
    SUB_TIPOS = ("instream", "outstream")

    def __init__(self, url_archivo, url_clic, sub_tipo, duracion):
        # Video siempre tiene ancho y alto igual a 1
        super().__init__(1, 1, url_archivo, url_clic, sub_tipo)
        self.duracion = duracion

    @property
    def ancho(self):
        return 1
    @ancho.setter
    def ancho(self, value):
        pass  # No se puede modificar

    @property
    def alto(self):
        return 1
    @alto.setter
    def alto(self, value):
        pass  # No se puede modificar

    @property
    def duracion(self):
        return self._duracion
    @duracion.setter
    def duracion(self, value):
        # Validar duración mayor a 0
        self._duracion = value if value > 0 else 5

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")

class Display(Anuncio):
    FORMATO = "Display"
    SUB_TIPOS = ("tradicional", "native")

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")

class Social(Anuncio):
    FORMATO = "Social"
    SUB_TIPOS = ("facebook", "linkedin")

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")
