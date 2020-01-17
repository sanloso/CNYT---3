import unittest
import calculadoraCom

class testCalculadora(unittest.TestCase):
    def test_sumaComplejos(self):
        self.assertEqual(calculadoraCom.suma([2,3.4],[3,-4.5]),([5.0, -1.1]))
    def test_sumaComplejos2(self):
        self.assertEqual(calculadoraCom.suma([4,5],[4,6]),([8.0, 11.0]))
    def test_sumaComplejos3(self):
        self.assertEqual(calculadoraCom.suma([1,-3],[0,2]),([1.0, -1.0]))

    def test_restaComplejos(self):
        self.assertEqual(calculadoraCom.resta([3,-2],[4,6]),([-1.0, -8.0]))
    def test_restaComplejos2(self):    
        self.assertEqual(calculadoraCom.resta([3,2],[5,-6]),([-2.0, 8.0]))
    def test_restaComplejos3(self):
        self.assertEqual(calculadoraCom.resta([5,1],[5,3]),([0.0, -2.0]))

    def test_multiplicacionComplejos(self):
        self.assertEqual(calculadoraCom.multiplicar([2,3],[4,5]),([-7, 22]))
    def test_multiplicacionComplejos2(self):
        self.assertEqual(calculadoraCom.multiplicar([2,1],[2,-3]),([7, -4]))
    def test_multiplicacionComplejos3(self):
        self.assertEqual(calculadoraCom.multiplicar([4,-3],[4,-3]),([7, -24]))

    
    def test_divisionComplejos(self):
        self.assertEqual(calculadoraCom.dividir([3,2],[-1,2]),([0.2, -1.6]))
    def test_divisionComplejos2(self):
        self.assertEqual(calculadoraCom.dividir([2,4],[4,-2]),([0.0, 1.0]))
    def test_divisionComplejos3(self):
        self.assertEqual(calculadoraCom.dividir([1,-4],[3,1]),([-0.1, -1.3]))
    
    def test_moduloComplejos(self):
        self.assertEqual(calculadoraCom.modulo([3,5]),(5.831))
    def test_moduloComplejos2(self):
        self.assertEqual(calculadoraCom.modulo([6,2]),(6.325))
    def test_moduloComplejos3(self):
        self.assertEqual(calculadoraCom.modulo([10,22]),(24.166))

    def test_conjugadoComplejos(self):
        self.assertEqual(calculadoraCom.conjugado([3,5]),([3, -5]))
    def test_conjugadoComplejos2(self):
        self.assertEqual(calculadoraCom.conjugado([6,2]),([6, -2]))
    def test_conjugadoComplejos3(self):
        self.assertEqual(calculadoraCom.conjugado([10,-22]),([10, 22]))

    def test_convertorComplejos(self):
        self.assertEqual(calculadoraCom.convertor([4,-5]),([6.403, -0.896]))
    def test_convertorComplejos2(self):
        self.assertEqual(calculadoraCom.convertor([8,12]),([14.422, 0.983]))
    def test_convertorComplejos3(self):
        self.assertEqual(calculadoraCom.convertor([4,10]),([10.77, 1.19]))
        
if __name__=='__main__':
    unittest.main()
