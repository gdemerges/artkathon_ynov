import pandas as pd
import requests
from pathlib import Path
from PIL import Image, ImageDraw
import random


def load_noaa_cag_service(url: str) -> pd.DataFrame:
    """
    Charge les données JSON depuis l'URL NOAA et retourne un DataFrame pandas.
    Format NOAA : les colonnes sont des dates (YYYYMM) et les valeurs sont les anomalies.
    """
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    
    if 'data' in data:
        records = data['data']
    else:
        records = data
    
    if isinstance(records, dict):
        df = pd.DataFrame([records])
    else:
        df = pd.DataFrame(records)
    
    date_columns = [col for col in df.columns if col.isdigit() and len(col) == 6]
    
    if not date_columns:
        raise ValueError(f"Aucune colonne de date trouvée. Colonnes disponibles : {df.columns.tolist()}")
    
    records_list = []
    for col in date_columns:
        for idx, value in df[col].items():
            if pd.notna(value): 
                if isinstance(value, dict):
                    if 'value' in value:
                        num_value = value['value']
                    elif 'anomaly' in value:
                        num_value = value['anomaly']
                    else:
                        num_value = next((v for v in value.values() if isinstance(v, (int, float))), None)
                    
                    if num_value is not None:
                        records_list.append({
                            'date': col,
                            'value': float(num_value)
                        })
                else:
                    records_list.append({
                        'date': col,
                        'value': float(value)
                    })
    
    df_transformed = pd.DataFrame(records_list)
    return df_transformed


def generate_image(
    df: pd.DataFrame,
    x_col: str,
    y_col: str,
    value_col: str,
    out_path: Path,
    with_colorbar: bool = False,
    normalize: bool = True,
) -> Path:
    """
    Génère une visualisation artistique (ciel étoilé) à partir d'un DataFrame.
    
    Args:
        df: DataFrame contenant les données
        x_col: nom de la colonne pour l'axe X (ex: 'year_in_decade')
        y_col: nom de la colonne pour l'axe Y (ex: 'decade')
        value_col: nom de la colonne contenant les valeurs à visualiser
        out_path: chemin du fichier de sortie
        with_colorbar: afficher une barre de couleur (non implémenté pour l'instant)
        normalize: normaliser les valeurs entre 0 et 1
    
    Returns:
        Path du fichier image généré
    """
    required_cols = [x_col, y_col, value_col]
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Colonne '{col}' introuvable dans le DataFrame")
    
    valeurs = df[value_col].tolist()
    
    # Normalisation
    val_min = min(valeurs)
    val_max = max(valeurs)
    
    def normaliser(val):
        if val_max == val_min:
            return 0.5
        return (val - val_min) / (val_max - val_min)
    
    if normalize:
        scales = [normaliser(v) for v in valeurs]
    else:
        scales = valeurs
    
    # Définition du canevas
    hauteur = 1024
    largeur = len(valeurs) * 25  # espacement horizontal
    img = Image.new("RGB", (largeur, hauteur), color=(0, 0, 0))  # fond noir
    draw = ImageDraw.Draw(img)
    
    # Paramètres des cercles (étoiles)
    rayon_min = 5
    rayon_max = 25
    jaune_max = (255, 255, 0)
    jaune_min = (128, 128, 0)
    dispersion = hauteur // 2
    
    # Dessiner les cercles (étoiles)
    for i, s in enumerate(scales):
        # Position horizontale
        x = i * 25 + 12  # centré sur la case
        
        # Position verticale aléatoire autour du centre
        y_central = hauteur // 2
        y = int(y_central + random.uniform(-dispersion, dispersion))
        
        # Taille du cercle (s est la valeur normalisée entre 0 et 1)
        rayon = int(rayon_min + s * (rayon_max - rayon_min))
        
        # Couleur du cercle : dégradé de jaune selon l'intensité
        r = int(jaune_min[0] * (1 - s) + jaune_max[0] * s)
        g = int(jaune_min[1] * (1 - s) + jaune_max[1] * s)
        b = int(jaune_min[2] * (1 - s) + jaune_max[2] * s)
        couleur = (r, g, b)
        
        # Dessiner le cercle
        draw.ellipse(
            [x - rayon, y - rayon, x + rayon, y + rayon],
            fill=couleur
        )
    
    # Sauvegarde du fichier
    img.save(out_path)
    return out_path
