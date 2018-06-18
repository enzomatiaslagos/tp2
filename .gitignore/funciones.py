import random

def textoNuevo(lista):
    """Convierrte la lista de oraciones en texto"""
    texto = " ".join(lista)
    texto = texto.upper()
    return texto



def numeroJugadores(max_jugadores):
    """Devulve cantidad de jugadores"""
    seguir = True
    while seguir:
        cantJugadores = int(input("Cantidad de jugadores:"))
        if 2 <= cantJugadores <= max_jugadores:
            seguir = False
        else:
            print("Cantidad incorrecta, vuelva a ingresar cantidad de jugadores.")
    return cantJugadores

def jugadores(cantJugadores):
    """Devuelve diccionario con el nombre de los jugadores y su orden de juego (que fue dado de manera aleatoria)"""
    nombreJugadores = []
    while len(nombreJugadores) != cantJugadores:
        nombreJugadores.append(str(input("Ingrese nombre y apellido:")).upper())
    orden = range(1, cantJugadores + 1)
    import random
    nombresAleatorios = random.sample(nombreJugadores,
                                      cantJugadores)  # Da un orden aleatorio en que fueron ingresados los nombres
    jugadoresYSuOrden = dict(zip(nombresAleatorios, orden))
    for clave, valor in jugadoresYSuOrden.items():
        print("El jugador", clave, "jugara en la posicion", valor)
    return jugadoresYSuOrden

def listaNombres(jugadoresYSuOrden):
    """Devuelve lista con nombre de los jugadores"""
    nombres = list(jugadoresYSuOrden.keys())
    return nombres

def largoPalabra(long_palabra_min):
    """Devuelve el largo elegido para jugar"""
    seguir = True
    while seguir:
        largo = int(input("Ingrese largo de la palabra, mayor a 5, con la que quiere jugar:"))
        if largo >= long_palabra_min:
            seguir = False
        else:
            print("Ingrese otro largo, no existen palabras para el largo ingresado.")
    return largo

def asignacionPalabra(listaJugadores,listaPalabras,largo):
    """Asigna palabras a cada jugador"""
    jugadoresYPalabra = {}
    palabrasDelLargo = []
    for palabra in listaPalabras:
        if len(palabra) == largo:
            palabrasDelLargo.append(palabra)
    for nombre in listaJugadores:
        jugadoresYPalabra[nombre] = random.choice(palabrasDelLargo)
    return jugadoresYPalabra

def agregarPalabraAlDiccResultados(jugadoresYPalabra, diccResultados):
    for jugador in jugadoresYPalabra:
        diccResultados[jugador][3].append(jugadoresYPalabra[jugador])

def palabra_a_adivinar(jugadoresYPalabra,largo):
    """genera diccionario con todo lo necesario para la partida"""
    diccionario = {}
    vacio = 0
    for jugadores in jugadoresYPalabra:
        diccionario[jugadores] = [jugadoresYPalabra[jugadores],[],vacio,vacio,vacio,[],vacio]
        for i in range(largo):
                diccionario[jugadores][1].append("-")
        """posiciones={nombre:palabra,palabra_adivinada,puntos,aciertos,desaciertos,letras_ingresadas,intentos}"""
    return diccionario

def ingreso_letra(letras_anteriores):
    """pide el ingreso y lo valida"""
    letra = input("ingresar letra: ")
    letra = letra.upper()
    continuar = True
    while continuar == True:
        if letra.isalpha() != True:
            letra = input("Error, ingrese una letra valida: ")
            letra = letra.upper()
        elif letra in letras_anteriores:
            letra=input("Por favor, ingrese una letra que no haya intentado anteriormente:")
            letra = letra.upper()
        else:
            continuar = False
    return (letra)

def diccionario_a_variable(diccionario,jugador):
    """pasa los valores del diccionario a variables para tratalos mas facil"""
    palabra = diccionario[jugador][0]
    lista_aciertos = diccionario[jugador][1]
    puntos = diccionario[jugador][2]
    aciertos = diccionario[jugador][3]
    desaciertos = diccionario[jugador][4]
    letras_ingresadas = diccionario[jugador][5]
    intentos = diccionario[jugador][6]
    return palabra,lista_aciertos,puntos,aciertos,desaciertos,letras_ingresadas,intentos


def posicion_adivinada(palabra,letra,lista_aciertos):
    """si la letra esta en la palabra, la reemplaza en la lista de los aciertos"""
    lista_palabra = []
    for caracter in palabra:
            lista_palabra.append(caracter)
    largo_palabra = len(lista_palabra)
    if letra in lista_palabra:
            for i in range(0,largo_palabra):
                    if letra == lista_palabra[i]:
                            lista_aciertos[i]=letra
    print(lista_aciertos)
    return lista_aciertos

