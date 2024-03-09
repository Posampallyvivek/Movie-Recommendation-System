# Movie-Recommendation-System
@BHARAT INTERN providing application based knowledge <br>
Task-2 is movie recommendation system <br>
# Recommendation system
A recommendation system (or recommender system) is a class of machine learning that uses data to help predict, narrow down, and find what people are looking for among an exponentially growing number of options.
# Types Of Recommendation Systems
# 1. Collaborative Filtering
The collaborative filtering method is based on gathering and analyzing data on user’s behavior. This includes the user’s online activities and predicting what they will like based on the similarity with other users.
# 2. Content-Based Filtering
Content-based filtering methods are based on the description of a product and a profile of the user’s preferred choices. In this recommendation system, products are described using keywords, and a user profile is built to express the kind of item this user likes.
# 3. Hybrid Recommendation Systems
In hybrid recommendation systems, products are recommended using both content-based and collaborative filtering simultaneously to suggest a broader range of products to customers. This recommendation system is up-and-coming and is said to provide more accurate recommendations than other recommender systems.

# In this project we are using content based filtering in the movie recommendation system
# Major steps and its explation
# Step 1 : Data Loading and Cleaning
i. Two CSV files, 'movies' and 'credits', are read into DataFrames using Pandas.
ii. The two DataFrames are merged based on the 'title' column.
# Step 2 : Data Preprocessing
i. Columns of interest are selected from the merged DataFrame ('movies').
ii. Null values are dropped, and the DataFrame is filtered accordingly.
# Step 3 : Feature Extraction
i. The 'genres', 'keywords', 'cast', and 'crew' columns contain JSON-like strings, which are converted to Python lists using the ast.literal_eval function.
ii. Functions are defined to extract relevant information from these columns, such as movie genres, keywords, cast members, and director.
iii. Spaces are removed from certain columns, and a new column 'tags' is created by combining information from multiple columns.
# Step 4 : Text Processing
i. The 'tags' column is converted to lowercase and then stemmed using the Porter stemming algorithm.
# Step 5 : Vectorization
i. The 'tags' column is vectorized using the CountVectorizer from scikit-learn, resulting in a matrix of word counts.
# Step 6 : Cosine Similarity
i. Cosine similarity is calculated between movie vectors using cosine_similarity from scikit-learn. This results in a similarity matrix.
# Step 7 : Recommendation Function
i. A function 'recommend' is defined to recommend movies based on a given movie title.
ii. The function finds the index of the input movie in the DataFrame, sorts the similarity scores in descending order, and prints the titles of the top 5 most similar movies (excluding the input movie).
# Step 8 : Testing The Model
The 'recommend' function is then called with the movie title 'Spider-Man' to demonstrate movie recommendations based on content similarity.
