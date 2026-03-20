import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")

female=df[(df["Gender"] == "Female") & (df["Stress Level"] == 7)]

print(female)



