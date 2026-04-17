import pandas as pd
import plotly.express as px

# 1
df = pd.read_csv("Filmovi.csv")
print(df.columns)

# 2
print(df.isnull().sum())
print(df.dtypes)

# 3
print(df[df["cast"].str.contains("James McAvoy", na=False)]["title"])

# 4
print(df.sort_values(by="title")["title"])

# 5
df_genres = df.assign(genres=df["genres"].str.split(", ")).explode("genres")
genre_count = df_genres["genres"].value_counts()
print(genre_count)

fig = px.bar(genre_count.head(10), x=genre_count.head(10).index, y=genre_count.head(10).values)
fig.show()

# 6
print(df.loc[df["year_norm"].idxmin()]["title"])
print(df.loc[df["year_norm"].idxmax()]["title"])

# 7
fig = px.histogram(df, x="year_norm")
fig.show()

# 8
print(df[df["director"] != df["writers"]]["title"])

# 9
df_genres = df.assign(genres=df["genres"].str.split(", ")).explode("genres")
fig = px.scatter(df_genres, x="year_norm", y="genres",  hover_name='title', )
fig.show()
