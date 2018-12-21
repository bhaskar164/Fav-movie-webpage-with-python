#! usr/bin/python3
from Movie_project import fresh_tomatoes
from Movie_project.Media import Movie
#1st Movie
toystory = Movie("Toy Story",
                 "Toys got real",
                 "https://upload.wikimedia.org/wikipedia/en/7/78/Toy_Story_4_teaser_poster.jpg",
                 "https://www.youtube.com/watch?v=LDXYRzerjzU")

#toystory.Show_Trailer()
#print(toystory.story)
#2nd Movie
HTTDrgn = Movie("How To Train Your Dragon",
                "Dragons under Training",
                "https://m.media-amazon.com/images/M/MV5BMjIwMDIwNjAyOF5BMl5BanBnXkFtZTgwNDE1MDc2NTM@._V1_SY1000_CR0,0,631,1000_AL_.jpg",
                "https://www.youtube.com/watch?v=SkcucKDrbOI")
#HTTDrgn.Show_Trailer()
#3rd Movie
HarryPotter = Movie("Harry Potter and Deathly Hallows Part-2",
                    "Harry Potter is Fighting with voldermort",
                    "http://www.gstatic.com/tv/thumb/v22vodart/7953526/p7953526_v_v8_bc.jpg",
                    "https://youtu.be/5NYt1qirBWg")
#4th Movie
AquaMan = Movie("Aqua Man",
                "King Of Ocean Saving His World",
                "https://pbs.twimg.com/media/Dsdlbj3U4AAJoO7.jpg",
                "https://www.youtube.com/watch?v=WDkg3h8PCVU")
#5th Movie
WonderWoman = Movie("Wonder Woman",
                    "Wonder Woman saving the world from threats",
                    "http://www.gstatic.com/tv/thumb/v22vodart/12543972/p12543972_v_v8_ab.jpg",
                    "https://www.youtube.com/watch?v=VSB4wGIdDwo")
#6th Movie
Avengers = Movie("Avengers:Infinity War"
                 ,"Avengers come together to Save the world From Thanos"
                 ,"http://www.gstatic.com/tv/thumb/v22vodart/12863030/p12863030_v_v8_ae.jpg",
                 "https://www.youtube.com/watch?v=6ZfuNTqbHE8")
#7th Movie
Thor = Movie("Thor Ragnarok",
             "Thor's Kingdom under attack",
             "https://upload.wikimedia.org/wikipedia/en/7/7d/Thor_Ragnarok_poster.jpg",
             "https://www.youtube.com/watch?v=ue80QwXMRHg")
#8th Movie
BlackPanther = Movie("Black Panther",
                     "Introducing Black Panther the new avenger and his kingdom",
                     "http://www.gstatic.com/tv/thumb/v22vodart/12878741/p12878741_v_v8_ac.jpg",
                     "https://www.youtube.com/watch?v=xjDjIWPwcPU")
Antman = Movie("Ant Man and Wasp",
                     "Ant Man Fighting With crimes along with wasp",
                     "http://www.gstatic.com/tv/thumb/v22vodart/13798222/p13798222_v_v8_af.jpg",
                     "https://www.youtube.com/watch?v=UUkn-enk2RU")

movies = [toystory,HTTDrgn,HarryPotter,AquaMan,WonderWoman,Avengers,Thor,BlackPanther,Antman]
fresh_tomatoes.open_movies_page(movies)