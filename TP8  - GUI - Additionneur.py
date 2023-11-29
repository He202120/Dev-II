from tkinter import *

EXPRESSION = ""

#Création de l'interface graphique
gui = Tk()
# Couleur de fond
gui.configure(background="#101419")

# Titre de l'application
gui.title("Calculatrice")

# Tailler de la fenetre
gui.geometry("870x80")

#Création de la variable qui permet d'afficher(doit être crée après la création de du gui)
equation = StringVar()

#Création des cadre pour écrire
ValeurA = Entry(gui,width=40)
ValeurB = Entry(gui,width=40)

def calculer(signe):
    """
    Effectue un calcul en fonction du signe spécifié et met à jour la variable de contrôle equation.

    Args:
        signe (str): Le signe de l'opération à effectuer ("+", "-", "*", "/").

    PRE:
        - Les valeurs dans les champs de texte (ValeurA et ValeurB) doivent être convertibles en entiers.
        - Le paramètre signe doit être l'un des signes valides ("+", "-", "*", "/").
    POST:
        - Si la conversion et le calcul réussissent, le résultat est affiché dans la variable de contrôle (equation).
        - Si une erreur de valeur (ValueError) se produit pendant la conversion, affiche "erreur" dans la variable de contrôle.
        - Si le signe spécifié n'est pas valide, affiche "erreur" dans la variable de contrôle.
    """
    try:
        global EXPRESSION
        if signe == "+":
            EXPRESSION = int(ValeurA.get()) + int(ValeurB.get()) # Le .get() permet de recupérer les données misent dans champs text
        elif signe == "/":
            EXPRESSION = int(ValeurA.get()) / int(ValeurB.get())
        elif signe == "-":
            EXPRESSION = int(ValeurA.get()) - int(ValeurB.get())
        elif signe == "*":
            EXPRESSION = int(ValeurA.get()) * int(ValeurB.get())
        else:
            equation.set("erreur")

        total = str(EXPRESSION)
        equation.set(total)
    except ValueError:
        equation.set("erreur")

#Création du bouton central - avec la fonction calculer qui y est appelé à chaque clique
BoutonPlus = Button(gui,text="+", width=40, command=lambda bouton="+": calculer(bouton))
BoutonDiviser = Button(gui,text="/", width=40, command=lambda bouton="/": calculer(bouton))
BoutonSoustraire = Button(gui,text="-", width=40, command=lambda bouton="-": calculer(bouton))
BoutonMultiplier = Button(gui,text="*", width=40, command=lambda bouton="*": calculer(bouton))

#Création de la zone d'affichage juste en-dessous du bouton
resultat = Label(gui, bg="#101419", fg="#FFF", textvariable=equation, height=2)

#Mise en place des élémentes par colones et rangée
ValeurA.grid(column=0, row=0)
ValeurB.grid(column=2, row=0)
BoutonPlus.grid(column=1, row=0)
BoutonDiviser.grid(column=0,row=1)
BoutonSoustraire.grid(column=1,row=1)
BoutonMultiplier.grid(column=2,row=1)
resultat.grid(column=1,row=2)

if __name__ == "__main__":

    #Commande permettant de garder le gui en permanence ouvert
    gui.mainloop()
