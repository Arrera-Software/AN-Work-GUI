from arrera_tk import *

class CAnWorkGUI:
    def __init__(self, arrtk : CArreraTK,nameAssistant : str,asset:str):
        # Attributs
        self.__tableurOpen = False
        # Attributs de l'interface
        self.__arrTk = arrtk
        self.__emplacementAsset = asset+"/"
        self.__screen = self.__arrTk.aTopLevel(width=500, height=650,
                                               title=nameAssistant + " : Arrera Work",
                                               resizable=True)

        # Row 0 = rouge, row 1 = bleu
        self.__screen.rowconfigure(0, weight=1)  # le rouge occupe tout sauf la place du bleu
        self.__screen.rowconfigure(1, weight=0)  # le bleu a une hauteur fixe
        self.__screen.columnconfigure(0, weight=1)
        self.__screen.columnconfigure(1, weight=2)
        self.__screen.columnconfigure(2, weight=1)

        # Recuperation des image
        imgTableurAcceuil = self.__arrTk.createImage(self.__emplacementAsset + "tableur.png",tailleX=100, tailleY=100)
        imgWordAcceuil = self.__arrTk.createImage(self.__emplacementAsset + "word.png",tailleX=100, tailleY=100)
        imgProjectAcceuil = self.__arrTk.createImage(self.__emplacementAsset + "project.png",tailleX=100, tailleY=100)

        imgTableurDock = self.__arrTk.createImage(self.__emplacementAsset + "tableur.png",tailleX=50, tailleY=50)
        imgWordDock = self.__arrTk.createImage(self.__emplacementAsset + "word.png",tailleX=50, tailleY=50)
        imgProjectDock = self.__arrTk.createImage(self.__emplacementAsset + "project.png",tailleX=50, tailleY=50)
        imgAnnulerDock = self.__arrTk.createImage(self.__emplacementAsset + "annuler.png",tailleX=50, tailleY=50)

        # Images pour la frame Tableur
        imgAddComptage = self.__arrTk.createImage(self.__emplacementAsset + "tableur/add-comptagexcf.png",
                                                  tailleX=90, tailleY=90)
        imgAddMaxmum = self.__arrTk.createImage(self.__emplacementAsset + "tableur/add-maxmum.png",
                                                tailleX=90, tailleY=90)
        imgAddMinimum = self.__arrTk.createImage(self.__emplacementAsset + "tableur/add-minimum.png",
                                                 tailleX=90, tailleY=90)
        imgAddMoyenne = self.__arrTk.createImage(self.__emplacementAsset + "tableur/add-moyenne.png",
                                                 tailleX=90, tailleY=90)
        imgAddSomme = self.__arrTk.createImage(self.__emplacementAsset + "tableur/add-somme.png"
                                               ,tailleX=90, tailleY=90)
        imgAddValeur = self.__arrTk.createImage(self.__emplacementAsset + "tableur/add-valeur.png"
                                                ,tailleX=90, tailleY=90)
        imgCloseTableur = self.__arrTk.createImage(self.__emplacementAsset + "tableur/close-tableur.png"
                                                   ,tailleX=90, tailleY=90)
        imgOpenTableur = self.__arrTk.createImage(self.__emplacementAsset + "tableur/open-tableur.png"
                                                  ,tailleX=90, tailleY=90)
        imgOpenTableurCoputerSoft = self.__arrTk.createImage(self.__emplacementAsset + "tableur/open-tableur-coputer-soft.png"
                                                             ,tailleX=90, tailleY=90)
        imgReadTableur = self.__arrTk.createImage(self.__emplacementAsset + "tableur/read-tableur.png"
                                                  ,tailleX=90, tailleY=90)
        imgSupprValeur = self.__arrTk.createImage(self.__emplacementAsset + "tableur/suppr-valeur.png"
                                                  ,tailleX=90, tailleY=90)
        imgViewTableur = self.__arrTk.createImage(self.__emplacementAsset + "tableur/view-tableur.png"
                                                  ,tailleX=90, tailleY=90)

        # Frames
        self.__fAcceuil = self.__arrTk.createFrame(self.__screen)
        self.__fDock = self.__arrTk.createFrame(self.__screen, bg="grey", height=70)
        self.__fTableur = self.__arrTk.createFrame(self.__screen)
        self.__fTableurNoOpen = self.__arrTk.createFrame(self.__screen)
        self.__fWord = self.__arrTk.createFrame(self.__screen)
        self.__fProjet = self.__arrTk.createFrame(self.__screen)

        # Widgets dans la frame d'accueil
        labelTitleAcceuil = self.__arrTk.createLabel(self.__fAcceuil, text=nameAssistant + " : Arrera Work",
                                              ppolice="Arial",ptaille=25)
        btnArreraTableurAcceuil = self.__arrTk.createButton(self.__fAcceuil,width=100,
                                                            height=100, image=imgTableurAcceuil,
                                                            command=self.__activeTableur)
        btnArreraWordAcceuil = self.__arrTk.createButton(self.__fAcceuil, width=100,
                                                         height=100, image=imgWordAcceuil,
                                                         command=self.__activeWord)
        btnArreraProjectAcceuil = self.__arrTk.createButton(self.__fAcceuil, width=100,
                                                            height=100, image=imgProjectAcceuil,
                                                            command=self.__activeProjet)

        # Widgets dans la frame dock
        btnArreraTableurDock = self.__arrTk.createButton(self.__fDock,width=60,
                                                         height=60, image=imgTableurDock,
                                                         command=self.__activeTableur)
        btnArreraWordDock = self.__arrTk.createButton(self.__fDock, width=60,
                                                      height=60, image=imgWordDock,
                                                      command=self.__activeWord)
        btnArreraProjectDock = self.__arrTk.createButton(self.__fDock, width=60,
                                                         height=60, image=imgProjectDock,
                                                         command=self.__activeProjet)
        btnArreraBackAcceuilDock = self.__arrTk.createButton(self.__fDock, width=60,
                                                             height=60,image =imgAnnulerDock,
                                                             command=self.__activeAcceuil)

        # Widgets du frame Tableur
        labelTitleNoOpenTableur = self.__arrTk.createLabel(self.__fTableurNoOpen, text="Travail sur un tableur",
                                                     ppolice="Arial",ptaille=25)
        btnOpenTableur = self.__arrTk.createButton(self.__fTableurNoOpen,width=90,height=90,
                                                   image=imgOpenTableur)
        labelTitleTableur = self.__arrTk.createLabel(self.__fTableur, text="Travail sur un tableur",
                                                     ppolice="Arial",ptaille=25)
        btnOpenTableurWithComputer = self.__arrTk.createButton(self.__fTableur,width=90,height=90,image=imgOpenTableurCoputerSoft,)
        btnCloseTableur = self.__arrTk.createButton(self.__fTableur,width=90,height=90,image=imgCloseTableur)
        btnReadTableur = self.__arrTk.createButton(self.__fTableur,width=90,height=90,image=imgReadTableur)
        btnAddValeurTableur = self.__arrTk.createButton(self.__fTableur,width=90,height=90,image=imgAddValeur)
        btnAddMoyenneTableur = self.__arrTk.createButton(self.__fTableur,width=90,height=90,image=imgAddMoyenne)
        btnAddSommeTableur = self.__arrTk.createButton(self.__fTableur,width=90,height=90,image=imgAddSomme)
        btnAddComptageTableur = self.__arrTk.createButton(self.__fTableur,width=90,height=90,image=imgAddComptage)
        btnAddMinimumTableur = self.__arrTk.createButton(self.__fTableur,width=90,height=90,image=imgAddMinimum)
        btnAddMaximumTableur = self.__arrTk.createButton(self.__fTableur,width=90,height=90,image=imgAddMaxmum)
        btnAffichageTableur = self.__arrTk.createButton(self.__fTableur,width=90,height=90,image=imgViewTableur)
        btnSupprDataTableur = self.__arrTk.createButton(self.__fTableur,width=90,height=90,image=imgSupprValeur)
        # Grille des frame
        # Ajoute 3 lignes à fAcceuil pour jouer sur le centrage vertical
        self.__fAcceuil.rowconfigure(0, weight=1)  # espace au dessus
        self.__fAcceuil.rowconfigure(1, weight=0)  # boutons ici
        self.__fAcceuil.rowconfigure(2, weight=1)  # espace en dessous

        # Colonnes pareil pour leur largeur
        self.__fAcceuil.columnconfigure(0, weight=1)
        self.__fAcceuil.columnconfigure(1, weight=2)
        self.__fAcceuil.columnconfigure(2, weight=1)

        self.__fDock.grid_columnconfigure(0, weight=1)
        self.__fDock.grid_columnconfigure(5, weight=1)

        self.__fTableurNoOpen.grid_rowconfigure(0, weight=1)
        self.__fTableurNoOpen.grid_rowconfigure(1, weight=0)
        self.__fTableurNoOpen.grid_rowconfigure(2, weight=0)
        self.__fTableurNoOpen.grid_rowconfigure(3, weight=1)

        self.__fTableurNoOpen.grid_columnconfigure(0, weight=1)
        self.__fTableurNoOpen.grid_columnconfigure(1, weight=0)
        self.__fTableurNoOpen.grid_columnconfigure(2, weight=1)

        self.__fTableur.grid_columnconfigure(0, weight=1)
        self.__fTableur.grid_columnconfigure(1, weight=1)
        self.__fTableur.grid_columnconfigure(2, weight=1)

        # Affichage des frames
        labelTitleAcceuil.grid(row=0, column=0, columnspan=3, sticky='new', pady=20)  # En haut, centré, espacé en haut

        # Placement des boutons sur la même ligne et centrés
        btnArreraTableurAcceuil.grid(row=1, column=0, padx=10, pady=60)
        btnArreraWordAcceuil.grid(row=1, column=1, padx=10, pady=60)
        btnArreraProjectAcceuil.grid(row=1, column=2, padx=10, pady=60)

        # PLacement des boutons dans le dock
        btnArreraTableurDock.grid(row=0, column=1, padx=5, pady=5)
        btnArreraWordDock.grid(row=0, column=2, padx=5, pady=5)
        btnArreraProjectDock.grid(row=0, column=3, padx=5, pady=5)
        btnArreraBackAcceuilDock.grid(row=0, column=4, padx=5, pady=5)

        # Placement widget des frame Tableur
        labelTitleNoOpenTableur.grid(row=0, column=1, sticky="n")
        btnOpenTableur.grid(row=2, column=1, sticky="n")

        labelTitleTableur.grid(row=0, column=0, columnspan=3, sticky='ew')

        btnOpenTableurWithComputer.grid(row=1, column=0, padx=20, pady=20)

        btnReadTableur.grid(row=1, column=1, padx=20, pady=20)
        btnAddValeurTableur.grid(row=1, column=2, padx=20, pady=20)
        btnAddMoyenneTableur.grid(row=2, column=0, padx=20, pady=20)
        btnAddSommeTableur.grid(row=2, column=1, padx=20, pady=20)
        btnAddComptageTableur.grid(row=2, column=2, padx=20, pady=20)
        btnAddMinimumTableur.grid(row=3, column=0, padx=20, pady=20)
        btnAddMaximumTableur.grid(row=3, column=1, padx=20, pady=20)
        btnAffichageTableur.grid(row=3, column=2, padx=20, pady=20)
        btnSupprDataTableur.grid(row=4, column=0, padx=20, pady=20)
        btnCloseTableur.grid(row=4, column=1, padx=20, pady=20)


    def active(self):
        self.__activeAcceuil()
        self.__arrTk.view()

    def __disabelFrame(self, frame):
        self.__fAcceuil.grid_forget()
        self.__fDock.grid_forget()
        self.__fTableur.grid_forget()
        self.__fWord.grid_forget()
        self.__fProjet.grid_forget()
        self.__fTableurNoOpen.grid_forget()

    def __activeAcceuil(self):
        self.__disabelFrame(self.__fAcceuil)
        self.__fAcceuil.grid(row=0, column=0, columnspan=3, sticky='nsew')

    def __activeTableur(self):
        self.__disabelFrame(self.__fTableur)
        if not self.__tableurOpen:
            self.__fTableurNoOpen.grid(row=0, column=0, columnspan=3, sticky='nsew')
        else:
            self.__fTableur.grid(row=0, column=0, columnspan=3, sticky='nsew')
        self.__fTableur.grid(row=0, column=0, columnspan=3, sticky='nsew')
        self.__fDock.grid(row=1, column=0, columnspan=3, sticky='ew')

    def __activeWord(self):
        self.__disabelFrame(self.__fTableur)
        self.__fWord.grid(row=0, column=0, columnspan=3, sticky='nsew')
        self.__fDock.grid(row=1, column=0, columnspan=3, sticky='ew')

    def __activeProjet(self):
        self.__disabelFrame(self.__fTableur)
        self.__fProjet.grid(row=0, column=0, columnspan=3, sticky='nsew')
        self.__fDock.grid(row=1, column=0, columnspan=3, sticky='ew')