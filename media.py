class Movie():
    """ This Class provides a way to store movie related information
        Such as title, storyline, poster image url, and trailer.
        To create and instance of the Movie class, import media into
        your python file then create an instance by:
        variable = media.Movie(movie_title, movie_storyline,
        poster_image, trailer_youtube)
    """

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
