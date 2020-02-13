import VECTORESYMATRICES as vm
def test_suma():
    m1 = [[[8,3]],[[-1,-4]],[[0,-9]]]
    m2 = [[[8,-3]],[[2,5]],[[3,0]]]
    assert vm.sumamatriz(m1,m2) == [[[16, 0]], [[1, 1]], [[3, -9]]],'El resultado no es el correcto'

def test_inversoaditivo():
    m3 = [[[-5,2]],[[3,0]],[[0,-1]]]
    assert vm.inversoadimatriz(m3) == [[[5, -2]], [[-3, 0]], [[0, 1]]],'El resultado no es el correcto'

def test_multescalarmatriz():
    m4 = [[[-2,5]],[[-1,-1]],[[2,-9]]]
    assert vm.multescalarmatriz([-1,1],m4) == [[[-3, -7]], [[2, 0]], [[7, 11]]],'El resultado no es el correcto'

def test_suma1():
    m5 = [[[-8,-3],[-6,-4],[0,-4]],[[-1,8],[6,-10],[8,-5]],[[4,0],[8,5],[-7,-9]]]
    m6 = [[[-7,-2],[-4,-2],[7,7]],[[5,9],[0,3],[6,-5]],[[1,5],[-6,-6],[5,8]]]
    assert vm.sumamatriz(m5,m6) == [[[-15, -5], [-10, -6], [7, 3]], [[4, 17], [6, -7], [14, -10]], [[5, 5], [2, -1], [-2, -1]]],'El resultado no es el correcto'

def test_inversoaditivo1():
    m7 = [[[7,3],[-1,7]],[[-9,-4],[-7,-9]]]
    assert vm.inversoadimatriz(m7) == [[[-7, -3], [1, -7]], [[9, 4], [7, 9]]],'El resultado no es el correcto'

def test_multescalarmatriz1():
    m8 = [[[3,-2],[8,-4]],[[4,-10],[-2,-8]]]
    assert vm.multescalarmatriz([-2,3],m8) == [[[0, 13], [-4, 32]], [[22, 32], [28, 10]]],'El resultado no es el correcto'

def test_transpuesta():
    m9 = [[[5,9],[-7,-5]],[[8,2],[-3,-7]]]
    assert vm.transpuesta(m9) == [[[5, 9], [8, 2]], [[-7, -5], [-3, -7]]],'El resultado no es el correcto'

def test_conjugadamatriz():
    m10 = [[[-6,1],[3,8]],[[2,-6],[3,0]]]
    assert vm.conjugadamatriz(m10) == [[(-6, -1), (3, -8)], [(2, 6), (3, 0)]],'El resultado no es el correcto'

def test_adjunta():
    m11 = [[[7,7],[3,8],[8,4]],[[5,0],[8,-6],[-10,-1]]]
    assert vm.adjuntamatriz(m11) == [[(7, -7), (5, 0)], [(3, -8), (8, 6)], [(8, -4), (-10, 1)]],'El resultado no es el correcto'
    
def test_multiplicarmatriz():
    m12 = [[[-6,2],[0,6],[7,2]],[[6,9],[7,7],[-6,-6]],[[5,8],[-6,8],[6,9]]]
    m13 = [[[9,-6],[-3,-4],[5,-2]],[[3,6],[-1,-5],[0,-5]],[[9,9],[8,-4],[-8,-4]]]
    assert vm.multiplicarmatriz(m12,m13) == [[[-33, 153], [120, 0], [-44, -22]], [[87, 0], [-26, -117], [107, 70]], [[0, 165], [147, 26], [69, -36]]],'El resultado no es el correcto'

def test_multiplicarmatriz1():
    m131 = [[[2,1],[3,0],[1,-1]],[[0,0],[0,-2],[7,-3]],[[3,0],[0,0],[1,-2]]]
    m132 = [[[0,-1],[1,0]],[[0,0],[0,1]]]
    assert  vm.multiplicarmatriz(m131,m132) == 0,'El resultado no es el correcto'

