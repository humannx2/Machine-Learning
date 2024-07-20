# Movie Recommendation System

This repository contains a Flask web application for a movie recommendation system. The application uses a TF-IDF vectorizer and cosine similarity to recommend movies based on the user's input.

## Features

- Clean and preprocess movie titles
- Calculate cosine similarity between movie titles
- Recommend top 5 movies based on user's input
- Simple and interactive web interface

## Requirements

- Python 3.x
- Flask
- NumPy
- Pandas
- Scikit-learn

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/humannx2/movierecommendation.git
    cd movierecommendation
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Place your `movies.csv` dataset in the root directory of the project.

## Usage

1. Run the Flask application:
    ```sh
    python app.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000/`.

3. Enter a movie title in the search bar and click 'Search' to get movie recommendations.

## Code Overview

### app.py

This is the main Flask application file. It contains the following key functions:

- `clean(title)`: Cleans the movie titles by removing non-alphanumeric characters.
- `find_recommendation(n, num_recommendations=5)`: Finds and returns movie recommendations based on the cosine similarity score.
- `search(title)`: Searches for movies that match the input title.
- `index()`: The main route that handles both GET and POST requests. It renders the `index.html` template and displays recommendations or error messages.

## templates/index.html

You need to create a HTML template for the web interface. It must contains a form for movie title input and displays the recommendations.

### datasets/movies.csv

The application requires a dataset of movies in CSV format. The dataset should have at least one column named `title` which contains the movie titles. The dataset used for this model is available under the datasets folder.

## Contributing

Feel free to open issues or submit pull requests if you have any improvements or bug fixes.

## License

This project is licensed under the MIT License.
