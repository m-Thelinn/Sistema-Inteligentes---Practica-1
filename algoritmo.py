from tablero import Tablero
import time
import math

PROFUNDIDADMAX = 4 #constante que marca la profundidad maxima del arbol de busqueda
pioridadesCentrales = {0:1,1:1,2:2,3:2,4:2,5:2,6:1,7:1} #las columnas tienen una serie de pioridades

class Nodo:
    def __init__(self, tablero, padre, profundidad):
        self.tablero = tablero #clase tablero
        self.padre = padre #clase nodo
        self.profundidad = profundidad #integer
    
    def getTablero(self):
        return self.tablero
    
    def getPadre(self):
        return self.padre

    def getProfundidad(self):
        return self.profundidad
    
    def setTablero(self, tablero):
        self.tablero = tablero
    
    def setPadre(self, padre):
        self.padre = padre

    def setProfundidad(self, profundidad):
        self.profundidad = profundidad

def puntuarTablero(tablero):
    valor = 0
    lista = []

    for i in range(tablero.getAlto()):
        for j in range(tablero.getAncho()):
            #VERTICAL
            if (i+3) <tablero.getAlto():
                lista = [tablero.getCelda(i, j), tablero.getCelda(i+1, j), tablero.getCelda(i+2, j), tablero.getCelda(i+3, j)]
                contIA = lista.count(2)
                contJ = lista.count(1)
                contVacio = lista.count(0)
                if(contIA > contJ):
                    if(contIA == 4):                            
                        valor += 100
                    elif(contIA == 3 and contVacio == 1):
                        valor += 20
                    elif(contIA == 3 and contJ == 1):
                        valor += 5                  
                elif contJ > contIA:
                    if(contJ == 4):
                        valor -= 100
                    elif(contJ == 3 and contVacio == 1):
                        valor -= 20                        
                    elif(contJ == 3 and contIA == 1):
                        valor -= 5
                                                
            #HORIZONTAL
            if (j+3) <tablero.getAncho():
                lista = [tablero.getCelda(i, j), tablero.getCelda(i, j+1), tablero.getCelda(i, j+2), tablero.getCelda(i, j+3)]                
                contIA = lista.count(2)
                contJ = lista.count(1)
                contVacio = lista.count(0)
                if(contIA > contJ):
                    if(contIA == 4):                            
                        valor += 100
                    elif(contIA == 3 and contVacio == 1):
                        valor += 20
                    elif(contIA == 3 and contJ == 1):
                        valor += 5                
                else:
                    if(contJ == 4):
                        valor -= 100
                    elif(contJ == 3 and contVacio == 1):
                        valor -= 20                        
                    elif(contJ == 3 and contIA == 1):
                        valor -= 5        
            #DIAGONAL
            if (i+3) <tablero.getAlto():
                if (j-3) >= 0:
                    lista = [tablero.getCelda(i, j), tablero.getCelda(i+1, j-1), tablero.getCelda(i+2, j-2), tablero.getCelda(i+3, j-3)]
                    contIA = lista.count(2)
                    contJ = lista.count(1)
                    contVacio = lista.count(0)
                    if(contIA > contJ):
                        if(contIA == 4):                            
                            valor += 100
                        elif(contIA == 3 and contVacio == 1):
                            valor += 30
                        elif(contIA == 3 and contJ == 1):
                            valor += 5
                    else:
                        if(contJ == 4):
                            valor -= 100
                        elif(contJ == 3 and contVacio == 1):
                            valor -= 30                        
                        elif(contJ == 3 and contIA == 1):
                            valor -= 5

                if (j+3) <tablero.getAncho():
                    lista = [tablero.getCelda(i, j), tablero.getCelda(i+1, j+1), tablero.getCelda(i+2, j+2), tablero.getCelda(i+3, j+3)]
                    contIA = lista.count(2)
                    contJ = lista.count(1)
                    contVacio = lista.count(0)
                    if(contIA > contJ):
                        if(contIA == 4):                            
                            valor += 100
                        elif(contIA == 3 and contVacio == 1):
                            valor += 30
                        elif(contIA == 3 and contJ == 1):
                            valor += 5
                    else:
                        if(contJ == 4):
                            valor -= 100
                        elif(contJ == 3 and contVacio == 1):
                            valor -= 30                        
                        elif(contJ == 3 and contIA == 1):
                            valor -= 5
    return valor

#def puntuarTablero(tablero, casilla):
#    valor = 0
#
#    for i in range(tablero.getAlto()):
#        for j in range(tablero.getAncho()):
#            #VERTICAL
#            if (i+3) <tablero.getAlto():
#                if tablero.getCelda(i, j)==casilla and tablero.getCelda(i+1, j)==casilla and tablero.getCelda(i+2, j)==casilla and tablero.getCelda(i+3, j)==casilla:
#                    valor += 100
#                if tablero.getCelda(i, j)==casilla and tablero.getCelda(i+1, j)==casilla and tablero.getCelda(i+2, j)==casilla:
#                    valor += 15
#                if tablero.getCelda(i, j)==casilla and tablero.getCelda(i+1, j)==casilla:
#                    valor += 5
#            #HORIZONTAL
#            if (j+3) <tablero.getAncho():
#                if tablero.getCelda(i, j)==casilla and tablero.getCelda(i, j+1)==casilla and tablero.getCelda(i, j+2)==casilla and tablero.getCelda(i, j+3)==casilla:
#                    valor += 100
#                if tablero.getCelda(i, j)==casilla and tablero.getCelda(i, j+1)==casilla and tablero.getCelda(i, j+2)==casilla:
#                    valor += 15
#                if tablero.getCelda(i, j)==casilla and tablero.getCelda(i, j+1)==casilla:
#                    valor += 5
#                    
#            #DIAGONAL
#            if (i+3) <tablero.getAlto():
#                if (j-3) >= 0:
#                    if tablero.getCelda(i, j) and tablero.getCelda(i+1, j-1)==casilla and tablero.getCelda(i+2, j-2)==casilla and tablero.getCelda(i+3, j-3)==casilla:
#                        valor += 100
#                    if tablero.getCelda(i, j) and tablero.getCelda(i+1, j-1)==casilla and tablero.getCelda(i+2, j-2)==casilla:
#                        valor += 15
#                    if tablero.getCelda(i, j) and tablero.getCelda(i+1, j-1)==casilla:
#                        valor += 5
#                if (j+3) <tablero.getAncho():
#                    if tablero.getCelda(i, j) and tablero.getCelda(i+1, j+1)==casilla and tablero.getCelda(i+2, j+2)==casilla and tablero.getCelda(i+3, j+3)==casilla:
#                        valor += 100
#                    if tablero.getCelda(i, j) and tablero.getCelda(i+1, j+1)==casilla and tablero.getCelda(i+2, j+2)==casilla:
#                        valor += 15
#                    if tablero.getCelda(i, j) and tablero.getCelda(i+1, j+1)==casilla:
#                        valor += 5
#            
#    return valor