def test_multiplicarmatriz2():
    m14 = [[[-1,5],[1,-7],[-6,3]],[[-3,-9],[2,-5],[1,-10]],[[-6,5],[6,-5],[3,-2]]]
    v1 = [[[1,-3]],[[4,3]],[[-3,1]]]
    assert vm.multiplicarmatriz(m14,v1) == [[[54, -32]], [[0, 17]], [[41, 30]]],'El resultado no es el correcto'

def test_productointerno():
    v2 = [[[2,-1]],[[-8,-5]],[[-2,-6]]]
    v3 = [[[6,-3]],[[5,-1]],[[-6,-2]]]
    assert vm.productinterno(v2,v3) == [4, 1],'El resultado no es el correcto'

def test_normavector():
    v4 = [[[4,5]],[[3,1]],[[0,-7]]]
    assert int(vm.normavector(v4))  == 10, 'El resultado no es el correcto'

def test_distancia():
    v5 = [[[2,7]],[[4,-1]],[[2,-4]]]
    v6 = [[[7,8]],[[2,-8]],[[1,4]]]
    assert int(vm.distanciavectores(v5,v6)) == 12, 'El resultado no es el correcto'

def test_distancia1():
    v7 = [[[9,-7]],[[-1,-6]]]
    v8 = [[[7,-8]],[[5,-9]]]
    assert round(vm.distanciavectores(v7,v8),2) == 7.07,'El resultado no es el correcto'
    
def test_unitaria():
    m15 = [[[(1/(2**0.5)),0],[0,(1/(2**0.5))]],[[0,(1/(2**0.5))],[(1/(2**0.5)),0]]]
    assert vm.matrizunitaria(m15) == True, 'El resultado no es el correcto'



def test_hermitiana():
    m17 = [[[3,0],[2,-1],[0,-3]],[[2,1],[0,0],[1,-1]],[[0,3],[1,1],[0,0]]]
    assert vm.matrizhermitiana(m17) == False, 'El resultado no es el correcto'

def test_hermitiana1():
    m18 = [[[1,0],[3,-1]],[[3,1],[0,1]]]
    assert vm.matrizhermitiana(m18) == False, 'El resultado no es el correcto'

def test_productotensorial():
    m19 = [[[1,1],[0,0]],[[1,0],[0,1]]]
    m20 = [[[-1,2],[-2,-2],[0,2]],[[2,3],[3,1],[2,2]],[[-2,1],[1,-1],[2,1]]]
    assert vm.productotensorial(m19,m20) == [[[-3, 1], [0, -4], [-2, 2], [0, 0], [0, 0], [0, 0]], [[-1, 5], [2, 4], [0, 4], [0, 0], [0, 0], [0, 0]], [[-3, -1], [2, 0], [1, 3], [0, 0], [0, 0], [0, 0]], [[-1, 2], [-2, -2], [0, 2], [-2, -1], [2, -2], [-2, 0]], [[2, 3], [3, 1], [2, 2], [-3, 2], [-1, 3], [-2, 2]], [[-2, 1], [1, -1], [2, 1], [-1, -2], [1, 1], [-1, 2]]],'El resultado no es el correcto'       
    
    

if __name__ == "__main__":
    test_suma()
    test_inversoaditivo()
    test_multescalarmatriz()
    test_suma1()
    test_inversoaditivo()
    test_inversoaditivo1()
    test_multescalarmatriz1()
    test_transpuesta()
    test_conjugadamatriz()
    test_adjunta()
    test_multiplicarmatriz()
    test_multiplicarmatriz1()
    test_multiplicarmatriz2()
    test_productointerno()
    test_normavector()
    test_distancia()
    test_distancia1()
    test_unitaria()
    test_unitaria1()
    test_hermitiana()
    test_hermitiana1()
    test_productotensorial()
    
    print("Prueba exitosa")
