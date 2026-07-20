# === EXAMEN TRANSVERSAL FINAL ==
from Funciones import *
from os import system
system("cls")

juegos = { # Titulo | Plataforma | Genero | Clasificacion | Multijugador | Editor
    'G001': ['Eclipse Runner', 'PC', 'accion', 'T', True,       'NovaStudio'],
    'G002': ['Puzzle Atlas', 'Switch', 'puzzle', 'E', False,    'BrightWorks'],
    'G003': ['Sky Legends', 'PS5', 'aventura', 'T', True,       'OrionGames'],
    'G004': ['Racing Pulse', 'PC', 'carreras', 'E', True,       'VelocityLab'],
    'G005': ['Mystic Farm', 'Switch', 'simulacion', 'E', False, 'GreenSeed'],
    'G006': ['Shadow Tactics', 'Xbox', 'estrategia', 'M', False,'IronGate']
}
inventario = { # Precio | Stock
    'G001': [9990, 7],
    'G002': [19990, 0],
    'G003': [42990, 3],
    'G004': [14990, 5],
    'G005': [17990, 9],
    'G006': [39990, 2],
}

system("cls")
while True:
    print("="*10,"MENÚ PRINCIPAL ","="*10)
    print("""1. Stock por plataforma
2. Búsqueda de juegos por rango de precio
3. Actualizar precio de juego
4. Agregar juego
5. Eliminar juego
6. Salir""")
    match leer_opcion():
        case 1:
            platform = input("Ingrese plataforma a consultar: ").lower()
            stock_plataforma(platform, juegos, juegos, inventario)
        case 2: 
            precio_min = validarInt(0, "inf", "Ingrese precio mínimo: ") 
            precio_max = validarInt(0, "inf", "Ingrese precio máximo: ")
            busqueda_precio(precio_min, precio_max, juegos, inventario)
        case 3:
            while True:
                codeInput = input("Ingrese codigo: ")
                existe_codigo = buscar_codigo(codeInput, inventario)
                #print(f"| Codigo ingresado: {codeInput} / Existe el codigo?: {existe_codigo} |") #debug
                if existe_codigo:
                    precio = int(input("Ingrese nuevo precio: "))
                    actualizar_precio(codeInput, precio, inventario)
                    opc = validar_bool("¿Desea actualizar otro precio (s/n)?:")
                    if not opc: break
                else: print("| El Codigo no existe")
        case 4:
            game = {
                "codigo": validar_codigo(inventario),
                "titulo": validarString("título"),
                "plataforma": validarString("plataforma"),
                "genero": validarString("género"),
                "clasificacion": validar_clasificacion(),
                "multiplayer": validar_multiplayer(),
                "editor": validarString("editor"),
                "precio":validar_precio(),
                "stock": validar_stock(),
            }
            agregar_juego(game["codigo"], game["titulo"], game["plataforma"],game["genero"],game["clasificacion"],game["multiplayer"],
            game["editor"], game["precio"], game["stock"], juegos, inventario)
        case 5: 
            while True:
                codeInput = input("Ingrese codigo: ")
                existe_codigo = buscar_codigo(codeInput, inventario)
                if existe_codigo:
                    juegos.pop(codeInput)
                    inventario.pop(codeInput)
                    print("Se ha eliminado el juego exitosamente!")
                    confirmar()
                    break
                else: print("| El Codigo no existe")
        case 6: 
            print("Programa finalizado")
            break
        #case _: print("Debe seleccionar una opción válida")
