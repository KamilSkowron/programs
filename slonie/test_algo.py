import unittest
from algo_testy import Zoo

class TestZoo(unittest.TestCase):

    def test_funkcja0(self):
        self.slo0 = Zoo("slo0.in")
        self.assertEqual(self.slo0.funkcja(), 11200)
        
    def test_funkcja1(self):
        self.slo1 = Zoo("slo1.in")
        self.assertEqual(self.slo1.funkcja(), 30518)

    def test_funkcja2(self):
        self.slo2 = Zoo("slo2.in")
        self.assertEqual(self.slo2.funkcja(), 23445)

    def test_funkcja3(self):
        self.slo3 = Zoo("slo3.in")
        self.assertEqual(self.slo3.funkcja(), 12123447)

    def test_funkcja4(self):
        self.slo4 = Zoo("slo4.in")
        self.assertEqual(self.slo4.funkcja(), 44923212)

    def test_funkcja5(self):
        self.slo5 = Zoo("slo5.in")
        self.assertEqual(self.slo5.funkcja(), 30028497)

    def test_funkcja6(self):
        self.slo6 = Zoo("slo6.in")
        self.assertEqual(self.slo6.funkcja(), 827992171)

    def test_funkcja7(self):
        self.slo7 = Zoo("slo7.in")
        self.assertEqual(self.slo7.funkcja(), 3264674811)

    def test_funkcja8a(self):
        self.slo8a = Zoo("slo8a.in")
        self.assertEqual(self.slo8a.funkcja(), 3333482707)

    def test_funkcja8b(self):
        self.slo8b = Zoo("slo8b.in")
        self.assertEqual(self.slo8b.funkcja(), 2589)

    def test_funkcja9a(self):
        self.slo9a = Zoo("slo9a.in")
        self.assertEqual(self.slo9a.funkcja(), 320834354)

    def test_funkcja9b(self):
        self.slo9b = Zoo("slo9b.in")
        self.assertEqual(self.slo9b.funkcja(), 3297708227)

    def test_funkcja10a(self):
        self.slo10a = Zoo("slo10a.in")
        self.assertEqual(self.slo10a.funkcja(), 3399736984)

    def test_funkcja10b(self):
        self.slo10b = Zoo("slo10b.in")
        self.assertEqual(self.slo10b.funkcja(), 3401255691)

    def test_funkcja1ocen(self):
        self.slo1ocen = Zoo("slo1ocen.in")
        self.assertEqual(self.slo1ocen.funkcja(), 1534)

    def test_funkcja2ocen(self):
        self.slo2ocen = Zoo("slo2ocen.in")
        self.assertEqual(self.slo2ocen.funkcja(), 62398)

    def test_funkcja3ocen(self):
        self.slo3ocen = Zoo("slo3ocen.in")
        self.assertEqual(self.slo3ocen.funkcja(), 24000)

    def test_funkcja4ocen(self):
        self.slo4ocen = Zoo("slo4ocen.in")
        self.assertEqual(self.slo4ocen.funkcja(), 99999800)


if __name__ == '__main__':
    unittest.main()