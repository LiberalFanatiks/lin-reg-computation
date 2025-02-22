#coding: utf-8
import matplotlib.pyplot as plt
import math
 
def average(data : list) -> float:
    """Calcule la moyenne arithmétique d'une liste de nombres.

    Args:
        data (list): Liste de nombres (int ou float).

    Returns:
        float: La moyenne des éléments de la liste.

    Raises:
        ZeroDivisionError: Si la liste est vide.
    """
    sum = 0
    for i in data:
        sum += i
    return sum / len(data)

 

def variance(x) -> float:
    """Calcule la variance d'une série de données.

    La variance est définie comme la moyenne des carrés moins le carré de la moyenne.

    Args:
        x (list): Liste de nombres (int ou float).

    Returns:
        float: La variance de la série.

    Raises:
        ZeroDivisionError: Si la liste est vide.
    """
    x_square = [x[i] * x[i] for i in range(len(x))]
    xsquare_average = average(x_square)
    x_average = average(x)
 

    return xsquare_average - x_average * x_average

def covariance(x, y) -> float:
    """Calcule la covariance entre deux séries de données.

    Args:
        x (list): Première liste de nombres (int ou float).
        y (list): Deuxième liste de nombres (int ou float), de même longueur que x.

    Returns:
        float: La covariance entre x et y.

    Raises:
        ZeroDivisionError: Si une des listes est vide.
        ValueError: Si les listes n'ont pas la même longueur.
    """

    xy = [x[i] * y[i] for i in range(len(x))]
    xy_average = average(xy)
    x_average = average(x)
    y_average = average(y)
    return xy_average - x_average * y_average

def deviation(x: float) -> float:
    """Calcule l'écart-type à partir d'une variance.

    Args:
        x (float): La variance (doit être un nombre positif ou zéro).

    Returns:
        float: La racine carrée de x, représentant l'écart-type.

    Raises:
        ValueError: Si x est négatif (car la racine carrée d'un nombre négatif n'est pas réelle).
    """
    return math.sqrt(x)
 
def main():
    plt.figure(1)
    
    x = [1, 3, 3, 5] # Les heures 
    y = [3, 4, 6, 5] # Les notes 

    plt.plot(x, y, marker='o', linestyle='-', color='b', label="Notes en fonction du temps passé")
    plt.xlabel("X - axe")
    plt.xlabel("Y - axe")
    plt.title("Note(x) en fonction de Heure(x)")
    plt.legend()
    
    # Calculer la regression linéaire 
    cov_xy =  covariance(x, y)
    variance_x = variance(x)
    variance_y = variance(y)
    a = cov_xy / variance_x
    b = average(y) - a * average(x)
    y = lambda x : a*x+b
    r = cov_xy / (deviation(variance_x) * deviation(variance_y))

    print(f"a={a};b={b} {r}")

    linear = [y(1), y(2), y(3), y(4), y(5)]
    plt.plot([1, 2, 3, 4, 5], linear, marker='s', linestyle='--', color='r', label="Regression linéaire")
    plt.show()

main()