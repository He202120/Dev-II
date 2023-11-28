from tkinter import *

EXPRESSION = ""


def Calculer(Signe):
    try:
        global expression
        if Signe == "+":
            expression = int(ValeurA.get()) + int(ValeurB.get()) # Le .get() permet de recupérer les données misent dans champs text
        elif Signe == "/":
            expression = int(ValeurA.get()) / int(ValeurB.get())
        elif Signe == "-":
            expression = int(ValeurA.get()) - int(ValeurB.get())
        elif Signe == "*":
            expression = int(ValeurA.get()) * int(ValeurB.get())
        else:
            equation.set("erreur")

        total = str(expression)
        equation.set(total)
    except:
        equation.set("erreur")


if __name__ == "__main__":

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

    #Création du bouton central - avec la fonction Calculer qui y est appelé à chaque clique
    BoutonPlus = Button(gui,text="+", width=40, command=lambda bouton="+": Calculer(bouton))
    BoutonDiviser = Button(gui,text="/", width=40, command=lambda bouton="/": Calculer(bouton))
    BoutonSoustraire = Button(gui,text="-", width=40, command=lambda bouton="-": Calculer(bouton))
    BoutonMultiplier = Button(gui,text="*", width=40, command=lambda bouton="*": Calculer(bouton))

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

    #Commande permettant de garder le gui en permanence ouvert
    gui.mainloop()