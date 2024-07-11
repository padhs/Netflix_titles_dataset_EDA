# EDA and insights from netflix dataset analysis + visualizations

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# load the dataset
df = pd.read_csv('./dataset/netflix_titles.csv')
print(df.head())
# there are some nulls
print(df.info())
print(df.shape)

print(df.columns)

'''
The max null counts are in directors, cast and country of origin
workflow: can't change the nulls in director, cast, country & date_added. It will be misleading. 
better to leave them as nulls
workflow2: random sampling for ratings and duration. alternative: remove those records
'''

# visualizing missing values:
sns.heatmap(df.isnull())
plt.show()

# shows the distribution of data
sns.histplot(df)
plt.show()

# missing values -->
print(df.isnull().sum())

# Handling missing values:
'''
directions of handling: 
1. we can delete. Not so good cause a lot of missing values are there. atleast 10%
2. we can impute based on average/modes but not efficient for categoricals
3. fill the missing values by their corresponding values which are correct
We can build a web scraper that will get the director and cast if present in the netflix url
& populate the same in the dataframe in respective columns & records
'''
# edit: since the dataset is scraped from netflix, the other variables don't match records from imdb.
'''
We can't use imdb for scraping. For example the release date for 'Kota Factory' is 2021 but according to IMDB
it's actually 2019. I checked Netflix, the missing data is because of data unavailability in netflix.
This brings us to another problem. Accuracy of the data source.
Since netflix is not dependent on IMDB data, they have their own data,
this data obtained correct but it can be misleading because it doesn't represent the actual release dates rather it
represents the date mentioned in netflix
need to make further decision before analysis.
For the scope of this project, i'm leaving the data as is
'''

# edit: alternative method --> scrape from google search results ? - success. Let's fill the missing values
dir_df = pd.read_csv('./dataset/ntflx_titles_with_dirs.csv')
print(dir_df.info())

# check for duplicates
print(df['show_id'].duplicated().sum())

# types of content(distribution)
print(df['type'].value_counts())
# movie = 6131 tv shows = 2676. 3x more movies than tv shows. user insight: subscribers watch more movies than tv shows
fig = px.bar(x=df["type"].value_counts().index,
             y=df["type"].value_counts().values,
             color=df["type"].value_counts().index)

# layout with customized title, axis labels, and background colors
fig.update_layout(
    title={
        'text': "Distribution of Content Type",
        'font': {'color': 'white'}
    },
    xaxis_title={
        'text': "Content Type",
        'font': {'color': 'white'}
    },
    yaxis_title={
        'text': "Count",
        'font': {'color': 'white'}
    },
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='black',
    font=dict(color='white')
)

fig.show()

# same viz but in pie-chart form
fig = px.pie(df, values=df["type"].value_counts().values, names=df["type"].value_counts().index)

fig.update_layout(title="Distribution of Content Type", plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='black', font=dict(color='white'))

fig.show()

# distribution by release_years/ sort by release year:
print(df['release_year'].value_counts())

fig = px.bar(x=df["release_year"].value_counts().index,
             y=df["release_year"].value_counts().values,
             color=df["release_year"].value_counts().index)

fig.update_layout(
    title={
        'text': "Highest Release Years for TV Shows and Movies",
        'font': {'color': 'white'}
    },
    xaxis_title={
        'text': "Release Year",
        'font': {'color': 'white'}
    },
    yaxis_title={
        'text': "Count",
        'font': {'color': 'white'}
    },
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='black',
    font=dict(color='white')
)
'''
insight: 
Highest no. of content released in 2018. causation of peak: Covid-19, which halted film productions and caused 
late releases of movies as per the trend, the no. of movies were supposed to increase but due to economic constraints
the new trend shows a decline in no. of movies that released in the following years
'''

# viz distribution by release years grouped by movies and tv-shows
grouped_data = df.groupby(['release_year', 'type']).size().reset_index(name='count')

fig = px.bar(grouped_data, x='release_year', y='count', color='type',
             title="Highest Release Years for TV Shows and Movies",
             labels={'release_year': "Release Year", 'count': "Count", 'type': "Type"},
             color_discrete_map={'Movie': 'blue', 'TV Show': 'green'})
fig.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='black',
    font=dict(color='white')
)
highest_release_year = grouped_data[grouped_data["count"] == grouped_data["count"].max()]["release_year"].iloc[0]
highest_type = grouped_data[grouped_data["count"] == grouped_data["count"].max()]["type"].iloc[0]
print(f"The highest type on the release year {highest_release_year} is {highest_type}.")
fig.show()

