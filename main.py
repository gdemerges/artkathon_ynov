# main.py
from __future__ import annotations
from pathlib import Path
import streamlit as st
from PIL import Image

from src.generate_art import load_noaa_cag_service, generate_image

st.set_page_config(page_title="Artkathon", page_icon="🎨", layout="centered")

URL_TEMPLATE = (
    "https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/"
    "time-series/{region}/{parameter}/{surface}/ytd/0/{startYear}-{endYear}/data.{format}"
)

PARAMETERS = {
    "tavg": "Average Temperature Anomaly",
    "pcp": "Precipitation",
}

REGIONS = {
    "globe": {"label": "Global", "surfaces": ["land", "ocean", "land_ocean"]},
    "nhem": {"label": "Northern Hemisphere", "surfaces": ["land","ocean","land_ocean"]},
    "shem": {"label": "Southern Hemisphere", "surfaces": ["land","ocean","land_ocean"]},
    "africa": {"label": "Africa", "surfaces": ["land"]},
    "asia": {"label": "Asia", "surfaces": ["land"]},
    "europe": {"label": "Europe", "surfaces": ["land"]},
    "northAmerica": {"label": "North America", "surfaces": ["land"]},
    "oceania": {"label": "Oceania", "surfaces": ["land"]},
    "southAmerica": {"label": "South America", "surfaces": ["land"]},
    "atlanticMdr": {"label": "Atlantic Main Development Region", "surfaces": ["land_ocean"]},
    "caribbeanIslands": {"label": "Caribbean Islands", "surfaces": ["land_ocean"]},
    "eastNPacific": {"label": "East N Pacific", "surfaces": ["land_ocean"]},
    "gulfOfAmerica": {"label": "Gulf of America", "surfaces": ["land_ocean"]},
    "hawaiianRegion": {"label": "Hawaiian Region", "surfaces": ["land_ocean"]},
    "arctic": {"label": "Arctic", "surfaces": ["land_ocean"]},
    "antarctic": {"label": "Antarctic", "surfaces": ["land_ocean"]},
}

# --- UI ---
st.title("🎨 Artkathon")
st.write("Générez des visualisations artistiques à partir des données climatiques NOAA")

colA, colB = st.columns(2)
with colA:
    region_key = st.selectbox(
        "Region",
        options=list(REGIONS.keys()),
        format_func=lambda k: f"{k} — {REGIONS[k]['label']}",
        index=list(REGIONS.keys()).index("globe"),
    )
    surfaces_allowed = REGIONS[region_key]["surfaces"]
    surface = st.selectbox("Surface", options=surfaces_allowed)

with colB:
    parameter = st.selectbox("Parameter", options=list(PARAMETERS.keys()),
                             format_func=lambda k: f"{k} — {PARAMETERS[k]}")


# Années selon le paramètre
if parameter == "pcp":
    yr_min, yr_max = 1979, 2025
else:
    yr_min, yr_max = 1950, 2025

startYear, endYear = st.slider("Year range", min_value=yr_min, max_value=yr_max,
                               value=(max(yr_min, 1880), yr_max), step=1)

noaa_url = URL_TEMPLATE.format(
    region=region_key,
    parameter=parameter,
    surface=surface,
    startYear=startYear,
    endYear=endYear,
    format="json",
)

st.caption("NOAA URL")
st.code(noaa_url, language="text")

if st.button("Générer l'œuvre", type="primary"):
    with st.spinner("Chargement des données et génération de l'œuvre..."):
        try:
            df = load_noaa_cag_service(noaa_url)

            if 'Date' in df.columns:
                date_col = 'Date'
            elif 'date' in df.columns:
                date_col = 'date'
            else:
                st.error(f"Colonnes disponibles : {df.columns.tolist()}")
                raise KeyError("Impossible de trouver une colonne de date")
            
            df['year'] = df[date_col].astype(str).str[:4].astype(int)
            df['decade'] = (df['year'] // 10) * 10
            df['year_in_decade'] = df['year'] % 10
            
            out_dir = Path("output")
            out_dir.mkdir(parents=True, exist_ok=True)
            out_path = out_dir / f"art_noaa_{region_key}_{surface}_{parameter}.png"
            
            generated_path = generate_image(
                df,
                x_col="year_in_decade",
                y_col="decade",
                value_col="value", 
                out_path=out_path,
            )
            
            st.image(str(generated_path), caption=f"{REGIONS[region_key]['label']} — {surface} — {parameter}", use_container_width=True)
            st.success(f"✅ Image générée : {generated_path}")
            
            with open(generated_path, "rb") as file:
                st.download_button(
                    label="Télécharger l'image",
                    data=file,
                    file_name=generated_path.name,
                    mime="image/png"
                )
                
        except Exception as e:
            st.error(f"Erreur lors de la génération : {str(e)}")
            st.exception(e)