def ganador(palabra,lista_aciertos):
    """se fija si gano una persona"""
    lista_palabra = list(palabra)
    return (lista_palabra == lista_aciertos)


def gana_maquina(diccionario,cantidad, max_desaciertos):
    """se fija si gano la maquina"""
    maquina = 0
    for clave in diccionario:
        if diccionario[clave][4]==max_desaciertos:
            maquina += 1
            print(maquina)
    if maquina == cantidad:
        return True
    else:
        return False

def aciertos_o_desaciertos(letra,palabra):
    """se fija si acerto o erro"""
    if letra in palabra:
        return True
    else:
        return False


def suma_cantidad_de_caractes(variable_a_sumar,letra,palabra, puntos_aciertos):
    """suma la cantidad de caracteres que haya: sirve tanto para puntos, como para aciertos"""
    for caracter in palabra:
        if caracter == letra:
            variable_a_sumar += puntos_aciertos
    return variable_a_sumar

def suma_puntos(puntos,letra,palabra,lista_aciertos, puntos_desaciertos, puntos_adivina):
    """asigna los puntos a cada participante en el turno"""
    if ganador(palabra,lista_aciertos):
        puntos += puntos_adivina
    elif letra in palabra:
        return suma_cantidad_de_caractes(puntos,letra,palabra)
    else:
        puntos -= puntos_desaciertos
    return puntos


def diccionario_resultados(lista_nombres):
    """diccionario con los resultados de cada partida indicando puntos, aciertos y desaciertos"""
    diccionario = {}
    for nombres in lista_nombres:
        diccionario[nombres] = [0,0,0]
    return diccionario

def autoriza_jugar(desaciertos,intentos):
    """se fija si cumple las condiciones para jugar o si ya perdio"""
    return (desaciertos < 7)


def diccionario_gana_maquina(diccionario_jugadores):
    """creamos diccionario para pasar los datos mas facil al diccionario de resultados, a diferencia del anterior este
    contiene a todos los jugadores"""
    dicc_jugadores = {}
    for jugador in diccionario_jugadores:
            dicc_jugadores[jugador] = [diccionario_jugadores[jugador][2], diccionario_jugadores[jugador][3],
                                             diccionario_jugadores[jugador][4]]
    return dicc_jugadores

def diccionario_ganador_jugador(clave,diccionario_jugadores):
    """creo diccionario de los perdedores para ordenarlos"""
    dicc_otros_jugadores = {}
    for jugador in diccionario_jugadores:
        if jugador != clave:
            dicc_otros_jugadores[jugador] = [diccionario_jugadores[jugador][2], diccionario_jugadores[jugador][3],
                                             diccionario_jugadores[jugador][4]]
    return dicc_otros_jugadores

def diccionario_gana_maquina(diccionario_jugadores):
    """diccionario que si gana la maquina despues le pasa los puntos al diccionario resultados"""
    dicc_resultados = {}
    for jugador in diccionario_jugadores:
        dicc_resultados[jugador] = [diccionario_jugadores[jugador][2], diccionario_jugadores[jugador][3],
                                    diccionario_jugadores[jugador][4]]
    return dicc_resultados

def creacion_diccionario_resultados(diccionario_jugadores):#jug y palabras
    """Crea las poscisiones para el diccionario de los resultados finales""" #AZUL
    dicc_resultados = {}
    for jugador in diccionario_jugadores:
        dicc_resultados[jugador] = [0,0,0, []]#lista vacia ==> palabras
        dicc_resultados[jugador][3].append(diccionario_jugadores[jugador])
    return dicc_resultados


def variable_a_diccionario(palabra,lista_aciertos,puntos,aciertos,desaciertos,letras_anteriores,intentos,clave,diccionario):
    """vuelve a asignarle los valores al diccionario del juego"""
    diccionario[clave][0] = palabra
    diccionario[clave][1] = lista_aciertos
    diccionario[clave][2] = puntos
    diccionario[clave][3] = aciertos
    diccionario[clave][4] = desaciertos
    diccionario[clave][5] = letras_anteriores
    diccionario[clave][6] = intentos
    return diccionario

def diccionario_lista_jugadores(diccionario_ordenado, long_palabra_min):
    """deuvuelve los jugadores con su palabra asignada y el largo de la palabra"""
    lista_nombres = listaNombres(diccionario_ordenado)
    largo = largoPalabra(long_palabra_min)
    listaPalabrasValidas = lista_Palabras(largo)
    jugadores_palabra = asignacionPalabra(lista_nombres, listaPalabrasValidas, largo)
    return jugadores_palabra,largo

def diccionario_suma_resultados(diccionario,diccionario_resultados):
    for jugador in diccionario:
        largo = len(diccionario[jugador])
        for i in range(largo):
            diccionario_resultados[jugador][i] = diccionario_resultados[jugador][i] + diccionario[jugador][i]
    return diccionario_resultados

