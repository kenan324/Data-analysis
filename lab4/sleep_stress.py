import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")

stressLevel = df["Stress Level"]

sleepQuality = df["Quality of Sleep"]

sns.regplot(x=sleepQuality, y=stressLevel)

plt.title("Stress Level and Quality of Sleep")
plt.xlabel("Stress Level")
plt.ylabel("Quality of Sleep")

plt.show()
