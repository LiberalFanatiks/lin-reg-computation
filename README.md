# lin-reg-computation
Ce projet fournit une implémentation simple et pédagogique d'une régression linéaire en Python. Il calcule les coefficients d'une droite de régression à partir de données brutes et visualise le résultat avec Matplotlib, sans dépendre de bibliothèques statistiques complexes comme NumPy ou SciPy.

## Objectif
L’objectif est de démontrer les bases mathématiques de la régression linéaire (moyenne, variance, covariance, écart-type) et d’illustrer son application sur un jeu de données représentant des heures d’étude et des notes obtenues. Ce code est idéal pour les apprenants ou développeurs souhaitant comprendre ces concepts de manière pratique.

## Fonctionnalités
- Calcul de la moyenne, variance, covariance et écart-type à partir de listes de nombres.
- Détermination des coefficients \( a \) (pente) et \( b \) (ordonnée à l’origine) de la droite \( y = ax + b \).
- Calcul du coefficient de corrélation \( r \) pour évaluer la relation linéaire.
- Visualisation des données et de la droite de régression avec Matplotlib.

## Prérequis
- **Python** : Version 3.x
- **Bibliothèques** :
- `matplotlib` (pour les graphiques)
- `math` (inclus dans Python)

Installez les dépendances avec :
```bash
pip install matplotlib
```

## Utilisation

1. Clonez le dépôt :
```bash
git clone https://github.com/LiberalFanatiks/lin-reg-computation.git
```

2. Exécutez le script :
```bash
python main.py
```

3. Observez le graphique généré et les valeurs de a, b, et r affichées dans la console.


## Exemple de données

- Entrée :
    - x=[1,3,3,5]
        (heures d’étude)
    - y=[3,4,6,5]
        (notes obtenues)
- Sortie :
    Un graphique avec les points de données et la droite de régression.
    Coefficients calculés affichés (ex. : a=0.5; b=2.5 r=0.8).

## Structure du code

- average(data) : Calcule la moyenne d’une liste.
- variance(x) : Calcule la variance d’une série.
- covariance(x, y) : Calcule la covariance entre deux séries.
- deviation(x) : Calcule l’écart-type à partir d’une variance.
- main() : Coordonne les calculs et génère le graphique.

Chaque fonction est documentée avec des docstrings au format Google.

## Exemple de résultat
Graphique de régression linéaire
![Graphique de régression linéaire](https://raw.githubusercontent.com/LiberalFanatiks/lin-reg-computation/refs/heads/main/graphique.png)

### Améliorations possibles

- Ajouter des vérifications pour gérer les listes vides ou de longueurs différentes.
- Permettre la lecture des données depuis un fichier (ex. : CSV).
- Optimiser les calculs en évitant les appels redondants à average().

## Auteur

[LiberalFanatiks aka @AvicenienRazien]

Contact : [biczosam.2024@gmail.com]