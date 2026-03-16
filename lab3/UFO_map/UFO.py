import pandas as pd
import plotly.express as px

df = pd.read_csv('../ufo_sightings.csv', low_memory=False)

fig = px.scatter_geo(
    df,
    lat="latitude",
    lon="longitude",
    hover_name="city",
    title = "UFO Sighting Around the world"
)

fig.show()