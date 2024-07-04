# EDA and insights from netflix dataset analysis + visualizations

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# load the dataset
df = pd.read_csv('./dataset/netflix_titles.csv')
print(df.head())
print(df.info())
print(df.shape)

# there are some nulls
print(df.columns)
print(df.isnull().sum())

# The max null counts are in directors, cast and country of origin
# workflow: can't change the nulls in director, cast, country & date_added. It will be misleading. better to leave them as nulls
# workflow2: random sampling for ratings and duration. alternative: remove those records
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

# edit: alternative method --> scrape from google search results ?
