import unittest
import calculadoraCom

class testCalculadora(unittest.TestCase):
    def test_sumaComplejos(self):
        self.assertEqual(calculadoraCom.suma([2,3.4],[3,-4.5]),([5.0, -1.1]))
    def test_sumaComplejos2(self):
        self.assertEqual(calculadoraCom.suma([4,5],[4,6]),([8.0, 11.0]))

    def test_restaComplejos(self):
        self.assertEqual(calculadoraCom.resta([3,-2],[4,6]),([-1.0, -8.0]))
    def test_restaComplejos2(self):    
        self.assertEqual(calculadoraCom.resta([3,2],[5,-6]),([-2.0, 8.0]))

    def test_multiplicacionComplejos(self):
        self.assertEqual(calculadoraCom.multiplicar([2,3],[4,5]),([-7, 22]))
    def test_multiplicacionComplejos2(self):
        self.assertEqual(calculadoraCom.multiplicar([2,1],[2,-3]),([7, -4]))
    
    def test_divisionComplejos(self):
        self.assertEqual(calculadoraCom.dividir([3,2],[-1,2]),([0.2, -1.6]))
    def test_divisionComplejos3(self):
        self.assertEqual(calculadoraCom.dividir([1,-4],[3,1]),([-0.1, -1.3]))
    
    def test_moduloComplejos(self):
        self.assertEqual(calculadoraCom.modulo([3,5]),(5.831))
    def test_moduloComplejos2(self):
        self.assertEqual(calculadoraCom.modulo([6,2]),(6.325))

    def test_conjugadoComplejos(self):
        self.assertEqual(calculadoraCom.conjugado([3,5]),([3, -5]))
    def test_conjugadoComplejos2(self):
        self.assertEqual(calculadoraCom.conjugado([6,2]),([6, -2]))

    def test_convertorComplejos(self):
        self.assertEqual(calculadoraCom.convertor([4,-5]),([6.403, -51.34]))
    def test_convertorComplejos2(self):
        self.assertEqual(calculadoraCom.convertor([8,12]),([14.422, 56.31]))

    def test_faseComplejos(self):
        self.assertEqual(calculadoraCom.fase([8,12]),(0.983))
    def test_faseComplejos2(self):
        self.assertEqual(calculadoraCom.fase([9,-15]),(-1.03))

    def test_adicionVectores(self):
        self.assertEqual(calculadoraCom.adicionVectores([[1,-5], [-2,10], [50,-90]],[[43,10], [4,10], [0,-5]]),([[44, 5], [2, 20], [50, -95]]))
    def test_adicionVectores2(self):
        self.assertEqual(calculadoraCom.adicionVectores([[-34,5], [54,10], [5,-9]],[[-3,17], [-42,10], [50,-50]]),([[-37, 22], [12, 20], [55, -59]]))

    def test_inversaVectores(self):
        self.assertEqual(calculadoraCom.inversaVectores([[-5,-15], [8,10], [5,-9]]),([[5, 15], [-8, -10], [-5, 9]]))
    def test_inversaVectores2(self):
        self.assertEqual(calculadoraCom.inversaVectores([[-6,-7], [-4,-10], [50,-50]]),([[6,7], [4,10], [-50,50]]))

    def test_multiplicacionEscalar(self):
        self.assertEqual(calculadoraCom.multiplicacionEscalar([2,5], [[53,-1], [8,0], [7,-3]]),([[111, 263], [16, 40], [29, 29]]))
    def test_multiplicacionEscalar2(self):
        self.assertEqual(calculadoraCom.multiplicacionEscalar([-3,-8], [[-66,0], [34,10], [32,-5]]),([[198, 528], [-22, -302], [-136, -241]]))

    def test_transVector(self):
        self.assertEqual(calculadoraCom.transVector([[23,0], [6,23], [4,-6]]),([[[23, 0]], [[6, 23]], [[4, -6]]]))
    def test_transVector2(self):
        self.assertEqual(calculadoraCom.transVector([[64,7], [76,8], [-23,54]]),([[[64, 7]], [[76, 8]], [[-23, 54]]]))

    def test_tensorVector(self):
        self.assertEqual(calculadoraCom.tensorVector([[2,1], [0,-3]],[[4,7], [-6,8], [-3,5]]),([[1, 18], [-20, 10], [-11, 7], [21, -12], [24, 18], [15, 9]]))
    def test_tensorVector2(self):
        self.assertEqual(calculadoraCom.tensorVector([[0,-1], [-10,1], [0,-6]],[[-2,2], [5,10]]),([[2, 2], [10, -5], [18, -22], [-60, -95], [12, 12], [60, -30]]))

    def test_conjugadoVector(self):
        self.assertEqual(calculadoraCom.conjugadoVector([[7, 7], [3, 8], [0, -8]]),([[7, -7], [3, -8], [0, 8]]))
    def test_conjugadoVector2(self):
        self.assertEqual(calculadoraCom.conjugadoVector([[3, 4], [6, -1], [-1, -3]]),([[3, -4], [6, 1], [-1, 3]]))

    def test_prodInternoVector(self):
        self.assertEqual(calculadoraCom.prodInternoVector([[7, 1], [1, 6], [-6, -8]],[[0, -6], [-5, -5], [5, -9]]),([1, 77]))
    def test_prodInternoVector2(self):
        self.assertEqual(calculadoraCom.prodInternoVector([[-10, 6], [7, -6], [-3, 7]],[[8, 3], [-6, -5], [-5, 1]]),([-52, -117]))
        
    def test_normaVector(self):
        self.assertEqual(calculadoraCom.normaVector([[-6, -3], [6, 6], [-4, -9]]),(14.629))
    def test_normaVector2(self):
        self.assertEqual(calculadoraCom.normaVector([[-1, -4], [8, -1], [-5, -9]]),(13.711))

    def test_distanciaVector(self):
        self.assertEqual(calculadoraCom.distanciaVector([[6, 4], [5, 4], [-2, 6]],[[8, -8], [0, -10], [-1, -7]]),(23.216))
    def test_distanciaVector2(self):
        self.assertEqual(calculadoraCom.distanciaVector([[1, 5], [5, 1], [-8, 8]],[[6, -7], [-1, 2], [-1, -2]]),(18.841))

    def test_adicionMatrices(self):
        self.assertEqual(calculadoraCom.adicionMatrices([[[4, 5], [-1, 8], [3, 1]], [[6, -4], [0, 7], [-2, -9]], [[-1, -6], [0, -3], [0, -5]]],[[[8, 8], [9, -6], [-8, 4]], [[-4, 3], [2, 4], [-4, 3]], [[-6, -10], [8, -6], [4, 1]]]),([[[12, 13], [8, 2], [-5, 5]], [[2, -1], [2, 11], [-6, -6]], [[-7, -16], [8, -9], [4, -4]]]))
    def test_adicionMatrices2(self):
        self.assertEqual(calculadoraCom.adicionMatrices([[[-2, 2], [5, -3], [-7, -9]], [[-1, 6], [-9, -9], [-9, -6]], [[8, 2], [7, -3], [1, -6]]],[[[5, 2], [6, -9], [-1, 2]], [[9, -2], [9, -10], [-6, 6]], [[8, -6], [-4, -4], [0, 7]]]),([[[3, 4], [11, -12], [-8, -7]], [[8, 4], [0, -19], [-15, 0]], [[16, -4], [3, -7], [1, 1]]]))

    def test_inversaMatrices(self):
        self.assertEqual(calculadoraCom.inversaMatrices([[[9, 9], [8, 9]], [[9, 4], [-10, 2]]]),([[[-9, -9], [-8, -9]], [[-9, -4], [10, -2]]]))
    def test_inversaMatrices2(self):
        self.assertEqual(calculadoraCom.inversaMatrices([[[-4, 6], [0, -6]], [[-2, 9], [3, 5]]]),([[[4, -6], [0, 6]], [[2, -9], [-3, -5]]]))

    def test_multiplicacion_escalar_matriz(self):
        self.assertEqual(calculadoraCom.multiplicacion_escalar_matriz([4,-6],[[[-7, 4], [-10, -1]], [[-2, -7], [1, -9]]]),([[[-4, 58], [-46, 56]], [[-50, -16], [-50, -42]]]))
    def test_multiplicacion_escalar_matriz2(self):
        self.assertEqual(calculadoraCom.multiplicacion_escalar_matriz([-2,9],[[[-10, 3], [-3, -1]], [[6, -3], [-5, -1]]]),([[[-7, -96], [15, -25]], [[15, 60], [19, -43]]]))

    def test_matTranspuesta(self):
        self.assertEqual(calculadoraCom.matTranspuesta([[[7, -9], [3, -4]], [[-1, 9], [5, -2]]]),([[[7, -9], [-1, 9]], [[3, -4], [5, -2]]]))
    def test_matTranspuesta2(self):
        self.assertEqual(calculadoraCom.matTranspuesta([[[-2, -8], [2, 8]], [[-6, -5], [4, -9]]]),([[[-2, -8], [-6, -5]], [[2, 8], [4, -9]]]))

    def test_matrizProducto(self):
        self.assertEqual(calculadoraCom.matrizProducto([[[-4, -3], [3, -7]], [[-1, -4], [3, -10]]],[[[7, -2], [-10, 5]], [[7, -7], [-3, -2]]]),([[[-62, -83], [32, 25]], [[-64, -117], [1, 59]]]))
    def test_matrizProducto2(self):
        self.assertEqual(calculadoraCom.matrizProducto([[[-10, -7], [-4, -7]], [[6, -7], [-8, -1]]],[[[1, -2], [-9, 1]], [[4, 1], [-1, 7]]]),([[[-33, -19], [150, 32]], [[-39, -31], [-32, 14]]]))

    def test_conjugadaMatriz(self):
        self.assertEqual(calculadoraCom.conjugadaMatriz([[[4, 8], [-3, -10]], [[-6, 4], [2, -8]]]),([[[4, -8], [-3, 10]], [[-6, -4], [2, 8]]]))
    def test_conjugadaMatriz2(self):
        self.assertEqual(calculadoraCom.conjugadaMatriz([[[2, 1], [-8, -3]], [[6, -8], [-2, 8]]]),([[[2, -1], [-8, 3]], [[6, 8], [-2, -8]]]))

    def test_tensorMatriz(self):
        self.assertEqual(calculadoraCom.tensorMatriz([[[-10, -5], [-9, 9]], [[1, 5], [-3, -2]]],[[[-9, -7], [7, 7]], [[-3, -4], [2, -10]]]),([[[55, 115], [-35, -105], [144, -18], [-126, 0]], [[10, 55], [-70, 90], [63, 9], [72, 108]], [[26, -52], [-28, 42], [13, 39], [-7, -35]], [[17, -19], [52, 0], [1, 18], [-26, 26]]]))
    def test_tensorMatriz2(self):
        self.assertEqual(calculadoraCom.tensorMatriz([[[-1, -7], [-10, 1]], [[-8, -7], [-9, -8]]],[[[-4, -2], [8, -5]], [[1, -3], [-5, 0]], [[0, -6], [-3, 0]]]),([[[-10, 30], [-43, -51], [42, 16], [-75, 58]], [[-22, -4], [5, 35], [-7, 31], [50, -5]], [[-42, 6], [3, 21], [6, 60], [30, -3]], [[18, 44], [-99, -16], [20, 50], [-112, -19]], [[-29, 17], [40, 35], [-33, 19], [45, 40]], [[-42, 48], [24, 21], [-48, 54], [27, 24]]]))

    def test_probabilidad(self):
        self.assertEqual(calculadoraCom.probabilidadPosicion([[2, 1], [-1, 2], [0, 1], [1,0], [3,-1], [2,0], [0,-2], [-2,1], [1,-3], [0,-1]] ,7),(10.87))

    
if __name__=='__main__':
    unittest.main()
