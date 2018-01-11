import webbrowser
#CLASS THAT IS SERVING AS BLUEPRINT TO EACH FAVOURITE MOVIE
class Movie():
      def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
            #CHARACTERISTICS OF EACH MOVIE OBJECT
            self.title=movie_title
            self.storyline=movie_storyline
            self.poster_image_url=poster_image
            self.trailer_youtube_url=trailer_youtube
      #FUNCTION TO DISPLAY TRAILER
      def opentrailer(self):
            webbrowser.open(self.trailer)
