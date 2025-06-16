from arrera_tk import *

class CAnWorkGUI:
    def __init__(self, arrtk : CArreraTK,nameAssistant : str):
        self.__arrTk = arrtk
        self.__screen = self.__arrTk.aTopLevel(width=500, height=600,
                                               title=nameAssistant + " : Arrera Work",
                                               resizable=True)

        # Row 0 = rouge, row 1 = bleu
        self.__screen.rowconfigure(0, weight=1)  # le rouge occupe tout sauf la place du bleu
        self.__screen.rowconfigure(1, weight=0)  # le bleu a une hauteur fixe
        self.__screen.columnconfigure(0, weight=1)
        self.__screen.columnconfigure(1, weight=2)
        self.__screen.columnconfigure(2, weight=1)

        # Frames
        self.__fAcceuil = self.__arrTk.createFrame(self.__screen, bg="red")
        self.__fDock = self.__arrTk.createFrame(self.__screen, bg="blue", height=70)

        # Frame rouge, tout en haut, occupe toute la largeur, sticky "nsew" pour grandir dans toutes les directions
        self.__fAcceuil.grid(row=0, column=0, columnspan=3, sticky='nsew')
        # Frame bleu, tout en bas, sticky "ew" pour couvrir toute la largeur
        self.__fDock.grid(row=1, column=0, columnspan=3, sticky='ew')

    def active(self):
        self.__arrTk.view()