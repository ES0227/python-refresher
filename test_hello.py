import unittest
import hello
import math


class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello.hello(), "Hello, world!")
        self.assertNotEqual(hello.hello(), "Hi")
        

    def test_sin(self):
        self.assertEqual(hello.sin(0), 0)
        self.assertEqual(hello.sin(1), 0.8414709848078965)

    def test_cos(self):
        self.assertEqual(hello.cos(0), 1)
        self.assertEqual(hello.cos(1), 0.5403023058681398)

    def test_tan(self):
        self.assertEqual(hello.tan(0), 0)
        self.assertEqual(hello.tan(1), 1.5574077246549023)

    def test_cot(self):
        self.assertEqual(hello.cot(0), float("inf"))
        self.assertEqual(hello.cot(1), 0.6420926159343306)

    def test_add(self):
        self.assertEqual(hello.add(0, 1), int(0+1))
        self.assertEqual(hello.add(4, 5), int (4+5))
        self.assertEqual(hello.add(25, 40), int(25+40))
        
    def test_sub(self):
        self.assertEqual(hello.sub(1,0), int(1-0))
        self.assertEqual(hello.sub(90, 30), int(90-30))
        self.assertEqual(hello.sub(400, 20), int(400-20))
        
    
    def test_mul(self):
        self.assertEqual(hello.mul(0, 1), int(0))
        self.assertEqual(hello.mul(8, 7), int(8*7))
        self.assertEqual(hello.mul(20, 7), int(20*7))
    
    def test_div(self):
        self.assertEqual(hello.div(2, 1), int(2))
        self.assertEqual(hello.div(8, 7), float(8/7))
        self.assertEqual(hello.div(20, 7), float(20/7))
    
    def test_sqrt(self):
        self.assertEqual(hello.sqrt(16), int(4))
        self.assertEqual(hello.sqrt(64), int(8))
        self.assertEqual(hello.sqrt(100), int(10))

    def test_power(self):
        self.assertEqual(hello.power(2, 1), int(2))
        self.assertEqual(hello.power(8, 7), int(8**7))
        self.assertEqual(hello.power(20, 7), int(20**7))
    
    def test_log(self):
        self.assertEqual(hello.log(10), math.log(10))

    
    

    
    


    

if __name__ == "__main__":
    unittest.main()
