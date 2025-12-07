import math
def normalizar(lista, modo):
    match modo:
        case "minmax":
                return minmax(lista)
        case "zscore":
            return zscore(lista)
        case "unit":
            return unit(lista)

def minmax(lista):
    nueva_lista = []
    maximo = max(lista)
    minimo = min(lista)
    for i in range(len(lista)):
        nueva_lista.append((lista[i] - minimo) / (maximo - minimo))
    return nueva_lista

def zscore(lista):
    nueva_lista = []
    media = sum(lista) / len(lista)
    varianza = sum([(x - media) ** 2 for x in lista]) / len(lista)
    desviacion_estandar = math.sqrt(varianza)
    for i in range(len(lista)):
        nueva_lista.append((lista[i] - media) / desviacion_estandar)
    return nueva_lista

def unit(lista):
    nueva_lista = []
    lista_cuadrado = []
    for i in range(len(lista)):
        lista_cuadrado.append(lista[i] ** 2)
    norma_vector = math.sqrt(sum(lista_cuadrado))
    for i in range(len(lista)):
        nueva_lista.append(lista[i] / norma_vector)
    return nueva_lista

seguir = True
while seguir:
    modo = input("Ingresa el modo a usar (minmax/zscore/unit): ").lower()
    entrada = input("Ingresa la lista a normalizar (ej: 1 2 3 4 5): ")
    lista_strings = entrada.split() 
    lista = [float(numero) for numero in lista_strings] 

    print(normalizar(lista, modo))
    respuesta = input("¿Quiere seguir? (SI/NO): ").upper()
    if respuesta == "NO":
        seguir = False