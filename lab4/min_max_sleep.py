import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")

minSleep=df.loc[df["Sleep Duration"].idxmin()]
print(minSleep["Occupation"])


maxSleep=df.loc[df["Sleep Duration"].idxmax()]
print(maxSleep["Occupation"])

