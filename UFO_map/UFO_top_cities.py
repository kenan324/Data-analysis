import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv('../ufo_sightings.csv', low_memory=False)

df["latitude"] = pd.to_numeric(df["latitude"], errors='coerce')
df["longitude"] = pd.to_numeric(df["longitude"], errors='coerce')
df = df.dropna(subset=['latitude', 'longitude'])

city_counts = df['city'].value_counts().head(10).reset_index()

top10_cites = city_counts.merge(
    df[['city', 'latitude', 'longitude']].drop_duplicates(subset=['city'])
)

# Create scatter_geo plot
fig = px.scatter_geo(
    top10_cites,
    lat="latitude",
    lon="longitude",
    text="city",
    size="count",
    projection="natural earth",
    title="Top 10 Most Frequent Cities"
)

fig.show()
