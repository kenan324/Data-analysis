import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_csv('../ufo_sightings.csv', low_memory=False)



df["datetime"] = pd.to_datetime(df["datetime"], errors="coerce")
df["hour"] = df["datetime"].dt.hour

hour_count = df["hour"].value_counts().sort_index()


hour_count.plot()
plt.title("UFO Hours by Hour of Day")
plt.xlabel("Hour of Day")
plt.ylabel("Number of Hours")
hour_count.plot(kind="bar")

plt.show()