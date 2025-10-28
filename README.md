# Artkathon
  Sujet : Créer un programme qui génère automatiquement une œuvre d’art abstraite à partir de données. Le rendu final doit être une image statique (PNG ou JPG), produite uniquement par votre code.
## Equipe
3 Data Engineers :
- **Esteban COSTA**
- **Guillaume DEMERGÈS**
- **Wafah LEMAISSI**
- **Chien Cong PHAM**
    
## Description du projet
- Lancement du projet avec un échange des différentes idées. 
- Décision de créer une Heat Map qui, en fonction du jeu de données, rempli un tableau avec un dégradé de couleurs suivant la température en entrée du fichier.
- Après avoir mis en place un POC pour la heatmap, nous avons consulté notre enseignant qui nous a conseillé d'avoir plus d'abstraction. Suite à cela, nous avons revu le modèle pour générer une sortie qui représente une galaxie d'étoiles.

Le script python a été testé sur 2 jeux de données. Le premier traite la thématique du réchauffement climatique. Le flux de données récupéré représente les variations de températures au fil des années depuis 1850 jusqu'à aujourd'hui. Le second concerne les ventes de la marque BMW au fil des années.

La représentation finale de ces données prend la forme suivante : l'utilisateur choisit la couleur du fond de l'image, et viendront s'insérer des cercles de couleur jaune.
L'objectif était, avec un fond noir, de réprésenter une galaxie d'étoiles. 
- Les cercles répondent à deux règles : leur taille leur intensité varie fonction de la valeur normalisée de la température ou du montant des ventes. Ainsi, plus l'étoile et grosse et puissante en couleur, plus la température en °C / les ventes sont élévées. 

Nous avons également mis en place une interface Streamlit, permettant de choisir (pour le dataset des températures) :
- la région
- la surface 
- le paramètre (*température moyenne* `tavg` ou *précipitations* `pcp`)
- la période d’années

Etant donné que la webapp n'était pas attendue, nous avons concentré nos efforts sur la version sans streamlit qui est dans un notebook python nommé "V2". C'est cette version qui contient le code le plus à jour.

## Fonctionnement du code
Voici comment se déroule de façon séquentielle le code python permettant la création d'une image à partir d'un dataset en JSON. 

- 1 : récupération des inputs de l'utilisateur (le nom du fichier d'entrée, le nom de la colonne année ainsi que le nom de la colonne valeur et enfin le nom de sortie du fichier, la teinte du fond avec le code RGB ...)
- 2 : vérification de l'existence du fichier JSON et vérification des valeurs RGB entrée + gestion des erreurs de saisie 
- 3 : récupération des données dans le dataset grâce aux inputs de l'utilisateur
- 4 : normalisation des données (les données seront entre 0 et 1, cela évite que si on a une valeur à 100 et une a 5000000 on en voit pas une des deux)
- 5 : définition du canevas sur lequel on va insérer les cercles
- 6 : déssiner les cercles grâce aux paramètres définis dans le code (taille min et max des cercles, couleur min et max du jaune pour les étoiles) et utilisation de la valeur normalisée pour définir la taille et l'intensité de chaque cercle. Pour avoir un effet de "galaxie" et pas une ligne centrale, la position verticale des cercles est aléatoire pour un rendu visuel pour attrayant.
- 7 : sauvegarde et exportation du fichier dans le répertoir d'éxécution du code

Ces étapes sont "manuelles" lorsqu'on lance le code, toutefois une interface Streamlit gère ces étapes avec une interface visuelle. 

## Utilisation du programme (sans l'interface Streamlit)
Pour lancer le programme, rendez vous dans le dossier "version sans streamlit" et ouvrer le notebook python nommé "V2".  
Une fois sur votre éditeur, lancez le notebook. 

Il vous demandera : 
- le nom du fichier à partir duquel vous souhaitez générer une image
- le nom de la colonne de temps (Année)
- le nom de la colonne contenant les valeurs (ventes?)
- le nom de sortie du fichier (ex : monfichier)
- la valeur rouge du fond
- la valeur vert du fond
- la valeur bleu du fond

Ensuite, il génèrera une image à partir de vos données que vous pourrez trouver dans le même répertoir où vous avez executé le code. 

## Lancer le programme sans streamlit avec les différents datasets 
Si vous avez ouvert le notebook v2 dans votre éditeur de code, lancez-le. Ensuite veuillez répondre comme suit aux différentes questions qui vous seront posées dans la console : 

1 - Pour le dataset BMW nommé "data.json", répondre comme suit aux questions de la console : 
data.json / année / ventes / imagebmw / 0 / 0 / 0

2 - Pour le dataset des températures nommé "autredata.json", répondre comme suit aux questions de la console : 
autredata.json / année /anomaly / imagetemperatures / 0 / 0 / 0

Maintenant, vous avez l'image associée au dataset dans votre répertoire. Il est important de noter qu'en lançant le programme avec les mêmes données, l'image finale peut varier car la position verticale des cercles est aléatoire.

## Utilisation du programme (avec l'interface Streamlit)
--- ici guillaume est ce que tu peux juste pointer les différences
