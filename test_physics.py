import physics
import unittest


class testPhysics (unittest.TestCase):

    def test_correct_buoyancy(self):
        self.assertEqual(physics.calculate_buoyancy(9, 100), 8829)
        with self.assertRaises(ValueError):
            (physics.calculate_buoyancy(9, -10))
        self.assertNotEqual(physics.calculate_buoyancy(9, 100), 10)
    
    def test_correct_float(self):
        self.assertEqual(physics.will_it_float(7, 5), True)
        with self.assertRaises(ValueError):
            (physics.will_it_float(-5, 3))
        self.assertEqual(physics.will_it_float(1/1000, 1), None)
                         
    def test_correct_pressure(self):
        self.assertEqual(physics.calculate_pressure(5), 150375)
        with self.assertRaises(ValueError):
            (physics.calculate_pressure(-10))

        
if __name__ == "__main__":
    __main__()
