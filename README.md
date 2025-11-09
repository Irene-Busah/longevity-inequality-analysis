# Beyond Risk Factors: Socioeconomic Drivers of the Global Longevity–Health Gap (1990–2019)

This project investigates the global disparity between life expectancy (LE) and healthy life expectancy (HALE), focusing on how socioeconomic inequality, education, and healthcare access modify this gap.

## 🌍 Data Sources
- **Global Burden of Disease (IHME)** – HALE, DALYs, YLDs, mortality, prevalence.
- **World Bank Open Data** – GDP per capita (PPP), health expenditure, poverty, Life expectancy
- **UNDP Human Development Reports** – HDI, GII, education inequality.

## 🎯 Objectives
1. Quantify the *longevity–health gap* (LE − HALE) across countries and time (1990–2019).
2. Assess how inequality and social development influence this gap.
3. Identify clusters of countries (“health gap archetypes”) using socioeconomic and health indicators.

## 🧩 Methods
- Data cleaning and merging with pandas.
- Regression and moderation analysis (statsmodels / scikit-learn).
- Clustering (k-means, hierarchical).
- Visualization with matplotlib and seaborn.

## 📊 Repository Structure
longevity-inequality-analysis/
│
├── data/
│   ├── raw/                  # Raw CSVs (World Bank, IHME)
│   ├── processed/            # Cleaned/merged datasets
│   └── README.md             # Describe sources and variable details
│
├── notebooks/
│   ├── 01_exploration.ipynb  # EDA, correlations, visualizations
│   ├── 02_modeling.ipynb     # Regression and clustering analysis
│   └── 03_results_figures.ipynb  # Final results and plots
│
├── src/
│   ├── data_cleaning.py      # Cleaning and merging scripts
│   ├── analysis_utils.py     # Helper functions (e.g. regression models)
│   └── visualization.py      # Plot functions (maps, trends, clusters)
│
├── reports/
│   ├── paper_draft.md        # Journal-style report draft
│   ├── figures/              # Exported charts and maps
│   └── tables/               # Summary tables
│
├── environment.yml or requirements.txt
├── .gitignore
├── LICENSE
├── README.md
└── CITATION.cff (optional)

