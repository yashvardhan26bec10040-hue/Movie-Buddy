# Movie Recommendation System

## 1. Problem Statement

Nowadays, there are thousands of movies available on different platforms, which makes it difficult to decide what to watch. Sometimes we like a particular movie and want to watch something similar, but searching for similar movies can take a lot of time.

To solve this problem, I decided to create a **Movie Recommendation System**. The main idea of this project is to recommend movies that are similar to a movie selected by the user.

The system uses the genres of movies to find similarities between them. It uses **CountVectorizer** to convert the genre information into numbers and **cosine similarity** to compare the movies. Based on the similarity scores, the system shows the top five recommended movies.

---

## 2. Scope of the Project

The main purpose of this project is to create a simple movie recommendation system that can be used easily by anyone.

The project currently focuses on:

* Reading movie information from a CSV file.
* Using movie genres to find similar movies.
* Converting genre information into a format that the computer can understand.
* Comparing movies using cosine similarity.
* Showing the five most similar movies to the user.
* Providing a simple interface using Streamlit.

This project is mainly developed for learning and demonstrating how a basic recommendation system works.

At the moment, the system does not have features such as user accounts, watch history, online movie streaming, or a database. These features can be added in future versions.

---

## 3. Target Users

The main users of this project are:

### Movie Viewers

People who are not sure what movie to watch can select a movie they already like and get similar movie recommendations.

### Students

Students can use this project to understand basic concepts of Python, data processing, machine learning, and recommendation systems.

### Movie Lovers

People who enjoy watching movies and want to discover movies similar to their favorites can use the system.

### Teachers and Evaluators

The project can also be used by teachers to understand and evaluate how recommendation algorithms and Python libraries have been used to develop the application.

---

## 4. High-Level Features

The main features of the Movie Recommendation System are:

### Movie Selection

The user can select a movie from a list provided by the application.

### Movie Recommendations

After selecting a movie, the system finds and displays five movies that are similar to it.

### Genre-Based Recommendations

The system mainly uses movie genres to determine how similar two movies are.

### Similarity Calculation

Cosine similarity is used to compare the movie data and find the movies that are most similar.

### Simple Web Interface

The project uses Streamlit to provide a simple and easy-to-use web interface.

### CSV Dataset

Movie information is stored in a CSV file, which is loaded and processed using Pandas.

### Future Expansion

The project can be improved later by adding features such as movie posters, ratings, trailers, user preferences, personalized recommendations, and a database.
