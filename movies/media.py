import webbrowser

# Movie class as provided by Udacity's Full-Stack Nanodegree
# Movie Trailers Project: https://classroom.udacity.com/nanodegrees/nd004/

class Movie():
	def __init__ (self, movie_title, movie_storyline, 
				  poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)