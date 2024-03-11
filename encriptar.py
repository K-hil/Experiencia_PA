
def encriptar_mensaje(mensaje: str) -> str:
    """
    Esta función toma un mensaje como entrada y lo encripta utilizando un libro_super_secreto.txt. 
    Cada letra del mensaje se busca en el libro y se transforma en un string con la siguiente estructura:
    
    "numero_linea,numero_palabra,numero_letra_en_palabra"
    
    Donde:
    - numero_linea es la línea en la que se encuentra la letra en el libro.
    - numero_palabra es la palabra en la que se encuentra la letra en la línea.
    - numero_letra_en_palabra es la posición de la letra en la palabra.
    
    Luego se concatenan todos los strings de cada letra para formar el mensaje encriptado.
    Los espacios entre palabras se representan con un punto y coma (;).
    
    Recibe:
        mensaje (str): El mensaje que se va a encriptar.
        
    Retorna:
        str: El mensaje encriptado.
    """

    with open('libro_super_secreto.txt', 'r') as libro:
        lineas = libro.readlines()
        mensaje_encriptado = ''
        for letra in mensaje:
            if letra not in (' ', '\n'):
                pos_linea = encontrar_en_lineas(letra, lineas)
                pos_palabra, pos_letra = encontrar_en_palabras(letra, lineas[pos_linea].split(' '))
                mensaje_encriptado += f'{pos_linea},{pos_palabra},{pos_letra}'
            else:
                mensaje_encriptado += ';'
    return mensaje_encriptado


def encontrar_en_palabras(letra, palabras):
    for num_palabra, palabra in enumerate(palabras):
        for c_pos, c in enumerate(palabra):
            if c == letra:
                return num_palabra, c_pos
            
def encontrar_en_lineas(letra, lineas):
    for i, linea in enumerate(lineas):
        if letra in linea:
            return i
    return -1 