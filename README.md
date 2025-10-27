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

La thématique principale du code serait le réchauffement climatique. Le flux de données récupéré représente les variations de températures au fil des mois depuis les années 1850 jusqu'à aujourd'hui. 
Les données représenteront en fonction de la tempérautre une couleur qui s'affichera dans un style dégradé tel que l'image ci-dessous : 

<img width="1011" height="495" alt="image" src="https://github.com/user-attachments/assets/527cbbe6-bbdf-412a-b49c-98960bf84e17" />

Les différents datasets peuvent être sélectionnés depuis une interface **Streamlit**, permettant de choisir :

- la **région** (*globe*, *hémisphère nord/sud*, *continents*, etc.)
- la **surface** (*terre*, *océan*, ou *les deux*)
- le **paramètre** (*température moyenne* `tavg` ou *précipitations* `pcp`)
- la **période d’années** à afficher
  
## Source des données

Les données proviennent directement de la plateforme officielle de la **NOAA** :  
[Climate at a Glance – Global Time Series](https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series)

L’API publique de la NOAA fournit les **anomalies de température** et de **précipitation** sous forme de **fichier JSON**, exploitées en temps réel par le programme.
