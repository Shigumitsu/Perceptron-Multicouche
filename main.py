
"""Interface permettant de plus facilement rentrer les paramètres
Pour ceux qui découvre mon code, merci de m'executer afin d'utiliser le PMC"""

# Merci au code de Mastard69 qui m'a permis de comprendre et de réaliser ce projet
# Page web du concerné :
# https://openclassrooms.com/forum/sujet/perceptron-multicouches-42413

# Les modules externes
from random import uniform
from itertools import product
from math import exp

# Mes modules
import tools
import layer
import learn
# import neuron

def main():
    """Le programme commence ici
    Invite l'utilisateur à rentrer les données ici"""

    # On demande le nombre de neurones d'entrée
    nb_input = tools.input_to_int("Combien de neurones d'entrée ? : ", 1, 50)

    # On demande le nombre de neurones dans la couche cachée
    nb_hidden = tools.input_to_int("Combien de neurones dans la " + \
    "couche cachée ? : ", 1, 50)

    # On demande le nombre de neurones de sortie
    nb_output = tools.input_to_int("Combien de neurones de sortie ? : ", 1, 50)

    tools.print_line()

    # On créer le perceptron multicouche demandée
    print("Création du perceptron multicouche demandée...")

    # Création des couches
    layer_input = layer.Layer(nb_input)
    layer_hidden = layer.Layer(nb_hidden)
    layer_output = layer.Layer(nb_output)

    print("Terminée !\n")

    # On créer une base d'exercice au perceptron
    print("Création d'une base d'entrainement au perceptron...")
    valid = True
    lst_learn = []
    while valid:
        tools.print_line()
        print("Base d'exercice n°", len(lst_learn) + 1, "\n")
        print("-- Début de l'apprentissage --")
        lst_learn.append(learn.Learn())

        # On rentre les valeurs d'entrée
        for _ in range(layer_input.get_nb_neurons()):
            neuron_val = tools.input_to_int("\tValeur neurone entrée n°" + \
            str(_ + 1) + " : ")
            lst_learn[len(lst_learn) - 1].add_input(neuron_val)

        tools.print_line()

        # On rentre les valeurs de sortie
        for _ in range(layer_output.get_nb_neurons()):
            neuron_val = tools.input_to_int("\tValeur neurone sortie n°" + \
            str(_ + 1) + " : ", 0, 1)
            lst_learn[len(lst_learn) - 1].add_output(neuron_val)

        tools.print_line()

        valid = tools.question_on("Voulez-vous rentrer un autre jeu de données ?")

    print("Terminée !\n")

    # On défini un poids pour chaques entrée
    # /!\ ATTENTION : LE POIDS DOIT ETRE NORMALEMENT COMPRIS ENTRE -0,5 ET 0,5 /!\
    print("Initialisation aléatoire des poids...")
    i = j = 0

    for i, j in product(range(layer_input.get_nb_neurons()), \
    range(layer_hidden.get_nb_neurons())):
        layer_input.get_neuron(i).add_weight(uniform(-1.0, 1.0))

    i = j = 0

    for i, j in product(range(layer_hidden.get_nb_neurons()), \
    range(layer_output.get_nb_neurons())):
        layer_hidden.get_neuron(i).add_weight(uniform(-1.0, 1.0))

    print("Terminée !\n")

    # On entraine notre perceptron multicouche
    print("Entrainement du perceptron multicouche...")
    iteration = 0
    error = 1.0
    for iteration in range(1000):
        current_data = 0
        for current_data in range(len(lst_learn)):
            tools.print_line()
            print("\tInstallation des données d'apprentissage...")

            for _ in range(layer_input.get_nb_neurons()):
                layer_input.get_neuron(_).set_value(lst_learn[current_data].get_input(_))
                layer_input.get_neuron(_).set_sigmoid(lst_learn[current_data].get_input(_))

            for _ in range(layer_output.get_nb_neurons()):
                layer_output.get_neuron(_).set_value(lst_learn[current_data].get_output(_))

            print("\tPropagation avant 1...")

            i = 0
            for i in range(layer_hidden.get_nb_neurons()):
                sumw = 0.0
                for _ in range(layer_input.get_nb_neurons()):
                    sumw += layer_input.get_neuron(_).get_sigmoid() * \
                    layer_input.get_neuron(_).get_weight(i)
                layer_hidden.get_neuron(i).set_potential(sumw)
                layer_hidden.get_neuron(i).set_sigmoid(1/(1 + exp((-1)*sumw)))

            print("\tPropagation avant 2...")

            i = 0
            for i in range(layer_output.get_nb_neurons()):
                sumw = 0.0
                for _ in range(layer_hidden.get_nb_neurons()):
                    sumw += layer_hidden.get_neuron(_).get_sigmoid() * \
                    layer_hidden.get_neuron(_).get_weight(i)
                layer_output.get_neuron(i).set_potential(sumw)
                layer_output.get_neuron(i).set_sigmoid(1/(1 + exp((-1)*sumw)))

            print("\tCalcul de l'erreur...")
            lst_learn[current_data].set_error(layer_output.calc_error())

            print("\tSignal d'erreur couche sortie...")
            for _ in range(layer_output.get_nb_neurons()):
                layer_output.get_neuron(_).calc_error()

            print("\tSignal d'erreur couche cachée...")
            i = 0

            for i in range(layer_hidden.get_nb_neurons()):
                phy = layer_hidden.get_neuron(i).get_sigmoid() * \
                (1 - layer_hidden.get_neuron(i).get_sigmoid())
                rm = 0.0

                for _ in range(layer_hidden.get_neuron(i).get_nb_weights()):
                    rm += layer_output.get_neuron(_).get_error() * \
                    layer_hidden.get_neuron(i).get_weight(_)
                layer_hidden.get_neuron(i).set_error(phy * rm)

            print("\tCorrection poids sortie...")
            i = j = 0
            for i, j in product(range(layer_hidden.get_nb_neurons()), \
            range(layer_hidden.get_neuron(i).get_nb_weights())):
                layer_hidden.get_neuron(i).set_weight(j, \
                layer_hidden.get_neuron(i).get_weight(j) + \
                layer_hidden.get_neuron(i).get_sigmoid() * \
                layer_output.get_neuron(j).get_error())

            print("\tCorrection poids cachée...")
            i = j = 0
            for i, j in product(range(layer_input.get_nb_neurons()), \
            range(layer_input.get_neuron(i).get_nb_weights())):
                layer_input.get_neuron(i).set_weight(j, \
                layer_input.get_neuron(i).get_weight(j) + \
                layer_input.get_neuron(i).get_sigmoid() * \
                layer_hidden.get_neuron(j).get_error())

            current_data = current_data + 1
            print("\tCalcul de la moyenne d'erreur...")
            total_error = 0.0

            for _ in range(len(lst_learn)):
                total_error += lst_learn[_].get_error()

            error = total_error / len(lst_learn)

            print("\n\tMoyenne d'erreur :", error)

        if error <= 0.05:
            break

    tools.print_line()

    print("Fin de l'apprentissage !")

    # On affiche la valeur de la sortie finale
    print("Valeur de la sortie finale :")
    for _ in range(layer_output.get_nb_neurons()):
        print("\tNeurone n°", _ + 1, ":", layer_output.get_neuron(_).get_sigmoid())

    print("\nTerminée !")

    tools.print_line()
    print("Test de l'apprentissage :")

    # Tant que l'utilisateur veut tester son programme
    valid = True
    while valid:
        # On test l'apprentissage donnée
        for _ in range(layer_input.get_nb_neurons()):
            neuron_val = tools.input_to_int("\tValeur neurone entrée n°" + \
            str(_ + 1) + " : ")
            layer_input.get_neuron(_).set_value(neuron_val)
            layer_input.get_neuron(_).set_sigmoid(neuron_val)

        print("Passage dans le réseau de neurone...")
        i = 0

        for i in range(layer_hidden.get_nb_neurons()):
            sumw = 0.0
            for _ in range(layer_input.get_nb_neurons()):
                sumw += layer_input.get_neuron(_).get_sigmoid() * \
                layer_input.get_neuron(_).get_weight(i)
            layer_hidden.get_neuron(i).set_potential(sumw)
            layer_hidden.get_neuron(i).set_sigmoid(1/(1 + exp((-1)*sumw)))

            i = 0
            for i in range(layer_output.get_nb_neurons()):
                sumw = 0.0
                for _ in range(layer_hidden.get_nb_neurons()):
                    sumw += layer_hidden.get_neuron(_).get_sigmoid() * \
                    layer_hidden.get_neuron(_).get_weight(i)
                layer_output.get_neuron(i).set_potential(sumw)
                layer_output.get_neuron(i).set_sigmoid(1/(1 + exp((-1)*sumw)))

        print("Terminée !")

        tools.print_line()

        # Affichage des résultats
        print("Affichage des résultats :")
        for _ in range(layer_output.get_nb_neurons()):
            print("\tNeurone n°", _, ":", layer_output.get_neuron(_).get_sigmoid())

        # On demande à l'utilisateur s'il veut faire un autre test
        valid = tools.question_on("Voulez-vous faire un autre test ?")

    # Fin du programme
    print("Fin du programme !")
    return 0

if __name__ == "__main__":
    main()
