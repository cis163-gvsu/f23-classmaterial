import unittest

def foo(x,y):
    '''
    if isinstance(x, str) or isinstance(y,str):
        raise TypeError
    '''
    if y == 0:
        raise ValueError
    return x/y

class MyTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(foo(4,2), 2)

    def test2(self):
        self.assertEqual(foo(10,2),5)

    def test3(self):
        self.assertEqual(foo(-6,-2),3)
    
    def test4(self):
        self.assertEqual(foo(-5,1),-5)

    def test5(self):
        self.assertEqual(foo(6,-2),-3)

    def test6(self):
        self.assertEqual(foo(0,2800),0)

    def test7(self):
        self.assertEqual(foo(3.5,7),0.5)

    def testDivideBy0(self):
        self.assertRaises(ValueError, foo, 5, 0)

    def testDivideBy0v2(self):
        with self.assertRaises(ValueError):
            foo(5,0)

if __name__ == '__main__':
    unittest.main()
