seguir = True
while seguir:
    N = int(input("Ingresa un número igual o mayor a 3: "))
    while N < 3:
        N = int(input("El número es menor a 3, por favor, ingresalo de nuevo: "))

    def matriz_espiral(rango):
        matriz = [[0 for _ in range(rango)] for _ in range(rango)]
        arriba = 0
        abajo = rango - 1
        izquierda = 0
        derecha = rango - 1    
        numero = 1
        
        while arriba <= abajo and izquierda <= derecha:      
            for i in range(izquierda, derecha + 1):
                matriz[arriba][i] = numero
                numero += 1
            arriba += 1       
            for i in range(arriba, abajo + 1):
                matriz[i][derecha] = numero
                numero += 1
            derecha -= 1        
            if arriba <= abajo:
                for i in range(derecha, izquierda - 1, -1):
                    matriz[abajo][i] = numero
                    numero += 1
                abajo -= 1     
            if izquierda <= derecha:
                for i in range(abajo, arriba - 1, -1):
                    matriz[i][izquierda] = numero
                    numero += 1
                izquierda += 1
        return matriz

    def imprimir_matriz(matriz):
        for fila in matriz:
            for valor in fila:
                print(f"{valor}\t", end="") 
            print()

    imprimir_matriz(matriz_espiral(N))

    respuesta = input("¿Quiere seguir? (SI/NO): ")
    if respuesta == "NO":
        seguir = False