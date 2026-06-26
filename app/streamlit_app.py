import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# --- Load artifacts ---
@st.cache_data
def load_all():
    with open('models/assignments.pkl', 'rb') as f:
        assignments = pickle.load(f)
    with open('models/X_pca.pkl', 'rb') as f:
        X_pca = pickle.load(f)
    with open('models/df_clean.pkl', 'rb') as f:
        df = pickle.load(f)
    return assignments, X_pca, df

assignments, X_pca, df = load_all()

ARCHETYPE_COLORS = {
    'Star Playmakers':    '#E8593C',
    'Rim Runners':        '#1D9E75',
    'Interior Enforcers': '#534AB7',
    'Floor Spacers':      '#BA7517'
}

# --- Page config ---
st.set_page_config(
    page_title="NBA Player Clustering",
    page_icon="🏀",
    layout="wide"
)

# --- Header ---
st.title("🏀 NBA Player Clustering")
st.markdown(
    "Unsupervised machine learning groups 327 NBA players into four "
    "statistical archetypes using advanced stats and shot location data "
    "from the 2025-26 season."
)

# --- Sidebar ---
st.sidebar.header("Player Lookup")
player_list = sorted(assignments['Player'].tolist())
selected_player = st.sidebar.selectbox("Select a player", player_list)

# --- Player card ---
player_row = assignments[assignments['Player'] == selected_player].iloc[0]
archetype = player_row['archetype']

st.sidebar.markdown(f"### {selected_player}")
st.sidebar.markdown(f"**Position:** {player_row['Pos']}")
st.sidebar.markdown(f"**Team:** {player_row['Team']}")
st.sidebar.markdown(f"**Archetype:** {archetype}")

# --- Archetype filter ---
st.subheader("Archetype Overview")
selected_archetype = st.selectbox(
    "Filter by archetype",
    ['All'] + list(ARCHETYPE_COLORS.keys())
)

if selected_archetype == 'All':
    display_df = assignments
else:
    display_df = assignments[assignments['archetype'] == selected_archetype]

st.dataframe(
    display_df[['Player', 'Pos', 'Team', 'archetype']].reset_index(drop=True),
    use_container_width=True
)

# --- PCA scatter plot ---
st.subheader("PCA Cluster Map")

fig, ax = plt.subplots(figsize=(10, 6))

for archetype_name, color in ARCHETYPE_COLORS.items():
    mask = assignments['archetype'] == archetype_name
    ax.scatter(
