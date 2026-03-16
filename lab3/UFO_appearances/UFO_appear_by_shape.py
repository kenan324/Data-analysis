import pandas as pd
import plotly.express as px
from matplotlib import pyplot as plt

df = pd.read_csv('../ufo_sightings.csv', low_memory=False)

shape_count = df["shape"].value_counts().head(10)

shape_count.plot(kind="bar")

plt.title("Most Common UFO Shapes")
plt.xlabel("Shapes")
plt.ylabel("Number of Sightings")

plt.show()