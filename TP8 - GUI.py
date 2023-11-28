from tkinter import *

expression = ""


def Calculer():
    try:
        global expression
        expression = int(ValeurA.get()) + int(ValeurB.get()) # Le .get() permet de recupérer les données misent dans champs text
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
    gui.geometry("660x50")

    #Création de la variable qui permet d'afficher(doit être crée après la création de du gui)
    equation = StringVar()

    #Création des cadre pour écrire
    ValeurA = Entry(gui,width=25)
    ValeurB = Entry(gui,width=25)

    #Création du bouton central - avec la fonction Calculer qui y est appelé à chaque clique
    BoutonA = Button(text="Appuyer pour valider", width=50, command=Calculer)

    #Création de la zone d'affichage juste en-dessous du bouton
    resultat = Label(gui, bg="#101419", fg="#FFF", textvariable=equation, height=2)

    #Mise en place des élémentes par colones et rangée
    ValeurA.grid(column=0, row=0)
    BoutonA.grid(column=1, row=0)
    ValeurB.grid(column=2, row=0)
    resultat.grid(row=1,column=1)

    #Commande permettant de garder le gui en permanence ouvert
    gui.mainloop()