from tablero import Tablero
import time

PROFUNDIDADMAX = 1 #constante que marca la profundidad maxima del arbol de busqueda
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

def evaluarCuatro(tablero, casilla, i, j):
    valor = 0

    #VERTICAL
    if (i+3) <tablero.getAlto():
        if tablero.getCelda(i+1, j)==casilla and tablero.getCelda(i+2, j)==casilla and tablero.getCelda(i+3, j)==casilla:
            valor += 100

    #HORIZONTAL
    if (j+3) <tablero.getAncho():
        if tablero.getCelda(i, j+1)==casilla and tablero.getCelda(i, j+2)==casilla and tablero.getCelda(i, j+3)==casilla:
            valor += 100
            
    #DIAGONAL
    if (i+3) <tablero.getAlto():
        if (j-3) >= 0:
            if tablero.getCelda(i+1, j-1)==casilla and tablero.getCelda(i+2, j-2)==casilla and tablero.getCelda(i+3, j-3)==casilla:
                valor += 100
        if (j+3) <tablero.getAncho():
            if tablero.getCelda(i+1, j+1)==casilla and tablero.getCelda(i+2, j+2)==casilla and tablero.getCelda(i+3, j+3)==casilla:
                valor += 100
     
    return valor

def bloquearCuatro(tablero, casilla, i, j):
    valor = 0

    #VERTICAL
    if (i+3) <tablero.getAlto():
        if tablero.getCelda(i+1, j)!=casilla and tablero.getCelda(i+2, j)!=casilla and tablero.getCelda(i+3, j)!=casilla:
            valor += 150

    #HORIZONTAL
    if (j+3) <tablero.getAncho():
        if tablero.getCelda(i, j+1)!=casilla and tablero.getCelda(i, j+2)!=casilla and tablero.getCelda(i, j+3)!=casilla:
            valor += 150
            
    #DIAGONAL
    if (i+3) <tablero.getAlto():
        if (j-3) >= 0:
            if tablero.getCelda(i+1, j-1)!=casilla and tablero.getCelda(i+2, j-2)!=casilla and tablero.getCelda(i+3, j-3)!=casilla:
                valor += 150
        if (j+3) <tablero.getAncho():
            if tablero.getCelda(i+1, j+1)!=casilla and tablero.getCelda(i+2, j+2)!=casilla and tablero.getCelda(i+3, j+3)!=casilla:
                valor += 50
     
    return valor

def evaluarTres(tablero, casilla, i, j):
    valor = 0

    #VERTICAL
    if (i+2) <tablero.getAlto():
        if tablero.getCelda(i+1, j)==casilla and tablero.getCelda(i+2, j)==casilla:
            valor += 20

    #HORIZONTAL
    if (j+2) <tablero.getAncho():
        if tablero.getCelda(i, j+1)==casilla and tablero.getCelda(i, j+2)==casilla:
            valor += 20
            
    #DIAGONAL
    if (i+2) <tablero.getAlto():
        if (j-2) >= 0:
            if tablero.getCelda(i+1, j-1)==casilla and tablero.getCelda(i+2, j-2)==casilla:
                valor += 20
        if (j+2) <tablero.getAncho():
            if tablero.getCelda(i+1, j+1)==casilla and tablero.getCelda(i+2, j+2)==casilla:
                valor += 20
     
    return valor

def evaluarDos(tablero, casilla, i, j):
    valor = 0

    #VERTICAL
    if (i+1) <tablero.getAlto():
        if tablero.getCelda(i+1, j)==casilla:
            valor += 7

    #HORIZONTAL
    if (j+1) <tablero.getAncho():
        if tablero.getCelda(i, j+1)==casilla:
            valor += 7
            
    #DIAGONAL
    if (i+1) <tablero.getAlto():
        if (j-1) >= 0:
            if tablero.getCelda(i+1, j-1)==casilla:
                valor += 7
        if (j+1) <tablero.getAncho():
            if tablero.getCelda(i+1, j+1)==casilla:
                valor += 7
     
    return valor

def evaluacion(nodo):
    tablero = nodo.getTablero()
     
    valor = 0

    for i in range(tablero.getAlto()):
        for j in range(tablero.getAncho()):
            casilla=tablero.getCelda(i,j)
            if casilla!=0:
                if casilla == 2:
                    valor += evaluarCuatro(tablero, casilla, i, j)
                    valor += evaluarTres(tablero, casilla, i, j)
                    valor += evaluarDos(tablero, casilla, i, j)
                    valor += bloquearCuatro(tablero, casilla, i, j)
                else:
                    valor -= evaluarCuatro(tablero, casilla, i, j)
                    valor -= evaluarTres(tablero, casilla, i, j)
                    valor -= evaluarDos(tablero, casilla, i, j)
                    valor -= bloquearCuatro(tablero, casilla, i, j)

    print(tablero)
                
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

#Algoritmo minimax. Genera el arbol y devuelve maximos y minimos
def minimax(nodo, col):
    maxValor = -1000000
    minValor = 1000000
    columna = -1

    if(nodoHoja(nodo) == 1):
        if(columnaCompleta(nodo.getTablero(), col) == 0):
            valor = evaluacion(nodo)
            print("Valor HOJA:", valor, col)
            return valor, col
    else:
        for i in range(8):
            if(columnaCompleta(nodo.getTablero(), i) == 0):
                #MAXIMO
                if(nodo.getProfundidad()%2 == 0):
                    nodoHijo = crearEstado(nodo, i, 2)
                    valor, c = minimax(nodoHijo, i)
                    if(maxValor < valor):
                        maxValor = valor
                        columna = c
                #MINIMO
                else:
                    nodoHijo = crearEstado(nodo, i, 1)
                    valor, c = minimax(nodoHijo, i)
                    if(minValor > valor):
                        minValor = valor
                        columna = c
        
        if(nodo.getProfundidad()%2 == 0):
            print("PROFUNDIDAD", nodoHijo.getProfundidad(),":", maxValor, columna)
            return maxValor, columna
        else:
            print("PROFUNDIDAD", nodoHijo.getProfundidad(),":", minValor, columna)
            return minValor, columna

#inicio del algoritmo. Devuelve la columna donde colocar la ficha
def inicioAlgoritmo(nodoRaiz):
    columna = -1
    valor = 0
    maxValor = -100000

    if(nodoRaiz.getProfundidad() < PROFUNDIDADMAX):
        for i in range(8): #generamos el primer nivel de profundidad
            valor, col = minimax(nodoRaiz, i)
            if(maxValor < valor):
                maxValor = valor
                columna = col

    
    print("VALOR RAIZ: ", valor, columna)
    
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
    inicio = time.time()
    c = inicioAlgoritmo(nodoRaiz)
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
                