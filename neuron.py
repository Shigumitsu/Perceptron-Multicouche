"""Création de neurones"""

class Neuron(object):
    """Classe neurone
    Permet de stocker les données d'un neurone"""

    def __init__(self, val):
        """Création du neurone"""

        self.__value = val
        self.__potential = 0.0
        self.__sigmoid = val
        self.__error = 0.0
        self.__lst_weight = []

    def add_weight(self, w_values):
        """Permet de rajouter un poids au neurone"""

        self.__lst_weight.append(w_values)

    def calc_diff(self):
        """Permet de calculer l'équart entre la réponse du perceptron et la
        véritable réponse"""

        return self.__value - self.__sigmoid

    def calc_error(self):
        """Permet de calculer le taux d'erreur du neurone"""

        phy = self.__sigmoid * (1 - self.__sigmoid)
        self.__error = phy * self.calc_diff()

    # En-dessous de cette ligne, il n'y a rien de vraiment interressant
    # Ils ne permettent que de récupérer une valeur ou de mettre une valeur

    def get_value(self):
        """Permet d'avoir la valeur"""

        return self.__value

    def set_value(self, val):
        """Permet de mettre une valeur déterminé"""

        self.__value = val

    def get_potential(self):
        """Permet d'avoir la valeur du potentiel"""

        return self.__potential

    def set_potential(self, val):
        """Permet de mettre un potentiel déterminé"""

        self.__potential = val

    def get_sigmoid(self):
        """Permet d'avoir la valeur de la sigmoid"""

        return self.__sigmoid

    def set_sigmoid(self, val):
        """Permet de mettre une sigmoid déterminé"""

        self.__sigmoid = val

    def get_error(self):
        """Permet d'avoir le nombre d'erreurs"""

        return self.__error

    def set_error(self, val):
        """Petmet de mettre un nombre d'erreurs déterminé"""

        self.__error = val

    def get_weight(self, i_values):
        """Permet d'avoir le poids de l'entrée i"""

        return self.__lst_weight[i_values]

    def set_weight(self, i_values, val):
        """Permet de mettre un poids déterminé sur une entrée i"""

        self.__lst_weight[i_values] = val

    def get_nb_weights(self):
        """Permet d'avoir le nombre de poids dans cette neurone"""

        return len(self.__lst_weight)
