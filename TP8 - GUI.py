from tkinter import *

EXPRESSION = ""

#Création de l'interface graphique
gui = Tk()
# Couleur de fond
gui.configure(background="#101419")

# Titre de l'application
gui.title("Calculatrice")

# Tailler de la fenetre
gui.geometry("660x50")

#Création de la variable qui permet d'afficher(doit être crée après la création de du gui)
equation = StringVar()

#Création des cadre pour écrire
ValeurA = Entry(gui,width=25)
ValeurB = Entry(gui,width=25)

def calculer():
    """
    Effectue le calcul de la somme de deux valeurs récupérées à partir de deux champs de texte.

    PRE:
        - Les valeurs dans les champs de texte (ValeurA et ValeurB) doivent être convertibles en entiers.
    POST:
        - Si la conversion et le calcul réussissent, la somme est affichée dans une variable de contrôle (equation).
        - Si une erreur de valeur (ValueError) se produit pendant la conversion, affiche "erreur" dans la variable de contrôle.
    """
    try:
        global EXPRESSION
        EXPRESSION = int(ValeurA.get()) + int(ValeurB.get()) # Le .get() permet de recupérer les données misent dans champs text
        total = str(EXPRESSION)
        equation.set(total)
    except ValueError:
        equation.set("erreur")

#Création du bouton central - avec la fonction calculer qui y est appelé à chaque clique
BoutonA = Button(text="Appuyer pour valider", width=50, command=calculer)

#Création de la zone d'affichage juste en-dessous du bouton
resultat = Label(gui, bg="#101419", fg="#FFF", textvariable=equation, height=2)

#Mise en place des élémentes par colones et rangée
ValeurA.grid(column=0, row=0)
BoutonA.grid(column=1, row=0)
ValeurB.grid(column=2, row=0)
resultat.grid(row=1,column=1)

#Commande permettant de garder le gui en permanence ouvert

if __name__ == "__main__":
    gui.mainloop()
    