def evaluacion(nodo):
    tablero = nodo.getTablero()
    print(tablero)

    if tablero.cuatroEnRaya() == 2:
        return math.inf
    elif tablero.cuatroEnRaya() == 1:
        return -math.inf
    else:
        return puntuarTablero(tablero)
                
#verifica que una columna no esta completa
def columnaCompleta(tablero, col):
    if tablero.getCelda(0, col) != 0:
        return True #completa
    else:
        return False #no completa

#devuelve 1 en caso de ser nodo hoja. Devuelve 0 si no lo es
def nodoHoja(nodo):
    if nodo.getProfundidad() >= PROFUNDIDADMAX:
        return True
    else:
        return False
    
#coloca una nueva ficha en la columna marcada.
def colocarNuevaFicha(tablero, columna, jugador):
    fila = busca(tablero, columna)
    tablero.setCelda(fila, columna, jugador)

#crear un nuevo estado con la casilla del tablero llena para posteriormente evaluarla.
def crearEstado(nodoPadre, i, jugador):
    tableroHijo = Tablero(nodoPadre.getTablero())
    colocarNuevaFicha(tableroHijo, i, jugador)
    nodoHijo = Nodo(tableroHijo, nodoPadre, nodoPadre.getProfundidad() + 1)

    return nodoHijo

#devuelve el valor minimo de una serie de hijos. Coloca ficha de jugador
def minimo(nodoPadre, alpha, beta):
    minValor = math.inf
    poda = False

    if(nodoHoja(nodoPadre) == True):
        return evaluacion(nodoPadre)
    else:
        for i in range(8):
            if poda == True:
                print('PODA')
                break
            if(columnaCompleta(nodoPadre.getTablero(), i) == False):
                nodoHijo = crearEstado(nodoPadre, i, 1)
                valor = maximo(nodoHijo, alpha, beta)
                if minValor > valor:
                    minValor = valor
                if valor < beta:
                    beta = valor
                if beta <= alpha:
                    poda = True

    print("Valor MIN profundidad", nodoPadre.getProfundidad() + 1,  ":", valor)
    return minValor

#devuelve el valor maximo de una serie de hijos. Coloca ficha de maquina
def maximo(nodoPadre, alpha, beta):
    maxValor = -math.inf
    poda = False

    if(nodoHoja(nodoPadre) == True):
        return evaluacion(nodoPadre)
    else:
        for i in range(8):
            if poda == True:
                print('PODA')
                break
            if(columnaCompleta(nodoPadre.getTablero(), i) == False):
                nodoHijo = crearEstado(nodoPadre, i, 2)
                valor = minimo(nodoHijo, alpha, beta)
                if maxValor < valor:
                    maxValor = valor
                if valor > alpha:
                    alpha = valor
                if beta <= alpha:
                    poda = True
                    
    print("Valor MAX profundidad", nodoPadre.getProfundidad() + 1,  ":", valor)
    return maxValor

#inicio del algoritmo. Devuelve la columna donde colocar la ficha
def minimax(nodoRaiz, alpha, beta):
    valor = 0
    maxValor = -math.inf
    columna = -1
    poda = False

    if(PROFUNDIDADMAX == 0):
        print("ERROR: NO SE ADMITE PROFUNDIDAD 0")
        quit()
 
    for i in range(8):
        if poda == True:
            print('PODA')
            break
        else:
            nodoHijo = crearEstado(nodoRaiz, i, 2)
            valor = minimo(nodoHijo, alpha, beta)
            if maxValor < valor:
                maxValor = valor
                columna = i
            if valor > alpha:
                alpha = valor
            if beta <= alpha:
                poda = True

    print("Valor final/columna: ", valor, ",", columna)
    return columna
    
# busca que fila es la primera vacia de una columna concreta
def busca(tablero, col):  
    if tablero.getCelda(0,col) != 0:
        i=-1
    i=0
    while i<tablero.getAlto() and tablero.getCelda(i,col)==0:          
        i=i+1      
    i=i-1
   
    return i

# llama al algoritmo que decide la jugada
def juega(tablero, posicion):
    encontrado = False
    nodoRaiz = Nodo(tablero, None, 0)

    inicio = time.time()
    c = minimax(nodoRaiz, -math.inf, math.inf)
    final = time.time()
    print("TIEMPO:", final - inicio)

    while not encontrado and c < tablero.getAncho():
        f = busca(tablero, c)
        if f != -1:
            encontrado = True
        else:
            c = c + 1
    
    if f != -1:
        posicion[0] = f
        posicion[1] = c
                