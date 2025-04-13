import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('airbnb.csv')

# Initial Exploration
print(df.head())
print(df.info())
print("Initial Data Shape:", df.shape)
print(df.describe())

# Identify missing values and duplicates
print("Missing values:\n", df.isnull().sum())
print("Number of duplicates:", df.duplicated().sum())

# Handle missing values by filling with the average (mean)
df['reviews_per_month'].fillna(df['reviews_per_month'].mean(), inplace=True)
df['price'].fillna(df['price'].mean(), inplace=True)
df['number_of_reviews'].fillna(df['number_of_reviews'].mean(), inplace=True)

# Drop any rows where data is still missing & remove duplicates
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# After Initial Cleaning
print(df.head())
print(df.info())
print("Cleaned Data Shape:", df.shape)
print(df.describe())

#Data viaualization

df['price'].plot()
plt.ylabel('Price')
plt.title('Plot ofPrices')
#plt.show()

df.plot(kind = 'scatter',x='price', y="number_of_reviews", color="purple")
plt.title("Pricce vs Num of Reviews")
#plt.show()


# Create 2x3 subplot grid
fig, axs = plt.subplots(2, 3, figsize=(15, 10))

# 1. Price vs Frequency
axs[0, 0].hist(df['price'], bins=20, color='lightblue')
axs[0, 0].set_title("Price vs Frequency")
axs[0, 0].set_xlabel("Price")
axs[0, 0].set_ylabel("Frequency")

# 2. Number of Reviews vs Frequency
axs[0, 1].hist(df['number_of_reviews'], bins=20, color='red')
axs[0, 1].set_title("Number of Reviews vs Frequency")
axs[0, 1].set_xlabel("Number of Reviews")
axs[0, 1].set_ylabel("Frequency")

# 3. Average Price by Room Type
room_type_avg = df.groupby('room_type')['price'].mean().reset_index()
axs[0, 2].bar(room_type_avg['room_type'], room_type_avg['price'], color='lightgreen')
axs[0, 2].set_title("Average Price by Room Type")
axs[0, 2].set_xlabel("Room Type")
axs[0, 2].set_ylabel("Average Price")



# 4. Number of Listings in Each Borough (Neighborhood Group)
neighborhoods = df['neighbourhood_group'].value_counts().reset_index()
neighborhoods.columns = ['neighbourhood_group', 'count']

axs[1, 0].bar(neighborhoods['neighbourhood_group'], neighborhoods['count'], color='orange')
axs[1, 0].set_title("Listings by Neighborhood Group")
axs[1, 0].set_xlabel("Neighborhood Group")
axs[1, 0].set_ylabel("Number of Listings")

# 5. Price vs Number of Reviews (Scatter Plot)
axs[1, 1].scatter(df['price'], df['number_of_reviews'], color='blue', alpha=0.5)
axs[1, 1].set_title("Price vs. Number of Reviews")
axs[1, 1].set_xlabel("Price")
axs[1, 1].set_ylabel("Number of Reviews")


# Finalize the layout
plt.tight_layout()
plt.show()
