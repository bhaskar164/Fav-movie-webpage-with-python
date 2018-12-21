#! usr/bin/python3
import webbrowser
class Movie:

    def __init__ (self, M_Title, M_Story, M_Poster, M_Trailer):
        self.title = M_Title
        self.story = M_Story
        self.poster = M_Poster
        self.trailer = M_Trailer

    def Show_Trailer(self):
        webbrowser.open(self.trailer)