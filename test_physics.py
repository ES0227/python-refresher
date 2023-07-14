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
    
    def test_acceleration_calculator (self):
        self.assertEqual (physics.calculate_acceleration (9, 9), 1)
        with self.assertRaises (ValueError):
            (physics.calculate_acceleration (-1, 0))
    
    def test_angAcceleration_calculator (self):
        self.assertEqual (physics.calculate_angular_acceleration (10, 5), 2)
        with self.assertRaises (ValueError):
            (physics.calculate_angular_acceleration (5, -3))
    
    def test_torque_calculator (self):
        self.assertAlmostEqual (physics.calculate_torque (5, 45, 7), 24.749) #np.sin(np.radians(45)*35))
        with self.assertRaises (ValueError):
            (physics.calculate_torque (-1, 5, 4))

    def test_momentOfInertia_calculator (self):
        self.assertEqual (physics.calculate_moment_of_inertia(2, 4), 32)
        with self.assertRaises (ValueError):
            (physics.calculate_moment_of_inertia (-3, 5))
    
    def test_auvAcceleration_calculator (self):
        self.assertAlmostEqual (physics.calculate_auv_acceleration (5, 30, 100, 0.1, 0.5))
            
    
            
            


    

        
#if __name__ == "__main__":
    #__main__()