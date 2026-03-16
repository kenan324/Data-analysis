import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px


df = pd.read_csv('../ufo_sightings.csv', low_memory=False)

df["latitude"] = pd.to_numeric(df["latitude"], errors='coerce')
df["longitude"] = pd.to_numeric(df["longitude"], errors='coerce')
df = df.dropna(subset=['latitude', 'longitude'])

df=df.sample(15000)
plt.figure(figsize = (12,6))
plt.hexbin(
    df["latitude"],
    df["longitude"],
    gridsize=70,
    cmap='inferno',
    mincnt=1,
)
plt.colorbar(label="Sightings density")
plt.title("UFO Sightings Density Heatmap")
plt.xlabel("Latitude")
plt.ylabel("Longitude")
plt.show()



