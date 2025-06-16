from arrera_tk import *

class CAnWorkGUI:
    def __init__(self, arrtk : CArreraTK,nameAssistant : str):
        self.__arrTk = arrtk
        self.__screen = self.__arrTk.aTopLevel(width=500,height=600,
                                         title=nameAssistant + " : Arrera Work",
                                         resizable=False)

        # Frame
        self.__fAcceuil = self.__arrTk.createFrame(self.__screen,width=500,height=530,bg="red")

        self.__fDock = self.__arrTk.createFrame(self.__screen,width=500,height=70,bg="blue")


        self.__fAcceuil.pack()
        self.__fDock.pack()

    def active(self):
        self.__arrTk.view()

