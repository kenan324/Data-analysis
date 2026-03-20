import pandas as pd

df=pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")

effect_of_BMI_SleepDisorder = pd.crosstab(df["BMI Category"], df["Sleep Disorder"])

print(effect_of_BMI_SleepDisorder)

