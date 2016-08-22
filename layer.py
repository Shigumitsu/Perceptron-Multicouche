
"""Défini une couche"""

# Mes modules
import neuron

class Layer:
    """Permet de contenir les neurones"""

    def __init__(self, nb_neuron):
        """Initialisation de la couche"""

        # Création d'une liste de neurones
        self.__lst_neuron = []
        # Création des neurones dans la couche
        for _ in range(nb_neuron):
            self.add_neuron()

    def add_neuron(self):
        """Permet de rajouter un neurone dans la couche"""

        # On rajoute un neurone dans la liste de neurone
        self.__lst_neuron.append(neuron.Neuron(0.0))

    def calc_error(self):
        """Permet de calculer le nombre d'erreur"""

        err = 0.0
        for _ in range(len(self.__lst_neuron)):
            err += pow(self.__lst_neuron[_].get_value() - self.__lst_neuron[_].get_sigmoid(), 2)

        return 0.5 * err

    def get_neuron(self, i):
        """Permet d'avoir le neurone i"""

        return self.__lst_neuron[i]

    def get_nb_neurons(self):
        """Permet d'avoir le nombre de neuronnes dans cette couche"""

        return len(self.__lst_neuron)
