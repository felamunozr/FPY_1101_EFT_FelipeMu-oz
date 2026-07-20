from os import system

# === Validaciones ===
def validarString(msg):
    while True:
        str = input(f"Ingrese {msg}: ")
        if str:
            if " " in str: print("ERROR: No debe contener espacios")
            else: return str
        else: print("ERROR: No debe estar vacio")

def validarInt(min, max, msg):
    while True:
        try:
            num = int(input(msg))
            if not max == "inf":
                if min<=num<=max:return num
                else: print(f"ERROR: El rango permitido es de {min}-{max}")
            else: 
                if min<=num: return num
                else: print(f"ERROR: El rango permitido es de {min}-{max}")
        except: 
            print("ERROR: Ingrese solo caracteres numericos")

def validar_bool(msg):
    while True:
        opc = input(msg).lower()
        match opc:
            case "s": return True
            case "n": return False
            case _: print("ERROR: Texto invalido")

# === Funciones Menu ===
def leer_opcion():
    opc = validarInt(1, 6, "Seleccione una opcion >> ")
    return opc

def confirmar():
    input("| Presione una tecla para continuar... |")
    system("cls")

# === Funciones Generales ===
def stock_plataforma(plataforma, list, inv):
    stockTotal = 0
    for i in list:
        if plataforma == list[i][1].lower():
            stockTotal += inv[i][1]
    print(f"El total de stock disponibles es: {stockTotal}")
    confirmar()

def busqueda_precio(p_min, p_max, list, inv):
    juegosEncontrados = []
    for i in inv:
        if (p_min<=inv[i][0]<=p_max) and (inv[i][1]>0): 
            juegosEncontrados.append(f"{list[i][0]}--{i}")
    juegosEncontrados.sort()
    print(juegosEncontrados)

def buscar_codigo(codigo, inventario):
    for i in inventario:
        if i==codigo: return True
 

def actualizar_precio(codigo, nuevo_precio, inv):
    inv[codigo][0] = nuevo_precio
    print("El precio ha sido actulizado")

# === VALIDACIONES JUEGO ===
def validar_codigo(inv):
    codeInput = input("Ingrese codigo: ")
    existe_codigo = buscar_codigo(codeInput, inv)
    if existe_codigo: print("El codigo ya existe")       
    else: return codeInput  

def validar_clasificacion():
    while True:
        clasificacion = validarString("clasificación").upper()
        if clasificacion == ("E" or "T" or "M"): return clasificacion
        else: print("ERROR: Clasificación invalida")

def validar_multiplayer():
    while True:
        opc = input("¿Es multiplayer? (s/n): ").lower()
        match opc:
            case "s": return True
            case "n": return False
            case _: print("ERROR: Texto invalido")

def validar_precio():
    precio = int(input("Ingrese precio: "))
    if precio>0: return precio

def validar_stock():
    stock = int(input("Ingrese stock: "))
    if stock>=0: return stock

def agregar_juego(codigo, titulo, plataforma, genero, clasificacion, multiplayer,
editor, precio, stock, list, inv):
    list[codigo] = [titulo, plataforma, genero, clasificacion, multiplayer, editor]
    inv[codigo] = [precio, stock]
    print(f"Se ha añadido el juego {titulo} al inventario exitosamente!:")
    confirmar()
