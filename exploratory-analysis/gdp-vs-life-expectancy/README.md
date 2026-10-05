# GDP vs Life Expectancy (2000–2015)

Is a country's economic output related to how long its citizens live? An exploratory analysis of GDP and life expectancy for **Chile, China, Germany, Mexico, the USA and Zimbabwe** using World Bank and WHO data.

**[→ View the notebook](life_expectancy_gdp.ipynb)**

## Highlights
- **China's GDP grew 813%** between 2000 and 2015 — far ahead of Chile (+211%) and the USA (+75%).
- Life expectancy rose in all six countries; **Zimbabwe improved most (+32%)** after an early-2000s decline, but still has the lowest average (~50 years).
- GDP and life expectancy are **moderately positively correlated** across countries (Pearson r ≈ 0.34, Spearman ρ ≈ 0.45), and strongly correlated within each country over time.

## Techniques
Bar, line, facet and violin plots (seaborn/matplotlib) · growth-rate calculation · Pearson & Spearman correlation

## Run
```bash
jupyter notebook life_expectancy_gdp.ipynb
```
