
"""Fichier permettant de créer une base d'entrainement"""

class Learn():
    """Classe permettant de créer une base d'entrainement"""

    def __init__(self):
        """Initialisation de la base d'entrainement"""

        self.__error = 2
        self.__lst_input = []
        self.__lst_output = []

    def add_input(self, val):
        """Permet de rajouter une entrée"""

        self.__lst_input.append(val)

    def add_output(self, val):
        """Permet de rajouter une sortie"""

        self.__lst_output.append(val)

    # En-dessous de cette ligne, il n'y a rien de vraiment interressant
    # Ils ne permettent que de récupérer une valeur ou de mettre une valeur

    def set_error(self, val):
        """Permet de mettre un nombre d'erreur déterminé"""
        self.__error = val

    def get_input(self, i_values):
        """Permet d'avoir la valeur de l'input i"""
        return self.__lst_input[i_values]

    def get_output(self, i_values):
        """Permet d'avoir la valeur de l'output i"""
        return self.__lst_output[i_values]

    def get_error(self):
        """Permet d'avoir le nombre d'erreurs"""
        return self.__error
