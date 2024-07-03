# EDA and insights from netflix dataset analysis + visualizations

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# load the dataset
df = pd.read_csv('./dataset/netflix_titles.csv'
                 , sep=',')
print(df.head())
print(df.info())
print(df.shape)

# there are some nulls
print(df.columns)
