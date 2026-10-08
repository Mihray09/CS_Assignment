import matplotlib.pyplot as plt
import pandas as pd

data = "istherecorrelation.csv"

df = pd.read_csv(data, sep=';', decimal=',')

plt.figure(figsize=(8,6), dpi=150)

plt.scatter(df['WO [x1000]'], df['NL Beer consumption [x1000 hectoliter]'])

for i, year in enumerate(df["Year"]):
    plt.annotate(
        year,
        (df["WO [x1000]"][i], df["NL Beer consumption [x1000 hectoliter]"][i]),
        xytext=(4,4),
        textcoords="offset points",
    )

plt.xlabel('Number of WO students (x1000)')
plt.ylabel('NL Beer Consumption (x1000 hectoliter)')
plt.title('WO students vs. Beer consumption')


plt.tight_layout()
plt.show()