def impresion_de_resultados(dicc_resultados,partida):
    print(" ")
    print("Partida numero: ",partida)
    print(" ")
    print("Los resultados generales son: ")
    print(dicc_resultados)
    for jugadores in dicc_resultados:
        print("jugador:", jugadores)
        print("puntos: ", dicc_resultados[jugadores][0])
        print("aciertos: ",dicc_resultados[jugadores][1])
        print("desaciertos: ",dicc_resultados[jugadores][2])
        print(" ")
    return dicc_resultados

def nuevo_orden_gana_jugador(dicc_ganador,dicc_perdedores,dicc_resultados):
    nuevo_orden ={}
    nuevo_orden.update(dicc_ganador)
    dicc_perdedores = dict(sorted(dicc_perdedores.items(), key=lambda x: x[1], reverse= True))
    for jugador in dicc_perdedores:
        nuevo_orden[jugador] = dicc_resultados[jugador]
    return nuevo_orden

def funcion_datos_a_variables():
    configuraciones = open("configuracion.txt", "r")
    max_player = datosAVariables(configuraciones)
    long_palabra_min = datosAVariables(configuraciones)
    max_desaciertos = datosAVariables(configuraciones)
    puntos_aciertos = datosAVariables(configuraciones)
    puntos_desaciertos = datosAVariables(configuraciones)
    puntos_adivina = datosAVariables(configuraciones)
    configuraciones.close()
    return max_player,long_palabra_min,max_desaciertos,puntos_aciertos,puntos_desaciertos,puntos_adivina

def datosAVariables(configuraciones):
    linea = configuraciones.readline()
    nombre,valor = linea.split(" ")
    valor.strip('\n')
    valor = int(valor)
    return valor

def lista_Palabras(largoPalabra):
    archivo = open('palabrasMezcladas.txt','r')
    lista=[]
    for linea in archivo:
        linea = linea.strip('\n')
        if len(linea) == largoPalabra:
            lista.append(linea)
    archivo.close()
    return lista

def abrirArchivo (nombreArchivo):
    archivo = open(nombreArchivo, "r")
    return archivo

def texto(archivo, long_palabra_min):
    lista_valida = []
    reemplazar = open('reemplazar.csv','r')
    for linea in archivo:
        linea=linea.rstrip("\n")
        lista=linea.split(" ")
        for palabra in lista:
            valida = True
            palabra = apareo(palabra,reemplazar)
            for caracter in palabra:
                if caracter.isalpha() == False:
                    valida = False
            if valida not in lista_valida and len(palabra)> long_palabra_min:
                lista_valida.append(palabra)
    archivo.close()
    reemplazar.close()
    return lista_valida

def cargaPalabrasTextosIniciales(lista_valida,numerotexto):
    archivo=open(numerotexto, "w")
    for palabra in lista_valida:
        archivo.write(palabra+"\n")

    archivo.close()

def funcion_datos_a_variables():
    configuraciones = open("configuracion.txt", "r")
    max_player = datosAVariables(configuraciones)
    long_palabra_min = datosAVariables(configuraciones)
    max_desaciertos = datosAVariables(configuraciones)
    puntos_aciertos = datosAVariables(configuraciones)
    puntos_desaciertos = datosAVariables(configuraciones)
    puntos_adivina = datosAVariables(configuraciones)
    configuraciones.close()
    return max_player,long_palabra_min,max_desaciertos,puntos_aciertos,puntos_desaciertos,puntos_adivina

def datosAVariables(configuraciones):
    linea = configuraciones.readline()
    nombre,valor = linea.split(" ")
    valor.strip('\n')
    valor = int(valor)
    return valor

def apareo(palabra,reemplazar):
    for linea in reemplazar:
        linea = linea.strip("\n")
        old,new = linea.split(",")
        if palabra.find(old) != -1:
            palabra = palabra.replace(old,new)
    reemplazar.seek(0)

    return palabra

def mezclarPalabras():
    palabras1 = open("palabras1.txt","r")
    palabras2 = open("palabras2.txt","r")
    palabras3 = open("palabras3.txt","r")
    palabrasMezcladas=open("palabrasMezcladas.txt", "w")
    listaPalabras = palabras1.readlines()
    listaPalabras2 = palabras2.readlines()
    listaPalabras3 = palabras3.readlines()
    for x in listaPalabras:
        x=x.strip('\n')
    for x in listaPalabras2:
        x=x.strip("\n")
        while x not in listaPalabras:
            listaPalabras.append(x)
    for x in listaPalabras3:
        x=x.strip("\n")
        while x not in listaPalabras:
            listaPalabras.append(x)
    listaPalabras.sort()
    palabrasMezcladas.write("".join(listaPalabras))
    palabras1.close()
    palabras2.close()
    palabras3.close()
    palabrasMezcladas.close()
    return palabrasMezcladas
