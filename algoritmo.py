import math
from tablero import Tablero

PROFUNDIDADMAX = 3 #constante que marca la profundidad maxima del arbol de busqueda
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

#evalua que existen dos fichas en linea horizontal
def dosEnLineaH(tablero):
    i = 0
    valor = 0
    fin = False
      
    while not fin and i < tablero.getAlto():
        j = 0
        while not fin and j < tablero.getAncho():
            casilla = tablero.getCelda(i,j)
            if casilla != 0:
                if (j+3) < tablero.getAncho():
                    if tablero.getCelda(i, j+1) == casilla:
                        valor = 5
                        fin = True
    
    return valor

#evalua que existen tres fichas en linea horizontal
def tresEnLineaH(tablero):
    i = 0
    valor = 0       
    fin = False
      
    while not fin and i < tablero.getAlto():
        j = 0
        while not fin and j < tablero.getAncho():
            casilla = tablero.getCelda(i,j)
            if casilla != 0:
                if (j+3) < tablero.getAncho():
                    if tablero.getCelda(i, j+1) == casilla and tablero.getCelda(i, j+2) == casilla:
                        valor = 10
                        fin = True
    
    return valor

#evalua que existen dos fichas en linea vertical
def dosEnLineaV(tablero):
    i = 0
    valor = 0       
    fin = False
      
    while not fin and i < tablero.getAlto():
        j = 0
        while not fin and j < tablero.getAncho():
            casilla = tablero.getCelda(i,j)
            if casilla != 0:
                if (i+3) < tablero.getAlto():
                    if tablero.getCelda(i+1, j) == casilla:
                        valor = 5
                        fin = True
    
    return valor

#evalua que existen tres fichas en linea vertical
def tresEnLineaV(tablero):
    i = 0
    valor = 0       
    fin = False
      
    while not fin and i < tablero.getAlto():
        j = 0
        while not fin and j < tablero.getAncho():
            casilla = tablero.getCelda(i,j)
            if casilla != 0:
                if (i+3) < tablero.getAlto():
                    if tablero.getCelda(i+1, j) == casilla and tablero.getCelda(i+2, j) == casilla:
                        valor = 10
                        fin = True
    
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
    return 0

#coloca una nueva ficha en la columna marcada. ERROR, LO HACE EN EL TABLERO PADRE E HIJO
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
def minimo(nodoPadre):
    minValor = math.inf
    columna = -1

    for i in range(8):
        if(columnaCompleta(nodoPadre.getTablero(), i) == 0):
            nodoHijo = crearEstado(nodoPadre, i, 1)
            if(nodoHoja(nodoHijo) == 1):
                valor = evaluacion(nodoHijo) + pioridadesTablero[i]
                if(minValor > valor):
                    minValor = valor
                    columna = i
            else:
                valor, col = maximo(nodoHijo)
                if(minValor > valor):
                    minValor = valor
                    columna = col
    
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
                if(maxValor < valor):
                    maxValor = valor
                    columna = i
            else:
                valor, col = minimo(nodoHijo)
                if(maxValor < valor):
                    maxValor = valor
                    columna = col

    return maxValor, columna

#inicio del algoritmo. Devuelve la columna donde colocar la ficha
def minimax(nodo):
    maxValor = 0
    columna = -1

    valor, col = maximo(nodo)
    if(maxValor < valor):
        maxValor = valor
        columna = col
    
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
                