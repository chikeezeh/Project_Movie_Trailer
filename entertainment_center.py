import media  # module that contains the Movie Class
import fresh_tomatoes  # main module that builds the HTML file.

# 6 different Movie class instance are created.
moana = media.Movie("Moana", "Storyline Goes Here",
                    "https://upload.wikimedia.org/wikipedia/en/2/26/Moana_Teaser_Poster.jpg",  # noqa
                    "https://www.youtube.com/watch?v=LKFuXETZUsI")

mulan = media.Movie("Mulan", "Storyline Goes Here",
                    "https://upload.wikimedia.org/wikipedia/en/a/a3/Movie_poster_mulan.JPG",  # noqa
                    "https://www.youtube.com/watch?v=MsAniqGowKE")

pocahontas = media.Movie("Pocahontas", "Storyline Goes Here",
                         "https://upload.wikimedia.org/wikipedia/en/5/57/Pocahontasposter.jpg",  # noqa
                         "https://www.youtube.com/watch?v=9q1QF8G47oU")

aladdin = media.Movie("Aladdin", "Storyline Goes Here",
                      "https://upload.wikimedia.org/wikipedia/en/5/58/Aladdinposter.jpg",  # noqa
                      "https://www.youtube.com/watch?v=cmUZuZniouU")

cinderella = media.Movie("Cinderella", "Storyline Goes Here",
                         "https://upload.wikimedia.org/wikipedia/en/4/44/Cinderella-disney-poster.jpg",  # noqa
                         "https://www.youtube.com/watch?v=cL-RjWKtZrM")

snow_white = media.Movie("Snow White", "Storyline Goes Here",
                         "https://upload.wikimedia.org/wikipedia/en/4/49/Snow_White_1937_poster.png",  # noqa
                         "https://www.youtube.com/watch?v=5kWr9e4JN5I")
"""a list that open_movies_page method in fresh_tomatoes.py
file takes to display the contents of the movies.
"""
movies = [moana, mulan, pocahontas, aladdin, cinderella, snow_white]

fresh_tomatoes.open_movies_page(movies)
