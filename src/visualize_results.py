"""
Visualizes analysis results: year-score correlation, top directors and actors, score distributions
"""
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import pandas as pd
import numpy as np

matplotlib.rc("font", family="serif")
plt.style.use("dark_background")

# get data
avg_rt_director = pd.read_csv("avg_rt_director.csv")
avg_rt_cast = pd.read_csv("avg_rt_cast.csv")
with open("year_score_correlation.txt") as f:
    data = float(f.read())
x, y = [], []
with open("year_score_x.txt") as f:
    for line in f:
        x.append(int(line))
with open("year_score_y.txt") as f:
    for line in f:
        y.append(int(line))

# year-score correlation
m, b = np.polyfit(x, y, 1)
x_graph = np.linspace(1927, 2023, num=100)
plt.title('RT Score vs Year')
plt.scatter(x, y)
plt.plot(x_graph, m*x_graph+b, color="C1", label=f"r = {data}")
plt.xlabel("Year")
plt.ylabel("RT Score")
plt.legend()
plt.savefig("year_score_correlation.png")
plt.show()

# top directors and actors
rt_d_sorted = avg_rt_director.sort_values(by=["Score"], ascending=False).head(n=10).reset_index(drop=True)
rt_d_sorted.to_csv('rt_d_sorted.csv')
print("Top 10 Directors (Avg Rt Score)")
for v in rt_d_sorted.iloc[:].values:
    print(f"- {v[0]} ({v[1]})")
    
rt_c_sorted = avg_rt_cast.sort_values(by=["Score"], ascending=False).head(n=25).reset_index(drop=True)
rt_c_sorted.to_csv('rt_c_sorted.csv')
print("Top 25 Actors (Avg Rt Score)")
for v in rt_c_sorted.iloc[:].values:
    print(f"- {v[0]} ({v[1]})")

# score distributions
sns.histplot(x="Score", data=avg_rt_director, kde=True, color="C2", edgecolor="black")
plt.title("Director RT Score Distribution")
plt.xlabel("Avg RT Score")
plt.savefig("rt_director_dist.png")
plt.show()

sns.histplot(x="Score", data=avg_rt_cast, kde=True, color="C3", edgecolor="black")
plt.title("Cast RT Score Distribution")
plt.xlabel("Avg RT Score")
plt.savefig("rt_cast_dist.png")
plt.show()
