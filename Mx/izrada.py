import pandas as pd
import plotly.express as px

#1
df = pd.read_csv("Mx/Filmovi.csv")

print(df.head(10))

#2
print("Ukupan broj redova:", len(df))

print("\nPrazne vrijednosti po kolonama:")
print(df.isnull().sum())

#3

anne_movies = df[df["cast"].str.contains("Anne Hathaway", na=False)]

print(anne_movies["title"])

#4

df["primary_genre"] = df["genres"].apply(lambda x: x.split(",")[0])

sorted_df = df.sort_values(by="primary_genre")

print(sorted_df[["title", "primary_genre"]])
#5


df["director"] = df["director"].fillna("")
directors = df["director"].str.split(",").explode()

director_counts = directors.value_counts().reset_index()
director_counts.columns = ["director", "count"]

top10 = director_counts.head(10)

fig = px.bar(top10, x="director", y="count",
             title="Top 10 režisera po broju filmova")

fig.show()


#6

oldest = df.loc[df["year_norm"].idxmin()]
newest = df.loc[df["year_norm"].idxmax()]

print("Najstariji film:", oldest["title"])
print("Najnoviji film:", newest["title"])

#7

fig = px.histogram(df, x="year_norm", nbins=20,
                   title="Distribucija filmova po godinama")

fig.show()

#8
def director_not_writer(row):
    directors = set(str(row["director"]).split(","))
    writers = set(str(row["writers"]).split(","))
    return len(directors.intersection(writers)) == 0

result = df[df.apply(director_not_writer, axis=1)]

print(result["title"])


#9

df["genre_split"] = df["genres"].str.split(",")
df_exploded = df.explode("genre_split")

fig = px.scatter(df_exploded,
                 x="year_norm",
                 y="genre_split",
                 title="Godina vs Žanr")

fig.show()
