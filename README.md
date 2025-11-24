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


## 📊 Repository Structure
longevity-inequality-analysis/

├── data

    ├── raw/                  
    ├── processed/            
    └── README.md             
├── notebooks

    ├── 01_exploration.ipynb  
    ├── 02_modeling.ipynb     
    └── 03_results_figures.ipynb 
├── src

    ├── data_cleaning.py      
    ├── analysis_utils.py     
    └── visualization.py      
├── reports/

    ├── paper_draft.md        
    ├── figures/             
    └── tables/              
├── requirements.txt

├── .gitignore

├── LICENSE

└── README.md

