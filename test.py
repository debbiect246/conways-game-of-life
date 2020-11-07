import unittest

class Testgameoflife(unittest.TestCase):
    def oneneighbour():
        result = tick(True,1)
        self.assert(result,False) 

if __name__ == '__main__':
    unittest.main()


