# NBA Player Archetype System — 2025-26 Season
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Scikit-Learn](https://img.shields.io/badge/ScikitLearn-1.4-orange)
![Status](https://img.shields.io/badge/Status-Live-green)

## What This Does for a Front Office

Roster construction depends on knowing what role a player fills, 
not just how many points he scores. This tool classifies every 
NBA player into one of four statistical archetypes using advanced 
stats and shot location data. No manual tagging. No subjective 
labels. The data decides.

Use it to identify lineup fit, evaluate trade targets by role, 
or find undrafted players whose statistical profile matches 
established contributors.

🚀 **[View Live Tool](https://nba-player-clustering-with-unsupervised-learninggit-jcnwog73jb.streamlit.app/)**

---

## The Finding That Matters

All five 2026 First Team All-NBA players — SGA, Jokić, 
Wembanyama, Dončić, and Cunningham — landed in the same 
archetype with zero manual intervention.

Giannis did not. His numbers are dominated by dunking, 
offensive rebounding, and paint finishing, not perimeter 
creation. The model caught a real statistical distinction 
that traditional scouting language misses. He's a Rim Runner 
masquerading as a wing star. That distinction matters when 
you're building a lineup around him.

---

## The Four Archetypes

| Archetype | Players | What They Do |
|---|---|---|
| Star Playmakers | 28 | Drive offense through scoring and creation. All-NBA tier. |
| Floor Spacers | 251 | Perimeter role players. Volume three-point shooting and shot distance define this group. |
| Rim Runners | 30 | Athletic bigs. Win at the rim through dunks and paint finishing. |
| Interior Enforcers | 18 | Pure paint bigs. Near-zero perimeter activity. |

---

## How It Was Built

- Pulled advanced stats and shot location data from Basketball 
  Reference for all players with 800+ minutes (2025-26 season)
- Scaled with RobustScaler, reduced dimensions with PCA 
  (14 components, 95% variance retained)
- Tested KMeans, Agglomerative Clustering, and DBSCAN
- Agglomerative Clustering at k=4 won on silhouette score 
  (0.307 vs KMeans 0.208)
- 327 players classified across 4 archetypes

---

## Front Office Applications

**Trade evaluation:** Know the archetype you're trading away 
before you find the replacement. Don't replace a Rim Runner 
with another Floor Spacer and wonder why your paint presence 
disappeared.

**Draft comps:** Find college players whose statistical 
profile matches an existing archetype. Identify which 
incoming rookies fill a roster need vs. which duplicate 
a role you already have.

**Lineup construction:** Build five-man units with 
intentional archetype balance rather than position labels 
that no longer reflect how the game is played.

---

## Author

Joel Hastings — M.S. Data Science, University of Colorado Boulder  
[LinkedIn](www.linkedin.com/in/joel-hastings-976bb855) | [Portfolio](#)
