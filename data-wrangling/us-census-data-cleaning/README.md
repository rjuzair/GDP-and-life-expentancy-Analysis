# US Census Data Cleaning

Combines state-level census extracts split across many CSV files into a single tidy dataset.

## Cleaning steps
- Concatenate `states*.csv` files with `glob` + `pd.concat`
- Strip `$` and `,` from **Income** and convert to numeric
- Split the combined **GenderPop** column (`"2341093M_2489527F"`) into **Men** and **Women**
- Impute missing **Women** values as `TotalPop − Men`
- Remove duplicate state rows
- Convert race/ethnicity percentages (`"17.5%"`) to numbers and impute gaps with the column mean
- Visualise income vs female population and the distribution of each race/ethnicity share

```bash
python analysis.py   # expects data/states0.csv … data/statesN.csv
```
