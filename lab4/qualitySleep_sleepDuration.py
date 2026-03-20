import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")

qualitySleep = df["Quality of Sleep"]

physicalActivity = df["Physical Activity Level"]

plt.bar(qualitySleep,physicalActivity)

plt.title("Sleep Health and Lifestyle")
plt.xlabel("Quality of Sleep")
plt.ylabel("Physical Activity Level")

plt.show()
