from unittest import TestCase

from sherali_adams.sherali_adams import * 
import numpy as np

class TestSA(TestCase):
    def test_look(self):
        look = fill_look(4,5)

        expected = {1: {5.0: (0, 1),
                        6.0: (0, 2),
                        8.0: (0, 3),
                        11.0: (0, 4),
                        7.0: (1, 2),
                        9.0: (1, 3),
                        12.0: (1, 4),
                        10.0: (2, 3),
                        13.0: (2, 4),
                        14.0: (3, 4)},
                    2: {15: (1, 6),
                        16: (1, 8),
                        17: (3, 6),
                        19: (1, 11),
                        20: (4, 6),
                        22: (4, 8),
                        18: (3, 7),
                        21: (4, 7),
                        23: (4, 9),
                        24: (4, 10)},
                    3: {25: (2, 16), 26: (2, 19), 27: (4, 16), 28: (4, 17), 29: (4, 18)},
                    4: {30: (3, 26)}}

        self.assertTrue(look == expected)

    def test_invert(self):
        self.assertTrue(invert(30,5,4) == [0,1,2,3,4])

    def test_instance(self):
        A = np.matrix([[-0., -1., -0., -1., -1.],
                       [ 1.,  0.,  0.,  0.,  0.],
                       [ 0.,  1.,  0.,  0.,  0.],
                       [ 0.,  0.,  1.,  0.,  0.],
                       [ 0.,  0.,  0.,  1.,  0.],
                       [ 0.,  0.,  0.,  0.,  1.],
                       [-1., -0., -0., -0., -0.],
                       [-0., -1., -0., -0., -0.],
                       [-0., -0., -1., -0., -0.],
                       [-0., -0., -0., -1., -0.],
                       [-0., -0., -0., -0., -1.]])
        
        b = np.array([-1.,  1.,  1.,  1.,  1.,  1., -0., -0., -0., -0., -0.])
        (newA,newb) = get_SA_instance(1,5,A,b)
        self.assertTrue(newA.shape == (151,15))
        self.assertTrue(all(b == np.array([-1.,  1.,  1.,  1.,  1.,  1., -0., -0., -0., -0., -0.])))


    def test_runSA(self):
        A = np.matrix([[-0., -1., -0., -1., -1.],
                       [ 1.,  0.,  0.,  0.,  0.],
                       [ 0.,  1.,  0.,  0.,  0.],
                       [ 0.,  0.,  1.,  0.,  0.],
                       [ 0.,  0.,  0.,  1.,  0.],
                       [ 0.,  0.,  0.,  0.,  1.],
                       [-1., -0., -0., -0., -0.],
                       [-0., -1., -0., -0., -0.],
                       [-0., -0., -1., -0., -0.],
                       [-0., -0., -0., -1., -0.],
                       [-0., -0., -0., -0., -1.]])
        
        b = np.array([-1.,  1.,  1.,  1.,  1.,  1., -0., -0., -0., -0., -0.])
        
        (AA,bb) = run_SA(2,5,A,b)
        self.assertTrue(AA.shape == (1711,25))

    def test_2x2(self):
        A = np.matrix([[1, 1],
                       [1, 1]])
        b = np.array([1,1])
        (AA,bb) = run_SA(1,2,A,b)
        expected = np.matrix([[ 1.,  1.,  0.],
                           [ 1.,  1.,  0.],
                           [ 0.,  0.,  1.],
                           [ 0.,  0.,  1.],
                           [ 1.,  1., -1.],
                           [ 1.,  1., -1.],
                           [ 0.,  0.,  1.],
                           [ 0.,  0.,  1.],
                           [ 1.,  1., -1.],
                           [ 1.,  1., -1.],
                           [ 1.,  0.,  0.],
                           [ 0.,  1.,  0.],
                           [ 0.,  0.,  1.],
                           [-1., -0., -0.],
                           [-0., -1., -0.],
                           [-0., -0., -1.]])
    
        self.assertTrue((AA == expected).all())
