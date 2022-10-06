from copy import deepcopy
import math
from wsgiref.validate import validator
from tablero import Tablero

PROFUNDIDADMAX = 4 #constante que marca la profundidad maxima del arbol de busqueda
pioridadesTablero = [1,2,3,4,4,3,2,1] #las columnas tienen una serie de pioridades

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


def verificar(tablero):
    i=0        
    valor = 0

    while i<tablero.getAlto():
        j=0
        while j<tablero.getAncho():
            casilla=tablero.getCelda(i,j)
            if casilla!=0:
                ################################
                # BUSCAR CUATRO EN RAYA
                ################################

                #búsqueda en horizontal
                if (j+3) <tablero.getAncho():
                    if tablero.getCelda(i, j+1)==casilla and tablero.getCelda(i, j+2)==casilla and tablero.getCelda(i, j+3)==casilla:
                        if(casilla==1):
                            valor += -50
                        else:
                            valor += 50
                    else:
                        if(casilla==1):
                            valor += -50
                        else:
                            valor += 50
                #búsqueda en vertical
                if (i+3) <tablero.getAlto():
                    if tablero.getCelda(i+1, j)==casilla and tablero.getCelda(i+2, j)==casilla and tablero.getCelda(i+3, j)==casilla:
                        if(casilla==1):
                            valor += -50
                        else:
                            valor += 50
                    else:
                        if(casilla==1):
                            valor += -50
                        else:
                            valor += 50

                #búsqueda en diagonal
                if (i+3) <tablero.getAlto():
                    if (j-3) >= 0:
                        if tablero.getCelda(i+1, j-1)==casilla and tablero.getCelda(i+2, j-2)==casilla and tablero.getCelda(i+3, j-3)==casilla:
                            if(casilla==1):
                                valor += -50
                            else:
                                valor += 50
                        else:
                            if(casilla==1):
                                valor += -50
                            else:
                                valor += 50
                    if (j+3) <tablero.getAncho():
                        if tablero.getCelda(i+1, j+1)==casilla and tablero.getCelda(i+2, j+2)==casilla and tablero.getCelda(i+3, j+3)==casilla:
                            if(casilla==1):
                                valor += -50
                            else:
                                valor += 50
                        else:
                            if(casilla==1):
                                valor += 50
                            else:
                                valor += -50
                ################################
                # BUSCAR TRES EN RAYA
                ################################
                
                #búsqueda en horizontal
                if (j+2) <tablero.getAncho():
                    if tablero.getCelda(i, j+1)==casilla and tablero.getCelda(i, j+2)==casilla:
                        if(casilla==1):
                            valor += -15
                        else:
                            valor += 15
                #búsqueda en vertical
                if (i+2) <tablero.getAlto():
                    if tablero.getCelda(i+1, j)==casilla and tablero.getCelda(i+2, j)==casilla:
                        if(casilla==1):
                            valor += -15
                        else:
                            valor += 15
                #búsqueda en diagonal
                if (i+2) <tablero.getAlto():
                    if (j-2) >= 0:
                        if tablero.getCelda(i+1, j-1)==casilla and tablero.getCelda(i+2, j-2)==casilla:
                            if(casilla==1):
                                valor += -15
                            else:
                                valor += 15
                    if (j+2) <tablero.getAncho():
                        if tablero.getCelda(i+1, j+1)==casilla and tablero.getCelda(i+2, j+2)==casilla:
                            if(casilla==1):
                                valor += -15
                            else:
                                valor += 15
                
                ################################
                # BUSCAR DOS EN RAYA
                ################################
                
                #búsqueda en horizontal
                if (j+1) <tablero.getAncho():
                    if tablero.getCelda(i, j+1)==casilla:
                        if(casilla==1):
                            valor += -5
                        else:
                            valor += 5
                #búsqueda en vertical
                if (i+1) <tablero.getAlto():
                    if tablero.getCelda(i+1, j)==casilla:
                        if(casilla==1):
                            valor += -5
                        else:
                            valor += 5
                #búsqueda en diagonal
                if (i+1) <tablero.getAlto():
                    if (j-1) >= 0:
                        if tablero.getCelda(i+1, j-1)==casilla:
                            if(casilla==1):
                                valor += -5
                            else:
                                valor += 5
                    if (j+1) <tablero.getAncho():
                        if tablero.getCelda(i+1, j+1)==casilla:
                            if(casilla==1):
                                valor += -5
                            else:
                                valor += 5
            j=j+1
        i=i+1

    return valor
