
# Script de demostración para modificar atributos de una campaña y manejar excepciones
from campana import Campaña
from error import LargoExcedidoError, SubTipoInvalidoError

# Crear una campaña con un solo anuncio de tipo Video
anuncios_data = [
    {
        'tipo': 'Video',
        'url_archivo': 'video.mp4',
        'url_clic': 'https://ejemplo.com',
        'sub_tipo': 'instream',
        'duracion': 10
    }
]

campaña = Campaña('Campaña 1', anuncios_data)
print(campaña)

try:
    # Solicitar nuevo nombre de campaña
    nuevo_nombre = input('Ingrese nuevo nombre para la campaña: ')
    campaña.nombre = nuevo_nombre
    # Solicitar nuevo subtipo para el anuncio
    nuevo_subtipo = input('Ingrese nuevo subtipo para el anuncio de video: ')
    campaña.anuncios[0].sub_tipo = nuevo_subtipo
except (LargoExcedidoError, SubTipoInvalidoError) as e:
    # Escribir mensaje de error en error.log
    with open('error.log', 'a') as f:
        f.write(str(e) + '\n')
    print(f"Error: {e}")
