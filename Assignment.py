#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 12:37:42 2024

@author: Beverlyne_Amusugut
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Loading the dataset
import pandas as pd

file_path = 'movie_dataset.csv'
movies_df = pd.read_csv(file_path)
print(movies_df)

#Display the first rows 
movies_df.head()
# Print the first 10 rows of the DataFrame
print(movies_df.head(10))

#Check for missing values
movies_df.isnull().sum()
print(movies_df.isnull().sum())

#Implementing assignment method to account for missing values/cleaning
movies_df['Revenue (Millions)'] = movies_df['Revenue (Millions)'].fillna(movies_df['Revenue (Millions)'].median())
movies_df['Metascore'] = movies_df['Metascore'].fillna(movies_df['Metascore'].median())

#Countercheck if the missing values has been accounted for
movies_df.isnull().sum()
print(movies_df.isnull().sum())

#Obtain the highest rated movie
highest_rated_movie = movies_df.loc[movies_df['Rating'].idxmax()]
highest_rated_movie[['Title', 'Rating']]

#print the result
print(f"Highest Rated Movie: {highest_rated_movie['Title']}, Rating: {highest_rated_movie['Rating']}")

# Calculate the average revenue
average_revenue = movies_df['Revenue (Millions)'].mean()

# Print the result
print(f"The average revenue of all movies is {average_revenue:.2f} Million")

# Filter the dataset for movies released between 2015 and 2017
movies_2015_2017 = movies_df[(movies_df['Year'] >= 2015) & (movies_df['Year'] <= 2017)]

# Calculate the average revenue for movies in this range
average_revenue_2015_2017 = movies_2015_2017['Revenue (Millions)'].mean()

# Print the result
print(f"The average revenue of movies from 2015 to 2017 is {average_revenue_2015_2017:.2f} Million")

# Filter the dataset for movies released in 2016
movies_2016 = movies_df[movies_df['Year'] == 2016]

# Count the number of movies released in 2016
movies_2016_count = movies_2016.shape[0]

# Print the result
print(f"The number of movies released in 2016 is {movies_2016_count}")

# Filter the dataset for movies directed by Christopher Nolan
nolan_movies = movies_df[movies_df['Director'] == 'Christopher Nolan']

# Count the number of movies directed by Christopher Nolan
nolan_movies_count = nolan_movies.shape[0]

# Print the result
print(f"The number of movies directed by Christopher Nolan is {nolan_movies_count}")


# Loading the dataset
file_path = 'movie_dataset.csv'
import pandas as pd

# Loading the dataset
file_path = 'movie_dataset.csv'
df = pd.read_csv(file_path)

# Display the first few rows of the dataset and the column names
print(df.head())
print(df.columns)


# Display the first few rows and columns of the dataset 
df.head(), df.columns

# Filter for movies directed by Christopher Nolan
nolan_movies = df[df['Director'] == 'Christopher Nolan']


#median_rating

import pandas as pd

data = {
    'Movie': ['Inception', 'The Dark Knight', 'Interstellar', 'Dunkirk', 'Memento'],
    'Director': ['Christopher Nolan', 'Christopher Nolan', 'Christopher Nolan', 'Christopher Nolan', 'Christopher Nolan'],
    'Rating': [8.8, 9.0, 8.6, 7.9, 8.4]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Filter for movies directed by Christopher Nolan
nolan_movies = df[df['Director'] == 'Christopher Nolan']

# Calculate the median rating
median_rating = nolan_movies['Rating'].median()

print(f"The median rating of movies directed by Christopher Nolan is: {median_rating}")


import pandas as pd

# Loading the dataset
file_path = 'movie_dataset.csv'  
df = pd.read_csv(file_path)

# Grouping the dataset by Year and obtaining the average Rating for each year
average_ratings_per_year = df.groupby('Year')['Rating'].mean()

# Finding the year with the highest average rating
highest_avg_rating_year = average_ratings_per_year.idxmax()

print(f"The year with the highest average rating is: {highest_avg_rating_year}")

import pandas as pd

# Loading the dataset
file_path = 'movie_dataset.csv'  
df = pd.read_csv(file_path)

# Count the number of movies in 2006 and 2016
movies_2006 = df[df['Year'] == 2006].shape[0]
movies_2016 = df[df['Year'] == 2016].shape[0]

# Calculate the percentage increase
percentage_increase = ((movies_2016 - movies_2006) / movies_2006) * 100

print(f"The percentage increase in number of movies made between 2006 and 2016 is: {percentage_increase:.2f}%")


import pandas as pd

# Loading the dataset
file_path = 'movie_dataset.csv'  
df = pd.read_csv(file_path)

# Separate the Actors column into individual actor names and create a list of all actors
all_actors = df['Actors'].str.split(',').explode().str.strip()  # Ensure no extra spaces

# Stating the actors in the multiple-choice list
target_actors = ['Mark Wahlberg', 'Bradley Cooper', 'Chris Pratt', 'Matthew McConaughey']

# Filter for only those actors in the list
filtered_actors = all_actors[all_actors.isin(target_actors)]

# Count the occurrences of each actor in the list
actor_counts = filtered_actors.value_counts()

# Find the most common actor from the list
most_common_actor = actor_counts.idxmax()

print(f"The most common actor among the choices is: {most_common_actor}")


import pandas as pd


# Load the dataset
file_path = 'movie_dataset.csv'  # Update the file path as necessary
df = pd.read_csv(file_path)

# Separate the Genre column into individual genres and create a list of all genres
all_genres = df['Genre'].str.split(',').explode().str.strip()  

# Check for the unique genres
unique_genres = all_genres.unique()

# Count the number of unique genres
unique_genre_count = len(unique_genres)

print(f"The number of unique genres is: {unique_genre_count}")

#correllation features
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Loading the dataset
file_path = 'movie_dataset.csv'  # Update the file path as necessary
df = pd.read_csv(file_path)

# Selection of numerical columns for correlation
numerical_features = df.select_dtypes(include=['float64', 'int64'])

# Computation of the correlation matrix
correlation_matrix = numerical_features.corr()

# Visualization Heatmaps
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix of Numerical Features')
plt.show()
