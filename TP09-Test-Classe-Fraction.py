import unittest
from tp9 import Fraction


class TestFractionMethods(unittest.TestCase):

    def test_creation(self):
        frac = Fraction(1, 2)
        self.assertEqual(frac.numerator, 1,"Test normal : numérateur")
        self.assertEqual(frac.denominator, 2,"Test normal : dénominateur")
        frac2 = Fraction(-1,2)
        self.assertEqual(frac2.numerator, -1,"Test négatif : numérateur")
        self.assertEqual(frac2.denominator, 2,"Test négatif : dénominateur")
        self.assertRaises(ZeroDivisionError, Fraction, 2.2, 2)
        self.assertRaises(ZeroDivisionError, Fraction, "", 2)
        self.assertRaises(ZeroDivisionError, Fraction, 3, 0)

    def test_str_representation(self):
        frac = Fraction(3, 4)
        self.assertEqual(str(frac), '3/4',"Test normal : 3/4 ")
        frac2 = Fraction(8, 4)
        self.assertEqual(str(frac2), '2/1',"Test simplification : 8/4 ")
        frac3 = Fraction(-8, 4)
        self.assertEqual(str(frac3), '-2/1',"Test simplification négatif : -8/4 ")
        frac4 = Fraction(0, 4)
        self.assertEqual(str(frac4), '0', "Test simplification négatif : -8/4 ")
        self.assertRaises(ZeroDivisionError, Fraction, 3, 0)
        self.assertRaises(ZeroDivisionError, Fraction, 3, "aa")

    def test_mixed_number_representation(self):
        frac = Fraction(1, 2)
        self.assertEqual(frac.as_mixed_number, '0 1/2',"Test normal : 1/2")
        frac2 = Fraction(5, 2)
        self.assertEqual(frac2.as_mixed_number, '2 1/2',"Test simplification : 5/2")
        frac3 = Fraction(-5, 2)
        self.assertEqual(frac3.as_mixed_number, '-2 -1/2',"Test simplification négatif : -5/2")
        frac4 = Fraction(4, 2)
        self.assertEqual(frac4.as_mixed_number, '2', "Test simplification négatif : -5/2")
        frac5 = Fraction(-4, 2)
        self.assertEqual(frac5.as_mixed_number, '-2', "Test simplification négatif : -5/2")


    def test_addition(self):
        frac1 = Fraction(1, 2)
        frac2 = Fraction(1, 2)
        result = frac1 + frac2
        self.assertEqual(result.numerator, 4,"Test addition normal : 1/2+1/2")
        self.assertEqual(result.denominator, 4,"Test addition normal : 1/2+1/2")
        self.assertEqual(str(result), '1/1',"Test normal : 4/4 ")
        frac3 = Fraction(-4, 2)
        frac4 = Fraction(1, 2)
        result2 = frac3 + frac4
        self.assertEqual(result2.numerator, -6,"Test addition négatif : -4/2+1/2")
        self.assertEqual(result2.denominator, 4,"Test addition négatif : -4/2+1/2")
        self.assertEqual(str(result2), '-3/2',"Test négatif : -6/4 ")
        self.assertRaises(ZeroDivisionError, Fraction, 3, 0)
        self.assertRaises(ZeroDivisionError, Fraction, 3, "aa")

    def test_division(self):
        frac1 = Fraction(1, 2)
        frac2 = Fraction(1, 2)
        result = frac1 / frac2
        self.assertEqual(result.numerator, 2,"Test divisions normal : 1/2 / 1/2")
        self.assertEqual(result.denominator, 2,"Test divisions normal : 1/2 / 1/2")
        frac3 = Fraction(1, 2)
        frac4 = Fraction(-1, 2)
        result2 = frac3 / frac4
        self.assertEqual(result2.numerator, -2,"Test divisions négatif : 1/2 / -1/2")
        self.assertEqual(result2.denominator, 2,"Test divisions négatif : 1/2 / -1/2")
        frac3 = Fraction(3, 4)
        frac4 = Fraction(0, 4)
        self.assertRaises(ZeroDivisionError, frac3.__truediv__, frac4)

    def test_egalite(self):
        frac1 = Fraction(1, 2)
        frac2 = Fraction(1, 2)
        self.assertEqual(frac1 == frac2, True,"Test egalité : 1/2 == 1/2")
        frac3 = Fraction(4, 4)
        frac4 = Fraction(2, 2)
        self.assertEqual(frac3 == frac4, True,"Test egalité après str : 4/4 == 2/2")
        frac5 = Fraction(-1, 2)
        frac6 = Fraction(1, 2)
        self.assertEqual(frac5 == frac6, False,"Test egalité négatif : -1/2 == 1/2")

    def test_integer_check(self):
        frac = Fraction(2, 2)
        frac2 = Fraction(5, 2)
        frac3 = Fraction(-2, 2)
        self.assertTrue(frac.is_integer,"Test entier positif : 2/2")
        self.assertFalse(frac2.is_integer,"Test no entier positif : 5/2")
        self.assertTrue(frac3.is_integer,"Test entier négatif : -2/2")


    def test_proper_fraction_check(self):
        frac = Fraction(3, 2)
        frac2 = Fraction(1, 2)
        frac3 = Fraction(-3, 2)
        self.assertFalse(frac.is_proper,"Test proper < 1 : 3/2")
        self.assertTrue(frac2.is_proper,"Test proper > 1 : 1/2")
        self.assertFalse(frac3.is_proper,"Test proper négatif > 1 : -3/2")

    def test_adjacent_check(self):
        frac1 = Fraction(1, 2)
        frac2 = Fraction(1, 2)
        self.assertTrue(frac1.is_adjacent_to(frac2),"Test adjacent avec : 1/2 is adjacent 1/2")
        frac3 = Fraction(4, 4)
        frac4 = Fraction(2, 2)
        self.assertTrue(frac3.is_adjacent_to(frac4),"Test adjacent avec : 4/4 is adjacent 2/2")
        frac3 = Fraction(-1, 2)
        frac4 = Fraction(1, 2)
        self.assertTrue(frac3.is_adjacent_to(frac4),"Test adjacent avec négatif: -1/2 is adjacent 1/2")

    def test_float_check(self):
        frac1 = Fraction(1, 2)
        self.assertEqual(float(frac1), 0.5,"Test float avec : 1/2 is adjacent 1/2")

if __name__ == '__main__':
    unittest.main()