#verifica que una columna no esta completa
def columnaCompleta(tablero, col):
    if tablero.getCelda(0, col) != 0:
        return 1 #completa
    else:
        return 0 #no completa

#devuelve 1 en caso de ser nodo hoja. Devuelve 0 si no lo es
def nodoHoja(nodo):
    if nodo.getProfundidad() >= PROFUNDIDADMAX:
        return 1
    else:
        return 0
    
#evalua el estado del tablero y devuelve un numero para el estado
def evaluacion(nodo):
    tablero = nodo.getTablero()

    valor = verificar(tablero)
    print(tablero)

    return valor

#coloca una nueva ficha en la columna marcada. ERROR, LO HACE EN EL TABLERO PADRE E HIJO
def colocarNuevaFicha(tablero, columna, jugador):
    fila = busca(tablero, columna)
    tablero.setCelda(fila, columna, jugador)

#crear un nuevo estado con la casilla del tablero llena para posteriormente evaluarla.
def crearEstado(nodoPadre, i, jugador):
    tableroHijo = deepcopy(nodoPadre.getTablero())
    colocarNuevaFicha(tableroHijo, i, jugador)
    nodoHijo = Nodo(tableroHijo, nodoPadre, nodoPadre.getProfundidad() + 1)

    return nodoHijo

#devuelve el valor minimo de una serie de hijos. Coloca ficha de jugador
def minimo(nodoPadre):
    minValor = math.inf
    columna = -1

    for i in range(8):
        if(columnaCompleta(nodoPadre.getTablero(), i) == 0):
            nodoHijo = crearEstado(nodoPadre, i, 1)
            if(nodoHoja(nodoHijo) == 1):
                valor = evaluacion(nodoHijo) + pioridadesTablero[i]
                print("Valor MIN HOJA ", i, ": ", valor)
                if(minValor > valor):
                    minValor = valor
                    columna = i
            else:
                valor, col = maximo(nodoHijo)
                if(minValor > valor):
                    minValor = valor
                    columna = col
    
    print("MINIMO PROF:", nodoHijo.getProfundidad(), minValor, columna)
    print("============================================================")
    return minValor, columna

#devuelve el valor maximo de una serie de hijos. Coloca ficha de maquina
def maximo(nodoPadre):
    maxValor = -math.inf
    columna = -1

    for i in range(8):
        if(columnaCompleta(nodoPadre.getTablero(), i) == 0):
            nodoHijo = crearEstado(nodoPadre, i, 2)
            if(nodoHoja(nodoHijo) == 1):
                valor = evaluacion(nodoHijo) + pioridadesTablero[i]
                print("Valor MAX HOJA ", i, ": ", valor)
                if(maxValor < valor):
                    maxValor = valor
                    columna = i
            else:
                valor, col = minimo(nodoHijo)
                if(maxValor < valor):
                    maxValor = valor
                    columna = col

    print("MAXIMO PROF:", nodoHijo.getProfundidad(), maxValor, columna)
    print("============================================================")
    return maxValor, columna

#inicio del algoritmo. Devuelve la columna donde colocar la ficha
def minimax(nodo):
    columna = -1

    valor, columna = maximo(nodo)

    print("FINAL: ", valor, columna)
    
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
    #nodoRaiz.getTablero().setCelda(5, 0, 1)
    #nodoRaiz.getTablero().setCelda(4, 0, 1)
    c = minimax(nodoRaiz)

    while not encontrado and c < tablero.getAncho():
        f = busca(tablero, c)
        if f != -1:
            encontrado = True
        else:
            c = c + 1
    if f != -1:
        posicion[0] = f
        posicion[1] = c
                