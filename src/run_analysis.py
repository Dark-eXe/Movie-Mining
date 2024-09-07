"""
Analyzes data from 'movies_cleaned.csv' and records the following statistics:
- Average Rotten Tomatoes Score for each director: 'avg_rt_director.csv'
- Average Rotten Tomatoes Score for each actor cast: 'avg_rt_cast.csv'
- Pearson Correlation Coefficient of year of movie release and Rotten Tomatoes Score: 'year_score_correlation.txt'
"""
import pandas as pd
import numpy as np

df = pd.read_csv('movies_cleaned.csv')

# avg_rt_director
avg_rt_director = {}
for director in set(df["Director"]):
    avg_rt_director[director] = None
d_rt = df.loc[:, ["Director", "Rotten Tomatoes Score (%)"]]
for i in range(len(d_rt)):
    director = d_rt.iloc[i]['Director']
    score = d_rt.iloc[i]['Rotten Tomatoes Score (%)']
    if not avg_rt_director[director]:
        avg_rt_director[director] = [score]
    else:
        avg_rt_director[director].append(score)
for director in avg_rt_director.keys():
    avg_rt_director[director] = np.average(avg_rt_director[director])

# avg_rt_cast
avg_rt_cast = {}
for i in range(96):
    for cast in df["Cast"].iloc[i].split(", "):
        avg_rt_cast[cast] = None
c_rt = df.loc[:, ["Cast", "Rotten Tomatoes Score (%)"]]
for i in range(96):
    for cast in c_rt.iloc[i]["Cast"].split(", "):
        if not avg_rt_cast[cast]:
            avg_rt_cast[cast] = [c_rt.iloc[i]["Rotten Tomatoes Score (%)"]]
        else:
            avg_rt_cast[cast].append(c_rt.iloc[i]["Rotten Tomatoes Score (%)"])
for cast in avg_rt_cast.keys():
    avg_rt_cast[cast] = np.average(avg_rt_cast[cast])

# year_score_correlation
year_score = df[["Year", "Rotten Tomatoes Score (%)"]]
years = np.arange(1927, 2023)
year_score_dict = {}
for y in years:
    year_score_dict[y] = [0.0]
for i in range(96):
    y = year_score.iloc[i]["Year"]
    s = year_score.iloc[i]["Rotten Tomatoes Score (%)"]
    if year_score_dict[y] == [0.0]:
        year_score_dict[y] = [s]
    else:
        year_score_dict[y].append(s)
# additional cleaning necessary for analysis: certain years are pointed to the scores of both the correct and following year
for y in years:
    if len(year_score_dict[y]) == 2:
        year_score_dict[y+1] = [year_score_dict[y][1]]
        year_score_dict[y] = year_score_dict[y][0]
    else:
        year_score_dict[y] = year_score_dict[y][0]
# create matrix to determine correlation coefficient, r
x = []
y = []
for k, v in year_score_dict.items():
    x.append(k)
    y.append(v)
r = np.corrcoef(x,y)[0][1]

# write statistics results to files
pd.DataFrame.from_dict(avg_rt_director, orient="index").to_csv("avg_rt_director.csv")
pd.DataFrame.from_dict(avg_rt_cast, orient="index").to_csv("avg_rt_cast.csv")
with open("year_score_x.txt", "w") as f:
    for point in x:
        f.write(str(point) + '\n')
with open("year_score_y.txt", "w") as f:
    for point in y:
        f.write(str(point) + '\n')
with open("year_score_correlation.txt", "w") as f:
    f.write(str(r))

print("Success! 'avg_rt_director.csv', 'avg_rt_cast.csv', 'year_score_x.txt', 'year_score_y.txt', and 'year_score_correlation.txt' created in same directory.")