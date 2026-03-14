import pandas as pd
import plotly.express as px


df = pd.read_csv('ufo_sightings.csv' ,low_memory=False)

df["latitude"] = pd.to_numeric(df["latitude"], errors='coerce')
df["longitude"] = pd.to_numeric(df["longitude"], errors='coerce')
df = df.dropna(subset=['latitude', 'longitude'])

df["datetime"]=pd.to_datetime(df["datetime"], errors='coerce')
df["year"]=df["datetime"].dt.year

df=df.sample(15000)

fig = px.scatter_geo(
    df,
    lon="longitude",
    lat="latitude",
    hover_name="city",
    animation_frame="year",
    projection="orthographic",
    color_discrete_sequence=["cyan"]
)


fig.update_layout(
    title= "UFO Global Sightings",
    template="plotly_dark",
    geo = dict(
        showland= True,
        landcolor= "rgb(217,217,217)",
        showcountries= True,
        showocean= True,
        oceancolor= "rgb(204,229,255)",
        bgcolor="black"
    )
)

fig.show()
