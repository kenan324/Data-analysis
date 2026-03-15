import pandas as pd
import plotly.express as px
from matplotlib import pyplot as plt

df = pd.read_csv('../ufo_sightings.csv', low_memory=False)

country_count = df["country"].value_counts()

country_count.plot(kind="bar", figsize=(10,5))

plt.title("Sighting Count by Country")
plt.xlabel("Country")
plt.ylabel("Number of Sightings")

plt.show()