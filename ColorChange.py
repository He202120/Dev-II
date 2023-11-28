import tkinter as tk

class ChangeurCouleurGrille:
    def __init__(self, racine, lignes, colonnes):
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
        couleur_actuelle = self.grille_boutons[i][j].cget('bg')
        nouvelle_couleur = 'black' if couleur_actuelle == 'white' else 'white'
        self.grille_boutons[i][j].config(bg=nouvelle_couleur) # .config permet de modifier une paramètre d'un obj avec tkinter ici on modifier bg (background)


if __name__ == "__main__":
    racine = tk.Tk()
    lignes = 5
    colonnes = 5
    ChangeurCouleurGrille(racine, lignes, colonnes)
    
    racine.mainloop() 

