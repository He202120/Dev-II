#test des fonctions
test1 = Fraction(1,2)
test2 = Fraction(2,2)
test3 = Fraction(4,2)
test4 = Fraction(5,3)
test5 = Fraction(0,3)
test6 = Fraction(-6,4)
#test7 = Fraction(4,0)

#fonction str
print("-----------------------------------------------------------------")
print("Test de la fonction __str__")
print("Avec une fraction simplifié (1/2)")
print(test1)
print("Avec une fraction non simplifié (4/2)")
print(test3)
print("Avec un fraction négative (-2/4)")
print(test6)
print("-----------------------------------------------------------------")
#fonction as_mixed_number
print("Avec un fraction dont le numérateur vaut 0 (0/3)")
print(test5.as_mixed_number)
print("Avec un fraction dont le numérateur est positif (5/3)")
print(test4.as_mixed_number)
print("Test de la fonction as_mixed_number avec (-2/4)")
print(test6.as_mixed_number)
print("-----------------------------------------------------------------")

#fonction __add__
print("Test de la fonction __add__ avec (1/2 + 2/2)")
nouvelle_fraction_plus = test1 + test2
print(nouvelle_fraction_plus)
print("Avec une fraction négative (1/2 + -6/4)")
nouvelle_fraction_plus = test1 + test6
print(nouvelle_fraction_plus)
print("-----------------------------------------------------------------")

#fonction __sub__
print("Test de la fonction __sub__ avec (1/2 - 2/2)")
nouvelle_fraction_moins = test1 - test2
print(nouvelle_fraction_moins)
print("Test de la fonction __sub__ avec (4/2 - 1/2)")
nouvelle_fraction_moins = test3 - test1
print(nouvelle_fraction_moins)
print("-----------------------------------------------------------------")

#fonction __mul__
print("Test de la fonction __mul__ avec (1/2 * 2/2)")
nouvelle_fraction_mult = test1 * test2
print(nouvelle_fraction_mult)
print("-----------------------------------------------------------------")

#fonction __truediv__
print("Test de la fonction __truediv__ avec (1/2 / 2/2)")
nouvelle_fraction_div = test1 / test2
print(nouvelle_fraction_div)
print("-----------------------------------------------------------------")
# print("Test de la fonction __truediv__ avec (1/2 / 0/3)")
# nouvelle_fraction_div = test1 / test5
# print(nouvelle_fraction_div)

#fonction __pow__
print("Test de la fonction __pow__ avec (1/2 ** 1/2)")
nouvelle_fraction_expo = test1 ** test1
print(nouvelle_fraction_expo)
print("-----------------------------------------------------------------")

#fonction __eq__
print("Test de la fonction __eq__ avec (1/2 == 1/2)")
nouvelle_fraction_egal = test1 == test1
print(nouvelle_fraction_egal)
print("Meme fonction mais avec 1/2 et 2/2")
nouvelle_fraction_egal = test1 == test2
print(nouvelle_fraction_egal)
print("-----------------------------------------------------------------")

#fonction __float__
print("Test de la fonction __float__ avec (1/2)")
print(test1.__float__)
print("-----------------------------------------------------------------")

#fonction is_zero
print("Test de la fonction is_zero avec (0/3)")
print(test5.is_zero)

print("Test de la fonction is_zero avec (1/2)")
print(test1.is_zero)
print("-----------------------------------------------------------------")

#fonction is_integer
print("Test de la fonction is_integer avec (2/3)")
print(test5.is_integer)
print("-----------------------------------------------------------------")

#fonction is-proper
print("Test de la fonction is_proper avec (1/2)")
print(test1.is_proper)
print("Test de la fonction is_proper avec (4/2)")
print(test4.is_proper)
