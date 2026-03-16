import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('../ufo_sightings.csv', low_memory=False)

city_count=df["city"].value_counts().head(10)

city_count.plot(kind="bar", figsize=(10,5))

plt.show()