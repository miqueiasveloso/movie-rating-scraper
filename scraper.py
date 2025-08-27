import requests
import pandas as pd

# Your OMDb API key
API_KEY = "4433753"

data = []

while True:
    # Ask the user for a movie name
    movie = input("🎬 Enter a movie name (or type 'quit' to finish): ")
    
    if movie.lower() == "quit":
        break  # exit the loop if user types quit

    # Build the request URL
    url = f"http://www.omdbapi.com/?t={movie}&apikey={API_KEY}"
    response = requests.get(url)
    movie_data = response.json()

    if movie_data["Response"] == "True":
        title = movie_data.get("Title", "N/A")
        year = movie_data.get("Year", "N/A")
        genre = movie_data.get("Genre", "N/A")
        director = movie_data.get("Director", "N/A")
        rating = movie_data.get("imdbRating", "N/A")

        print(f"✅ {title} ({year}) | {genre} | Directed by {director} | IMDb: {rating}")
        
        data.append({
            "title": title,
            "year": year,
            "genre": genre,
            "director": director,
            "rating": rating
        })
    else:
        print(f"❌ Movie '{movie}' not found!")
        data.append({
            "title": movie,
            "year": "N/A",
            "genre": "N/A",
            "director": "N/A",
            "rating": "N/A"
        })

# Save all results to CSV when user finishes
if data:
    df = pd.DataFrame(data)
    df.to_csv("movies.csv", index=False)
    print("\n🎉 All done! Data saved to movies.csv")
else:
    print("\n⚠️ No movies entered, nothing saved.")
