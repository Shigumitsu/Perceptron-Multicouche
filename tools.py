"""Ce fichier permet de mettre des fonctions utiles"""

from pydoc import locate

def color_message(message, color, reset_color="0"):
    """Permet de colorer un message
    -----
    Arguments:

    message : Message que vous voulez écrire en couleur
    Vous pouvez mettre plusieurs arguments en les séparant avec des virgule,
    directement dans le str.
    type : Str

    color : Couleur et mise en forme que vous voulez mettre à votre texte
    type : Str

    reset_color : Couleur de remise à 0
    type : Str

    -----
    Valeur de retour

    0: Si aucun problème
    Quitte le programme si problème"""

    # verif_var("color_message", "message", message, "string")
    # verif_var("color_message", "color", color, "string")
    # verif_var("color_message", "reset_color", reset_color, "string")
    color = "\033[" + color + "m"
    reset_color = "\033[" + reset_color + "m"
    print(color + message + reset_color)
    return

def verif_var(name_var, value_var, type_var, min_values=None, max_values=None):
    """Permet de vérifier si votre variable est bien comme celle demandée
    -----
    Arguments:

    name_var: Nom de la variable (utile pour le message d'erreur)
    type : Str

    value_var: Valeur de la variable à verifier
    type: Tout

    type_var : Type de variable à valider
    type : Str

    min_values : Si le nombre doit être au-dessus d'une certaine valeur
    type : Int, Float

    max_values : Si le nombre doit être en-dessous d'une certaine valeur
    type : Int, Float

    -----
    Valeur retourné:

    0 : Si aucun problème
    Quitte : Si un ou plusieurs problème(s)
    """

    # verif_var("verif_var", "name_def", name_def, "str")
    # verif_var("verif_var", "name_var", name_var, "str")
    # verif_var("verif_var", "type_var", type_var, "str")


    if not all(isinstance(_, (float, int, type(None))) \
    for _ in [max_values, min_values]):
        color_message("verif_var | Erreur : La valeur min ou/et max ne sont" + \
        " ni des int, ni des floats !\n", "31")
        return False

    if (min_values and max_values) != None and min_values > max_values:
        color_message("verif_var | Erreur : La valeur min est plus grande" + \
        " que la max !\n", "31")
        return False

    type_switch = {
        0 : "bool",
        1 : "memoryview",
        2 : "type",
        3 : "complex",
        4 : "dict",
        5 : "type(Ellipsis)",
        6 : "float",
        7 : "int",
        8 : "list",
        9 : "int",
        10 : "object",
        11 : "type(None)",
        12 : "type(NotImplemented)",
        13 : "slice",
        14 : "bytes",
        15 : "str",
        16 : "tuple",
        17 : "range",
    }

    i = 0
    for i in range(19):
        if i == 18 or type_var.lower() == type_switch.get(i).lower():
            break
    if i >= 18:
        color_message("verif_var | Erreur : Le type que vous avez rentré " + \
        "n'existe pas !\n", "31")
        return False

    if not isinstance(value_var, locate(type_switch.get(i))):
        color_message("Erreur : La valeur de " + name_var + \
        " n'est pas du bon type !\n", "31")
        return False

    if max_values and min_values:
        return True
    elif isinstance(value_var, (float, int)):
        if max_values != None and value_var > max_values:
            color_message("Erreur : La valeur de " + name_var + \
            " est supérieur au max de " + str(max_values) + " !\n", "31")
            return False
        elif min_values != None and value_var < min_values:
            color_message("Erreur : La valeur de " + name_var + \
            " est inférieur au min de " + str(min_values) + " !\n", "31")
            return False
    return True

def input_to_int(str_input="", min_values=None, max_values=None):
    """Transforme un input en int"""
    verif_var("str_input", str_input, "str")
    while 1:
        nb_input = input(str_input)
        try:
            nb_input = int(nb_input)
        except ValueError:
            color_message("Erreur: Vous n'avez pas rentrée un nombre valide\n",\
            "31")
            continue
        if verif_var("nb_input", nb_input, "int", min_values, max_values):
            break
    return nb_input

def question_on(str_input):
    """Permet de faire une question oui/non"""
    answer = input(str_input + " [o]/n : ")
    print()
    if answer.lower() in ('o', ''):
        return True
    return False

def print_line():
    """Permet de tracer des lignes"""
    print("\n##################################################\n")
