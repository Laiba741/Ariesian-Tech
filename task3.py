#importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'cereal.csv'
cereal_data = pd.read_csv('cereal.csv')
# Display basic statistics for numeric columns
print(cereal_data.describe())
 
#Analyzing key nutritional factors
top_sugar = cereal_data[['name', 'sugars']].sort_values(by='sugars', ascending=False).head(5)
print(top_sugar)

#top 5 cereals with highest sodium
top_sodium = cereal_data[['name', 'sodium']].sort_values(by='sodium', ascending=False).head(5)
print(top_sodium)

#top 5 cereals with highest caloric content
top_calories = cereal_data[['name', 'calories']].sort_values(by='calories', ascending=False).head(5)
print(top_calories)

# Plot histograms for sugar, sodium, and calorie content
fig, ax = plt.subplots(1, 3, figsize=(18, 5))
sns.histplot(cereal_data['sugars'], bins=10, kde=False, ax=ax[0])
ax[0].set_title('Sugar Distribution')

sns.histplot(cereal_data['sodium'], bins=10, kde=False, ax=ax[1])
ax[1].set_title('Sodium Distribution')

sns.histplot(cereal_data['calories'], bins=10, kde=False, ax=ax[2])
ax[2].set_title('Calorie Distribution')

plt.tight_layout()
plt.show()

# Calculate correlation matrix
correlation_matrix = cereal_data[['calories', 'sugars', 'sodium', 'fiber', 'rating']].corr()

# Plot heatmap for the correlation matrix
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix of Nutritional Factors')
plt.show()

# Plot scatter plot for sugar vs. rating
plt.figure(figsize=(8, 5))
sns.scatterplot(data=cereal_data, x='sugars', y='rating')
plt.title('Sugar Content vs. Consumer Rating')
plt.xlabel('Sugars (g)')
plt.ylabel('Rating')
plt.show()

# Group by manufacturer to find average sugar content
mfr_sugar = cereal_data.groupby('mfr')['sugars'].mean().sort_values(ascending=False)
print(mfr_sugar)

# Bar plot for manufacturers and their average sugar content
plt.figure(figsize=(10, 6))
sns.barplot(x=mfr_sugar.index, y=mfr_sugar.values)
plt.title('Average Sugar Content by Manufacturer')
plt.xlabel('Manufacturer')
plt.ylabel('Average Sugars (g)')
plt.show()