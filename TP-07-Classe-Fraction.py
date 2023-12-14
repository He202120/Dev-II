
class Fraction:
    """Classe représentant une fraction et les opérations sur celle-ci.

    Auteur : V. Van den Schrieck
    Date : Octobre 2021
    Cette classe permet la manipulation de fractions à travers plusieurs opérations.
    """

    def __init__(self, num=0, den=1):
        """Initialise une fraction avec un numérateur et un dénominateur.

        PRE: -
        POST : Initialise un objet Fraction avec le numérateur et le dénominateur fournis.
        """

        if den == 0 or not isinstance(den, int) or not isinstance(num, int):
            raise ValueError("Les deux composants doivent être des entiers et le dénominateur ne peut pas être 0")
        else:
            if den < 0:
                self.num = int(num * -1)
                self.den = abs(den)
            else:
                self.num = int(num)
                self.den = int(den)
        if not isinstance(self.num, int) or not isinstance(self.den, int):
            raise ValueError("Les deux composants doivent être des entiers et le dénominateur ne peut pas être 0")

    @property
    def numerator(self):
        """Obtient le numérateur de la fraction.

        PRE: Aucun
        POST : Renvoie le numérateur de la fraction.
        """
        return self.num

    @property
    def denominator(self):
        """Obtient le dénominateur de la fraction.

        PRE: Aucun
        POST : Renvoie le dénominateur de la fraction.
        """
        return self.den

    def __str__(self):
        """Renvoie une représentation textuelle de la forme réduite de la fraction.

        PRE: Aucun
        POST : Renvoie une chaîne représentant la forme réduite de la fraction.
        """
        if self.den == 0:
            raise ZeroDivisionError("la division par 0 est impossible")
        elif self.num == 0:
            return f"{int(self.num / self.den)}"
        else:
            if self.num < 0:
                return f"{(self.num // self.plus_grand_div_com(self.num, self.den))}/{abs(self.den // self.plus_grand_div_com(self.num, self.den))}"
            else:
                return f"{self.num // self.plus_grand_div_com(self.num, self.den)}/{self.den // self.plus_grand_div_com(self.num, self.den)}"

    @property
    def as_mixed_number(self):
        """Renvoie une représentation textuelle de la forme réduite de la fraction sous forme de nombre mixte.

        Un nombre mixte est la somme d'un entier et d'une fraction.

        PRE: Aucun
        POST : Renvoie une chaîne représentant le nombre mixte.
        """
        try:
            partie_entiere = int(self.num / self.den)
        except ZeroDivisionError:
            return "la division par 0 est impossible"
        except TypeError:
            return "la valeur renseigné n'est pas un entier"

        reste = self.num % self.den
        if reste == 0:
            if self.num < 0:
                return str(f"{partie_entiere}")
            else:
                return str(partie_entiere)
        else:
            if self.num < 0:
                return f"{partie_entiere} -{reste}/{self.den}"
            else:
                return f"{partie_entiere} {reste}/{self.den}"

    def __add__(self, autre):
        """Surcharge de l'opérateur + pour les fractions.

            PRE: `autre` est un objet Fraction.
            POST : Renvoie un nouvel objet Fraction représentant la somme de self et autre.
            """
        num1 = self.num * autre.den  # numérateur a*d
        num2 = autre.num * self.den  # numérateur c*b
        den_commun = self.den * autre.den  # dénominateur commun b*d
        num_somme = num1 + num2  # numérateur de la somme a*d+c*b
        return Fraction(num_somme, den_commun)

    def __sub__(self, autre):
        """Surcharge de l'opérateur - pour les fractions.

        PRE: `autre` est un objet Fraction.
        POST : Renvoie un nouvel objet Fraction représentant la différence entre self et autre.
        """
        num1 = self.num * autre.den  # numérateur a*d
        num2 = autre.num * self.den  # numérateur c*b
        den_commun = self.den * autre.den  # dénominateur commun b*d
        num_soustraction = num1 - num2  # numérateur de la soustraction a*d-c*b
        return Fraction(num_soustraction, den_commun)

    def __mul__(self, autre):
        """Surcharge de l'opérateur * pour les fractions.

        PRE: `autre` est un objet Fraction.
        POST : Renvoie un nouvel objet Fraction représentant le produit de self et autre.
        """
        nouveau_num = self.num * autre.num
        nouveau_den = self.den * autre.den
        return Fraction(nouveau_num, nouveau_den)

    def __truediv__(self, autre):
        """Surcharge de l'opérateur / pour les fractions.

        PRE: `autre` est un objet Fraction.
        POST : Renvoie un nouvel objet Fraction représentant la division de self par autre.
        """
        if autre.num == 0:
            raise ZeroDivisionError("division par 0 impossible")
        nouveau_num = self.num * autre.den
        nouveau_den = self.den * autre.num
        return Fraction(nouveau_num, nouveau_den)

    def __pow__(self, autre):
        """Surcharge de l'opérateur ** pour les fractions.

        PRE: `autre` un objet Fraction.
        POST : Renvoie un nouvel objet Fraction représentant self élevé à la puissance autre.
        """
        new_num = self.num ** autre.num
        new_den = self.den ** autre.num

        return Fraction(new_num, new_den)

    def __eq__(self, autre):
        """Surcharge de l'opérateur == pour les fractions.

        PRE: `autre` est un objet Fraction.
        POST : Renvoie True si self est égal à autre, False sinon.
        """
        return self.num * autre.den == autre.num * self.den

    def __float__(self):
        """Renvoie la valeur décimale de la fraction.

        PRE: Aucun
        POST : Renvoie un float représentant la valeur décimale de la fraction.
        """
        return self.num / self.den

    @property
    def is_zero(self):
        """Vérifie si la valeur de la fraction est 0.

        PRE: Aucun
        POST : Renvoie True si la fraction représente 0, False sinon.
        """
        return self.num / self.den == 0

    @property
    def is_integer(self):
        """Vérifie si une fraction est un entier (ex : 8/4, 3, 2/2, ...).

        PRE: Aucun
        POST : Renvoie True si la fraction est un entier, False sinon.
        """
        nbr = self.num / self.den
        try:
            isinstance(nbr,int)
        except ValueError:
            return False
        else:
            return nbr.is_integer()

    @property
    def is_proper(self):
        """Vérifie si la valeur absolue de la fraction est < 1.

        PRE: Aucun
        POST : Renvoie True si la fraction est une fraction propre, False sinon.
        """
        return abs(self.num) < abs(self.den)

    @property
    def is_unit(self):
        """Vérifie si le numérateur de la fraction est 1 dans sa forme réduite.

        PRE: Aucun
        POST : Renvoie True si la fraction est une fraction unitaire, False sinon.
        """
        return self.num == 1

    def is_adjacent_to(self, autre):
        """Vérifie si deux fractions diffèrent d'une fraction unitaire.

        Deux fractions sont adjacentes si la valeur absolue de leur différence est une fraction.

        PRE: `autre` est un objet Fraction.
        POST : Renvoie True si les fractions sont adjacentes, False sinon.
        """
        return abs(self.num * autre.den - autre.num * self.den) != 1

    def plus_grand_div_com(self, a, b):
        """Va trouver le plus grand diviseur commun pour a et b.

        Nous permettra de trouver la plus petite forme d'un fraction en divisant le numérateur et le dénominateur par le pgcd des deux

        PRE: -
        POST : Renvoie le plus grand diviseur commun pour a et b.
        """
        d = abs(a)
        while (a % d != 0 or b % d != 0):
            d = d - 1
        return d



la = Fraction(2,2)
print(la)
print(la.is_integer)




