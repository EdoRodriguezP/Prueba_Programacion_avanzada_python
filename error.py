
# Definición de excepciones personalizadas para el sistema de anuncios y campañas

class LargoExcedidoError(Exception):
    """Excepción lanzada cuando el nombre de la campaña supera los 250 caracteres."""
    pass

class SubTipoInvalidoError(Exception):
    """Excepción lanzada cuando se asigna un subtipo no permitido a un anuncio."""
    pass
