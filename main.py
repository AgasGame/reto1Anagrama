
 # * Reto de Mouredev: shorturl.at/bhKNW
 # * Reto #1
 # * ¿ES UN ANAGRAMA?

 # * Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
 # * Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
 # * NO hace falta comprobar que ambas palabras existan.
 # * Dos palabras exactamente iguales no son anagrama.

def isAnagrama(pal1,pal2):
    pal1 = pal1.lower()
    pal2 = pal2.lower()

    if pal1 == pal2:
        return False

    return (sorted(pal1) == sorted(pal2))



print(isAnagrama('amor','roma'))