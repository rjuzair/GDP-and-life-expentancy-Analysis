# US Domestic Airline Flight Performance Dashboard

An interactive **Plotly Dash** web app for monitoring US domestic airline performance (2005–2020).

## Reports
**Yearly airline performance** — for a selected year:
- Monthly cancellations by cancellation category (bar)
- Average flight time by airline (line)
- Share of diverted landings by airline (pie)
- Flights per origin state (US choropleth)
- Flights per destination state and airline (treemap)

**Yearly delay statistics** — monthly average carrier, weather, National Air System, security and late-aircraft delays by airline.

## Run
```bash
pip install -r requirements.txt
python app.py          # open http://127.0.0.1:8050
```
The data (a sample of the BTS *Reporting Carrier On-Time Performance* dataset) is loaded directly from IBM Skills Network storage.

`dashboard_walkthrough.ipynb` contains the original design notes and requirements.
