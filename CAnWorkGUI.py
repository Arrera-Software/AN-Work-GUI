from arrera_tk import *

class CAnWorkGUI:
    def __init__(self, arrtk : CArreraTK,nameAssistant : str,asset:str):
        self.__arrTk = arrtk
        self.__emplacementAsset = asset+"/"
        self.__screen = self.__arrTk.aTopLevel(width=500, height=600,
                                               title=nameAssistant + " : Arrera Work",
                                               resizable=True)

        # Row 0 = rouge, row 1 = bleu
        self.__screen.rowconfigure(0, weight=1)  # le rouge occupe tout sauf la place du bleu
        self.__screen.rowconfigure(1, weight=0)  # le bleu a une hauteur fixe
        self.__screen.columnconfigure(0, weight=1)
        self.__screen.columnconfigure(1, weight=2)
        self.__screen.columnconfigure(2, weight=1)

        # Recuperation des image
        imgTableur = self.__arrTk.createImage(self.__emplacementAsset + "tableur.png",tailleX=100, tailleY=100)
        imgWord = self.__arrTk.createImage(self.__emplacementAsset + "word.png",tailleX=100, tailleY=100)
        imgProject = self.__arrTk.createImage(self.__emplacementAsset + "project.png",tailleX=100, tailleY=100)

        # Frames
        self.__fAcceuil = self.__arrTk.createFrame(self.__screen)
        self.__fDock = self.__arrTk.createFrame(self.__screen, bg="blue", height=70)

        # Widgets dans la frame d'accueil
        labelTitle = self.__arrTk.createLabel(self.__fAcceuil, text=nameAssistant + " : Arrera Work",ppolice="Arial",ptaille=25)
        btnArreraTableur = self.__arrTk.createButton(self.__fAcceuil,width=100, height=100, image=imgTableur)
        btnArreraWord = self.__arrTk.createButton(self.__fAcceuil, width=100, height=100, image=imgWord)
        btnArreraProject = self.__arrTk.createButton(self.__fAcceuil, width=100, height=100, image=imgProject)

        # Grille des frame
        # Ajoute 3 lignes à fAcceuil pour jouer sur le centrage vertical
        self.__fAcceuil.rowconfigure(0, weight=1)  # espace au dessus
        self.__fAcceuil.rowconfigure(1, weight=0)  # boutons ici
        self.__fAcceuil.rowconfigure(2, weight=1)  # espace en dessous

        # Colonnes pareil pour leur largeur
        self.__fAcceuil.columnconfigure(0, weight=1)
        self.__fAcceuil.columnconfigure(1, weight=2)
        self.__fAcceuil.columnconfigure(2, weight=1)

        # Affichage des frames
        labelTitle.grid(row=0, column=0, columnspan=3, sticky='new', pady=20)  # En haut, centré, espacé en haut

        # Placement des boutons sur la même ligne et centrés
        btnArreraTableur.grid(row=1, column=0, padx=10, pady=60)
        btnArreraWord.grid(row=1, column=1, padx=10, pady=60)
        btnArreraProject.grid(row=1, column=2, padx=10, pady=60)

        # Affichage main
        self.__fAcceuil.grid(row=0, column=0, columnspan=3, sticky='nsew')
        #self.__fDock.grid(row=1, column=0, columnspan=3, sticky='ew')

    def active(self):
        self.__arrTk.view()