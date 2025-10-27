# Artkathon
  Sujet : Créer un programme qui génère automatiquement une œuvre d’art abstraite à partir de données. Le rendu final doit être une image statique (PNG ou JPG), produite uniquement par votre code.
## Equipe
3 Data Engineers :
- **Esteban COSTA**
- **Guillaume DEMERGÈS**
- **Wafah LEMAISSI**
    
## Description du projet
=> Lancement du projet avec un échange des différentes idées. 
=> Décision de créer une Heat Map qui, en fonction du jeu de données, rempli un tableau avec un dégradé de couleurs suivant la température en entrée du fichier.
=> Après avoir mis en place un POC pour la heatmap, nous avons consulté notre enseignant qui nous a conseillé d'avoir plus d'abstraction. Suite à cela, nous avons revu le modèle pour générer une sortie qui représente une galaxie d'étoiles. 

La thématique principale du code serait le réchauffement climatique. Le flux de données récupéré représente les variations de températures au fil des mois depuis les années 1850 jusqu'à aujourd'hui. 
Les données représenteront en fonction de la tempérautre une couleur qui s'affichera dans un style dégradé tel que l'image ci-dessous : 

<img width="1011" height="495" alt="image" src="https://github.com/user-attachments/assets/527cbbe6-bbdf-412a-b49c-98960bf84e17" />

Les différents datasets peuvent être sélectionnés depuis une interface **Streamlit**, permettant de choisir :

- la **région** (*globe*, *hémisphère nord/sud*, *continents*, etc.)
- la **surface** (*terre*, *océan*, ou *les deux*)
- le **paramètre** (*température moyenne* `tavg` ou *précipitations* `pcp`)
- la **période d’années** à afficher

## Fonctionnement du code
Voici comment se déroule de façon séquentielle le code python permettant la création d'une image à partir d'un dataset en JSON. 

1 : récupération des inputs de l'utilisateur (le nom du fichier d'entrée, le nom de la colonne année ainsi que le nom de la colonne valeur et enfin le nom de sortie du fichier)
2 : vérification de l'existence du fichier JSON et gestion d'érreurs 
3 : récupération des données dans le dataset grâce aux inputs de l'utilisateur
4 : normalisation des données (les données seront entre 0 et 1, cela évite que si on a une valeur à 100 et une a 5000000 on en voit pas une des deux)
5 : définition du canevas sur lequel on va insérer les cercles
6 : déssiner les cercles grâce aux paramètres définis dans le code (taille min et max des cercles, couleur min et max du jaune pour les étoiles) et utilisation de la valeur normalisée pour définir la taille et l'intensité de chaque cercle. Pour avoir un effet de "galaxie" et pas une ligne centrale, la position verticale des cercles est aléatoire pour un rendu visuel pour attrayant. 
7 : sauvegarde et exportation du fichier dans le répertoir d'éxécution du code

## Utilisation du programme
Pour lancer le programme, nous vous conseillons de créer un dossier dans lequel vous aurez le programme nommé "V2" ainsi que le dataset associé. 
Une fois sur votre éditeur, lancez le code. 

Il vous demandera : 
- le nom du fichier à partir duquel vous souhaitez générer une image
- le nom de la colonne de temps (Année)
- le nom de la colonne contenant les valeurs (ventes?)
- le nom de sortie du fichier (ex : monfichier)

Ensuite, il génèrera une image à partir de vos données que vous pourrez trouver dans le même répertoi où vous avez executé le code. 
  
## Source des données

Les données proviennent directement de la plateforme officielle de la **NOAA** :  
[Climate at a Glance – Global Time Series](https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series)

L’API publique de la NOAA fournit les **anomalies de température** et de **précipitation** sous forme de **fichier JSON**, exploitées en temps réel par le programme.
