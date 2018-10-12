import webbrowser

class Video():

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def show_title(self):
        print("Title is = ", self.title)
    
    def show_duration(self):
        print("Duration is = ", self.duration, "hr")

class Movie(Video):
    def __init__(self, title, movie_storyline, poster_image, trailer_youtube, duration):
        Video.__init__(self, title, duration)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_title(self):
        print(self.title)

    def show_movie_storyline(self):
        print(self.storyline)

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    def show_poster_image(self):
        webbrowser.open(self.poster_image_url)

def main():
    Movie().show_title()
    Movie().show_movie_storyline()
    Movie().show_trailer()
    Movie().show_poster_image()
    Video().show_title()
    Video().show_duration()

if __name__ == "__main__":
    main()