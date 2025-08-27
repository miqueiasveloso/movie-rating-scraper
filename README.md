# 🎬 Movie Rating Scraper

A simple Python project that scrapes movie ratings from the OMDb API and saves the results into a CSV file.
This project was built to practice Python, APIs, and data handling, and is perfect for beginners looking to showcase a practical project on GitHub.

## Project Structure

movie-rating-scraper/
- scraper.py      (Main Python script)
- movies.csv      (Output file with movie titles and ratings)
- README.md       (Project documentation)

## Features

- Fetches movie ratings from the OMDb API.
- Saves results into a CSV file (movies.csv).
- Beginner-friendly project demonstrating APIs, JSON parsing, and file handling in Python.

## Requirements

- Python 3.8+
- Requests library

Install dependencies:

pip install requests

## Usage

1. Clone this repository:
   git clone https://github.com/miqueiasveloso/movie-rating-scraper.git
   cd movie-rating-scraper

2. Run the scraper:
   python scraper.py

3. The script will generate a movies.csv file with the movie titles and ratings.

## Example Output

movies.csv:

title,year,genre,director,rating
Psycho,1960,"Drama, Horror, Mystery",Alfred Hitchcock,8.5

The Silence of the Lambs,1991,"Crime, Drama, Horror",Jonathan Demme,8.6

Halloween,1978,"Horror, Thriller",John Carpenter,7.7

The Shining,1980,"Drama, Horror",Stanley Kubrick,8.4

Rear Window,1954,"Drama, Mystery, Thriller",Alfred Hitchcock,8.5

## Notes

- You need a free API key from OMDb API (https://www.omdbapi.com/apikey.aspx).
- Replace the placeholder in scraper.py with your API key:

  API_KEY = "your_api_key_here"

## Why this project?

This project demonstrates how to:

- Work with APIs in Python.
- Handle JSON responses.
- Save and structure data into a CSV file.

It’s simple, clear, and a great way to show Python + API skills on GitHub!
