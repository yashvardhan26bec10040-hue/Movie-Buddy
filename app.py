import streamlit as st
import pandas as pd

# -----------------------------
# Load movie database
# -----------------------------

movies = pd.read_csv("movies.csv")


# -----------------------------
# Page settings
# -----------------------------

st.set_page_config(
    page_title="Movie Buddy",
    page_icon="🎬",
    layout="centered"
)


# -----------------------------
# Custom design
# -----------------------------

st.markdown(
    """
    <style>

    .stApp {
        background-color: #111111;
        color: white;
    }

    h1 {
        color: #e50914;
        text-align: center;
    }

    .description {
        text-align: center;
        color: #cccccc;
        font-size: 18px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# -----------------------------
# Main title
# -----------------------------

st.title("🎬 Movie Buddy")

st.markdown(
    '<p class="description">'
    'Find movies you might enjoy based on your favorite genre.'
    '</p>',
    unsafe_allow_html=True
)

st.write("")


# -----------------------------
# Genre filter
# -----------------------------

genres = ["All"] + sorted(movies["genre"].unique().tolist())

selected_genre = st.selectbox(
    "🎭 Select a genre",
    genres
)


# -----------------------------
# Movie selection
# -----------------------------

if selected_genre == "All":

    movie_list = movies["title"]

else:

    movie_list = movies[
        movies["genre"] == selected_genre
    ]["title"]


movie = st.selectbox(
    "🎥 Select a movie",
    movie_list
)

# -----------------------------
# Recommendation
# -----------------------------

if st.button("🎯 Recommend Movies"):

    selected_movie = movies[
        movies["title"] == movie
    ].iloc[0]

    selected_genre = selected_movie["genre"]

    recommendations = movies[
        (movies["genre"] == selected_genre) &
        (movies["title"] != movie)
    ].sort_values("rating", ascending=False)

    st.divider()

    st.subheader("🎬 Your Movie")

    st.write("**Movie:**", movie)
    st.write("**Genre:**", selected_genre)
    st.write("**Rating:** ⭐", selected_movie["rating"])

    st.subheader("🍿 You Might Also Like")

    for _, movie_data in recommendations.head(5).iterrows():

            st.write(
                "🎬",
                movie_data["title"],
                "| Genre:",
                movie_data["genre"],
                "| ⭐ Rating:",
                movie_data["rating"]
            )

else:

        st.info(
            "Sorry, we couldn't find similar movies."
        )


# -----------------------------
# About section
# -----------------------------

st.divider()

st.subheader("ℹ️ About This Project")

st.write(
    "Movie Buddy is a simple movie recommendation system "
    "created using Python, Pandas and Streamlit. "
    "It recommends movies that have the same genre as "
    "the movie selected by the user."
)
