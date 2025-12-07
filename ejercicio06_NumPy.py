import numpy as np
def normalizar(lista, modo):
    lista_nueva = np.array(lista, dtype=float)
    match modo:
        case "minmax":
            return minmax(lista_nueva)
        case "zscore":
            return zscore(lista_nueva)
        case "unit":
            return unit(lista_nueva)

def minmax(arr):
    minimo = np.min(arr)
    maximo = np.max(arr)
    denominador = maximo - minimo
    resultado = (arr - minimo) / denominador
    return resultado.tolist()

def zscore(arr):   
    media = np.mean(arr)   
    desviacion_estandar = np.std(arr)
    resultado = (arr - media) / desviacion_estandar
    return resultado.tolist()

def unit(arr):
    norma_vector = np.linalg.norm(arr)
    resultado = arr / norma_vector
    return resultado.tolist() 

seguir = True
while seguir:
    modo = input("Ingresa el modo a usar (minmax/zscore/unit): ")
    entrada = input("Ingresa la lista a normalizar (ej: 1 2 3 4 5): ")
    lista_strings = entrada.split()
    lista = [float(numero) for numero in lista_strings]
    print(normalizar(lista, modo))
        
    respuesta = input("¿Quiere seguir? (SI/NO): ").upper()
    if respuesta == "NO":
        seguir = False