"""Esta libreria realiza operaciones entre matrices o vectores que estan compuestos
por numeros complejos,para hacer un buen uso de esta libreria es necesario
importar la anterios libreria hecha llamada CMPLEJOS"""
import COMPLEJOS as comp
import math
def matrizP(a,b):
    """Genera una matriz"""
    matri = []
    for i in range (a):
        m = []
        for j in range (b):
            m.append([])
        matri.append(m)
    return matri
def identidad(a):
    """Genera una matriz identidad hecha por numeros complejos"""
    matri = []
    for i in range(a):
        m = []
        for j in range(a):
            if i == j:
                m.append([1,0])
            else:
                m.append([0,0])
        matri.append(m)
    return matri
def sumamatriz(matriz1,matriz2):
    """Recibe dos matrices o vectores y los suma, estos deben tener
    el mismo tamaño """
    res = matrizP(len(matriz1),len(matriz1[0]))
    for i in range(len(matriz1)):
        for j in range(len(matriz1[0])):
            res[i][j] = comp.suma(matriz1[i][j],matriz2[i][j])
    return res
def restamatriz(matriz1,matriz2):
    """Recibe dos matrices o vectores y los resta, estos deben tener
    el mismo tamaño"""
    res = matrizP(len(matriz1),len(matriz1[0]))
    for i in range(len(matriz1)):
        for j in range(len(matriz1[0])):
            res[i][j] = comp.resta(matriz1[i][j],matriz2[i][j])
    return res

def multiplicarmatriz(matriz1,matriz2):
    """Esta funcion Multiplica dos matrices complejas, cada elemento de las matrices estan compuestos por numeros complejos """
    if len(matriz1[0]) == len(matriz2):
        res = matrizP(len(matriz1),len(matriz2[0]))
        for i in range(len(res)):
            for j in range(len(res[0])):
                res[i][j] = [0,0]
                for k in range(len(matriz2)):
                    res[i][j] = comp.suma(res[i][j],
                                comp.producto(matriz1[i][k],matriz2[k][j]))
        if len(res) == 1:
            return res[i][j]
        return res
    else:
        return 0

def mostrar(matriz):
    """Muestra la matriz en pantalla, en caso de no encontrar una,
    indica error"""
    if type(matriz) is list:
        for i in matriz:
            print(*i)
    else:
        print("Error. Las matrices no tienen el mismo tamaño")
    
def inversoadimatriz(matriz):
    """Recibe una matriz o un vector y halla el inverso aditiva de este"""
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = comp.inversoaditivo(matriz[i][j])
    return matriz

def multescalarmatriz(escalar,matriz):
    """Multiplicar un numero complejos (escalar) con una matriz o vector """
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = comp.escalarpornum(escalar,matriz[i][j])
    return matriz


def transpuesta(matriz):
    """Genera la transpuesta de un vector o matriz dado"""
    res = matrizP(len(matriz[0]),len(matriz))
    for i in range(len(matriz[0])):
        for j in range(len(matriz)):
            res[i][j] = matriz[j][i]

    return res
def conjugadamatriz(matriz):

    """Halla el conjugado de una matriz """    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = comp.conjugado(matriz[i][j])
    return matriz


def adjuntamatriz(matriz):
    """Halla la adjunta de una matriz calculando la transpuesta y luego
    la conjugada"""
    transpuest = transpuesta(matriz)
    conjugada = conjugadamatriz(transpuest)
    return transpuest

def productinterno(vector1,vector2):
    """Halla el producto interno de dos vectores compuesto de complejos"""
    daga = adjuntamatriz(vector1)
    res = multiplicarmatriz(daga,vector2)
    if res[1] == 0:
        return res[0]
    return res

def normavector(vector1):
    """Halla la norma de un vector compuesto de complejos"""
    res = productinterno(vector1,vector1)
    res = res ** 0.5
    return res

def distanciavectores(vector1,vector2):
    """Halla la distancia entre dos vectores compuesto de complejos"""
    resta = restamatriz(vector1,vector2)
    res = normavector(resta)
    return res

def matrizhermitiana(matriz1):
    """Comprueba si una matriz es hermitiana"""
    daga = adjuntamatriz(matriz1)
    if daga == matriz1:
        return True
    return False

def truncar(matriz):
    """Trunca los valores reales en la matriz, sean de la parte real o de la
    parte imaginaria"""
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            for k in range(2):
                matriz[i][j][k] = math.ceil(matriz[i][j][k])
    return matriz

def matrizunitaria(matriz):
    """Comprueba si una matriz es unitaria"""
    daga = adjuntamatriz(matriz)
    res = multiplicarmatriz(matriz,daga)
    res = truncar(res)
    identidadP = identidad(len(matriz))
    if res == identidadP:
        return True
    return False

def productotensorial(matriz1,matriz2):
    """Halla el producto rensorial de dos matrices compuestas de complejos"""
    res = matrizP(len(matriz1)*len(matriz2),len(matriz1[0])*len(matriz2[0]))
    m = len(matriz2)
    n = len(matriz2[0])
    for i in range(len(res)):
        for j in range(len(res[0])):
            res[i][j] = comp.producto(matriz1[i//m][j//n],matriz2[i%m][j%n])
    return res
