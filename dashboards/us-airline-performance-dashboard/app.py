"""US Domestic Airline Flight Performance dashboard (Plotly Dash).

Two interactive reports for any year between 2005 and 2020:
  * Yearly airline performance - cancellations, flight time, diversions,
    flights per origin state (choropleth) and per destination state (treemap).
  * Yearly delay report - monthly average carrier, weather, NAS, security
    and late-aircraft delays by airline.

Run:  python app.py   then open http://127.0.0.1:8050
"""
import pandas as pd
import plotly.express as px
from dash import Dash, Input, Output, dcc, html
from dash.exceptions import PreventUpdate

DATA_URL = ("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/"
            "IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv")
YEARS = list(range(2005, 2021))

airline_data = pd.read_csv(DATA_URL, encoding="ISO-8859-1",
                           dtype={"Div1Airport": str, "Div1TailNum": str,
                                  "Div2Airport": str, "Div2TailNum": str})


def performance_figures(df):
    bar_data = df.groupby(["Month", "CancellationCode"])["Flights"].sum().reset_index()
    line_data = df.groupby(["Month", "Reporting_Airline"])["AirTime"].mean().reset_index()
    div_data = df[df["DivAirportLandings"] != 0.0]
    map_data = df.groupby("OriginState")["Flights"].sum().reset_index()
    tree_data = df.groupby(["DestState", "Reporting_Airline"])["Flights"].sum().reset_index()

    map_fig = px.choropleth(map_data, locations="OriginState", color="Flights",
                            locationmode="USA-states", color_continuous_scale="GnBu",
                            range_color=[0, map_data["Flights"].max()],
                            title="Number of flights from origin state")
    map_fig.update_layout(geo_scope="usa")

    return [
        px.treemap(tree_data, path=["DestState", "Reporting_Airline"], values="Flights",
                   color="Flights", color_continuous_scale="RdBu",
                   title="Flight count by airline to destination state"),
        px.pie(div_data, values="Flights", names="Reporting_Airline",
               title="% of diverted landings by reporting airline"),
        map_fig,
        px.bar(bar_data, x="Month", y="Flights", color="CancellationCode",
               title="Monthly flight cancellations"),
        px.line(line_data, x="Month", y="AirTime", color="Reporting_Airline",
                title="Average monthly flight time (minutes) by airline"),
    ]


def delay_figures(df):
    delays = {
        "CarrierDelay": "carrier",
        "WeatherDelay": "weather",
        "NASDelay": "National Air System",
        "SecurityDelay": "security",
        "LateAircraftDelay": "late aircraft",
    }
    figures = []
    for column, label in delays.items():
        data = df.groupby(["Month", "Reporting_Airline"])[column].mean().reset_index()
        figures.append(px.line(data, x="Month", y=column, color="Reporting_Airline",
                               title=f"Average {label} delay (minutes) by airline"))
    return figures


def dropdown(label, component_id, options, placeholder):
    return html.Div([
        html.H2(label, style={"margin-right": "2em", "font-size": 18}),
        dcc.Dropdown(id=component_id, options=options, placeholder=placeholder,
                     style={"width": "60%", "padding": "3px"}),
    ], style={"display": "flex", "align-items": "center"})


app = Dash(__name__)
app.title = "US Airline Performance"
app.layout = html.Div([
    html.H1("US Domestic Airline Flight Performance",
            style={"textAlign": "center", "color": "#503D36", "font-size": 28}),
    dropdown("Report type:", "input-type",
             [{"label": "Yearly Airline Performance Report", "value": "OPT1"},
              {"label": "Yearly Airline Delay Report", "value": "OPT2"}],
             "Select a report type"),
    dropdown("Choose year:", "input-year",
             [{"label": y, "value": y} for y in YEARS], "Select a year"),
    html.Div(id="plot1"),
    html.Div([html.Div(id="plot2"), html.Div(id="plot3")], style={"display": "flex"}),
    html.Div([html.Div(id="plot4"), html.Div(id="plot5")], style={"display": "flex"}),
])


@app.callback(
    [Output(f"plot{i}", "children") for i in range(1, 6)],
    [Input("input-type", "value"), Input("input-year", "value")],
)
def update_report(report, year):
    if report is None or year is None:
        raise PreventUpdate
    df = airline_data[airline_data["Year"] == int(year)]
    figures = performance_figures(df) if report == "OPT1" else delay_figures(df)
    return [dcc.Graph(figure=fig) for fig in figures]


if __name__ == "__main__":
    app.run(debug=False)
