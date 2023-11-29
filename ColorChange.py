import tkinter as tk

class ChangeurCouleurGrille:
    """
    Classe représentant une fenêtre avec une grille de boutons permettant de changer la couleur des cases.

    Args:
        racine: La fenêtre principale (root) à laquelle la grille est attachée.
        lignes (int): Le nombre de lignes dans la grille.
        colonnes (int): Le nombre de colonnes dans la grille.

    Attributs:
        lignes (int): Le nombre de lignes dans la grille.
        colonnes (int): Le nombre de colonnes dans la grille.
        grille_boutons (list): Une grille de boutons avec la taille spécifiée.

    Méthodes:
        quand_bouton_clique(i, j): Méthode appelée lorsqu'un bouton est cliqué pour changer la couleur de la case.

    Usage:
        racine = tk.Tk()
        app_grille = ChangeurCouleurGrille(racine, lignes=5, colonnes=5)
        racine.mainloop()
    """
    def __init__(self, racine, lignes, colonnes):
        """
        Initialise une grille de boutons dans la fenêtre spécifiée.

        Args:
            racine: La fenêtre principale (root) à laquelle la grille est attachée.
            lignes (int): Le nombre de lignes dans la grille.
            colonnes (int): Le nombre de colonnes dans la grille.
        """
        self.lignes = lignes
        self.colonnes = colonnes
        self.grille_boutons = [[None] * colonnes for _ in range(lignes)] #On va créer un tableau de x colonne liste sur x rangé exemple:[[None, None, None, None, None],
        for i in range(lignes):                                                                                                        # [None, None, None, None, None],
            for j in range(colonnes):                                                                                                  # [None, None, None, None, None],
                bouton = tk.Button(racine, width=5, height=2, bg="white", #définition de notre bouton                                  # [None, None, None, None, None],
                                   command=lambda i=i, j=j: self.quand_bouton_clique(i, j))                                            # [None, None, None, None, None]]
                bouton.grid(row=i, column=j)
                self.grille_boutons[i][j] = bouton  #Assignation de notre bouton dans notre table "self.grille_boutons"

    def quand_bouton_clique(self, i, j): #Création de notre fonction utilisé lors du clique de notre bouton
        """
        Change la couleur de la case (bouton) lorsqu'il est cliqué.

        Args:
            i (int): L'indice de ligne du bouton cliqué.
            j (int): L'indice de colonne du bouton cliqué.
        """
        couleur_actuelle = self.grille_boutons[i][j].cget('bg')
        nouvelle_couleur = 'black' if couleur_actuelle == 'white' else 'white'
        self.grille_boutons[i][j].config(bg=nouvelle_couleur) # .config permet de modifier une paramètre d'un obj avec tkinter ici on modifier bg (background)


if __name__ == "__main__":
    RACINE = tk.Tk()
    LIGNES = 5
    COLONNES = 5
    ChangeurCouleurGrille(RACINE, LIGNES, COLONNES)
    
    RACINE.mainloop() 
