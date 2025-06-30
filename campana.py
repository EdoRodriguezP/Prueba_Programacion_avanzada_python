
# Definición de la clase Campaña y su lógica de composición
from error import LargoExcedidoError
from anuncio import Anuncio, Video, Display, Social

class Campaña:
    # Clase que representa una campaña publicitaria
    def __init__(self, nombre, anuncios_data, fecha_inicio=None, fecha_termino=None):
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self._anuncios = self._crear_anuncios(anuncios_data)
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, value):
        # Validar largo del nombre
        if len(value) > 250:
            raise LargoExcedidoError("El nombre de la campaña supera los 250 caracteres.")
        self.__nombre = value

    @property
    def fecha_inicio(self):
        return self.__fecha_inicio
    @fecha_inicio.setter
    def fecha_inicio(self, value):
        self.__fecha_inicio = value

    @property
    def fecha_termino(self):
        return self.__fecha_termino
    @fecha_termino.setter
    def fecha_termino(self, value):
        self.__fecha_termino = value

    @property
    def anuncios(self):
        # Solo getter, no setter
        return self._anuncios

    def _crear_anuncios(self, anuncios_data):
        # Método privado para crear instancias de anuncios
        lista = []
        for data in anuncios_data:
            tipo = data.get('tipo')
            if tipo == 'Video':
                lista.append(Video(data['url_archivo'], data['url_clic'], data['sub_tipo'], data['duracion']))
            elif tipo == 'Display':
                lista.append(Display(data['ancho'], data['alto'], data['url_archivo'], data['url_clic'], data['sub_tipo']))
            elif tipo == 'Social':
                lista.append(Social(data['ancho'], data['alto'], data['url_archivo'], data['url_clic'], data['sub_tipo']))
        return lista

    def __str__(self):
        # Retornar nombre y cantidad de anuncios por tipo
        n_video = sum(isinstance(a, Video) for a in self._anuncios)
        n_display = sum(isinstance(a, Display) for a in self._anuncios)
        n_social = sum(isinstance(a, Social) for a in self._anuncios)
        return f"Nombre de la campaña: {self.nombre}\nAnuncios: {n_video} Video, {n_display} Display, {n_social} Social"
