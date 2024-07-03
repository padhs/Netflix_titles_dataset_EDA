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
# workflow2: random sampling for ratings and duration or we can remove those records

# visualizing missing values:
sns.heatmap(df.isnull())
plt.show()

# shows the distribution of data
sns.histplot(df)
plt.show()

