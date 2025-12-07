def agregar_estudiante(registro):
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = input("Ingrese la edad del estudiante: ")
    promedio = input("Ingrese el promedio del estudiante: ")
    
    try:
        promedio = float(promedio)
    except ValueError:
        print("Error: El promedio debe ser un número.")
        return

    estudiante = {
        "nombre": nombre,
        "edad": edad,
        "promedio": promedio
    }
    registro.append(estudiante)
    print("Estudiante agregado exitosamente.")

def mostrar_estudiantes(registro):
    if not registro:
        print("No hay estudiantes registrados.")
        return

    print("\n--- Lista de Estudiantes ---")
    for est in registro:
        print(f"Nombre: {est['nombre']}, Edad: {est['edad']}, Promedio: {est['promedio']:.2f}")

def mostrar_mejor_promedio(registro):
    if not registro:
        print("No hay estudiantes para comparar.")
        return
    
    mejor_estudiante = max(registro, key=lambda est: est['promedio'])
    
    print("\n--- Estudiante con Mejor Promedio ---")
    print(f"Nombre: {mejor_estudiante['nombre']}")
    print(f"Edad: {mejor_estudiante['edad']}")
    print(f"Promedio: {mejor_estudiante['promedio']:.2f}")

def buscar_por_nombre(registro):
    nombre_buscado = input("Ingrese el nombre del estudiante a buscar: ").lower()
    encontrado = None
    
    for est in registro:
        if est['nombre'].lower() == nombre_buscado:
            encontrado = est
            break
            
    if encontrado:
        print("\n--- Estudiante Encontrado ---")
        print(f"Nombre: {encontrado['nombre']}")
        print(f"Edad: {encontrado['edad']}")
        print(f"Promedio: {encontrado['promedio']:.2f}")
        print("------------------------------")
    else:
        print(f"Error: Estudiante con nombre '{nombre_buscado}' no encontrado.")
        
def eliminar_por_nombre(registro):
    nombre_eliminar = input("Ingrese el nombre del estudiante a eliminar: ").lower()
    
    registro_original_len = len(registro)
    registro[:] = [est for est in registro if est['nombre'].lower() != nombre_eliminar]
    
    if len(registro) < registro_original_len:
        print(f"Estudiante con nombre '{nombre_eliminar}' eliminado exitosamente.")
    else:
        print(f"Error: Estudiante con nombre '{nombre_eliminar}' no encontrado.")
        
def menu_principal():
    registro_estudiantes = []
    
    while True:
        print("\n=========> REGISTRO DE ESTUDIANTES <=========")
        print("1. Agregar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Mostrar estudiante con mejor promedio")
        print("4. Buscar por nombre")
        print("5. Eliminar por nombre")
        print("6. Salir")
        print("=============================================")
        
        opcion = input("Seleccione una opción (1-6): ")
        
        match opcion:
            case '1':
                agregar_estudiante(registro_estudiantes)
            case '2':
                mostrar_estudiantes(registro_estudiantes)
            case '3':
                mostrar_mejor_promedio(registro_estudiantes)
            case '4':
                buscar_por_nombre(registro_estudiantes)
            case '5':
                eliminar_por_nombre(registro_estudiantes)
            case '6':
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida. Por favor, intente de nuevo.")

menu_principal()