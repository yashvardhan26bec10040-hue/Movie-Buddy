# 🎬 Movie Buddy

Movie Buddy is a simple movie recommendation system made using Python and Streamlit.

The application allows users to select a movie and get recommendations based on its genre and rating.

## 📌 Project Features

- 🎬 Select a movie from the list
- 🎭 Filter movies by genre
- 🎯 Get movie recommendations
- ⭐ Display movie ratings
- 🏆 Display top-rated movies
- 🖥️ Simple Streamlit web interface

## 🛠️ Technologies Used

- Python
- Pandas
- Streamlit
- CSV

## ⚙️ How the Project Works

The project uses a CSV file containing movie names, genres, and ratings.

When the user selects a movie:

1. The program finds the selected movie.
2. It identifies the movie's genre.
3. It finds other movies belonging to the same genre.
4. The selected movie is removed from the results.
5. The remaining movies are sorted by rating.
6. The top five movies are displayed as recommendations.
7. ## 📸 Application Screenshot

![Movie Buddy Application](movie-buddy-app.png)

## 📂 Project Structure

```text

Movie-Buddy/
│
├── app.py
├── movies.csv
├── requirements.txt
└── README.md
