# NBA-Player-Clustering-with-Unsupervised-Learning


![Python](https://img.shields.io/badge/Python-3.11-blue)
![Scikit-Learn](https://img.shields.io/badge/ScikitLearn-1.4-orange)
![Status](https://img.shields.io/badge/Status-Complete-green)

## Overview

I used unsupervised machine learning to group 327 NBA players into four 
statistical archetypes using advanced stats and shot location data from the 
2025-26 season. No labels. No manual tagging. I let the data decide.

The model correctly placed all five 2026 First Team All-NBA players into 
the Star Playmakers cluster using only statistics.

🚀 **[View Live Demo](https://nba-player-clustering-with-unsupervised-learninggit-jcnwog73jb.streamlit.app/)**

---

## The Four Archetypes

| Archetype | Players | Description |
|---|---|---|
| Floor Spacers | 251 | Perimeter role players defined by shot distance and three point volume |
| Star Playmakers | 28 | Elite impact players driving offense through scoring and playmaking |
| Rim Runners | 30 | Athletic bigs dominating at the rim through dunking and paint finishing |
| Interior Enforcers | 18 | Pure paint bigs with near-zero perimeter activity |

---

## How It Works

- Scraped two Basketball Reference tables — advanced stats and shot location data
- Filtered to players with 800+ minutes to remove small sample noise
- Scaled features with RobustScaler and reduced dimensions with PCA (14 components, ~95% variance)
- Compared KMeans, Agglomerative Clustering, and DBSCAN
- Agglomerative Clustering with k=4 produced the best results (silhouette 0.307 vs KMeans 0.208)

---

## Key Finding

All five 2026 First Team All-NBA players — SGA, Jokić, Wembanyama, Dončić, 
and Cunningham — landed in Star Playmakers with zero manual intervention.

Giannis landed in Rim Runners, not Star Playmakers. His numbers are dominated 
by dunking, offensive rebounding, and paint finishing rather than perimeter 
creation. The model found a real statistical distinction that the eye test misses.

---

## Limitations & Next Steps

The model is based on one season and produces hard cluster boundaries — real 
basketball roles overlap. Next steps include testing across multiple seasons, 
trying softer clustering models like Gaussian Mixtures, and building a live 
player lookup tool.

---

## Author

Joel Hastings — M.S. Data Science, University of Colorado Boulder  
[LinkedIn](#) | [Portfolio](#)
