# -*- coding: utf-8 -*-
import media
import fresh_tomatoes
#MY FAVOURITE MOVIES(INSTANCES OF CLASS 'Movie')
toy_story=media.Movie("Toy Story",
                "A story about a boy and his toys that come to life",
                "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                "https://www.youtube.com/watch?v=KYz2wyBy3kc"
                )
finding_dory=media.Movie("Finding Dory",
                   "A story about a forgetful blue tang,Dory, with her friends Nemo and Marlin on a search for answers about her past",
                   "https://upload.wikimedia.org/wikipedia/en/3/3e/Finding_Dory.jpg",
                   "https://www.youtube.com/watch?v=NQu-153MnGQ"
                   )
the_good_dinosaur=media.Movie("The Good Dinosaur",
                        "A story about a young Apatosaurus named Arlo, who meets an unlikely human friend while traveling through a harsh and mysterious landscape",
                        "https://upload.wikimedia.org/wikipedia/en/8/80/The_Good_Dinosaur_poster.jpg",
                        "https://www.youtube.com/watch?v=O-RgquKVTPE"
                        )
shrek=media.Movie("Shrek",
            "A story about the adventure of an ogre named Shrek,a talking donkey and who rescue a sleeping princess ",
            "https://upload.wikimedia.org/wikipedia/en/3/39/Shrek.jpg",
            "https://www.youtube.com/watch?v=W37DlG1i61s" 
            )
inside_out=media.Movie("Inside Out",
                 "A story about The film is set in the mind of a young girl where five personified emotions—Joy,Sadness,Anger,Fear and Disgust try to lead her through life as her parents move from Minnesota to San Francisco, and she has to adjust to her new surroundings.",
                 "https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg",
                 "https://www.youtube.com/watch?v=seMwpP0yeu4"
                 )
kung_fu_panda3=media.Movie("Kung Fu Panda 3",
                     "A story about a panda dragon-warrior named Po who forms an army of pandas to battle Kai's jade minions",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/e/e6/Kung_Fu_Panda_3_poster.jpg/220px-Kung_Fu_Panda_3_poster.jpg",
                     "https://www.youtube.com/watch?v=10r9ozshGVE"
                     )
moana=media.Movie("Moana",
            "A story about a strong-willed daughter of a chief of a Polynesian village, who is chosen by the ocean itself to reunite a mystical relic with a goddess",
            "https://upload.wikimedia.org/wikipedia/en/thumb/2/26/Moana_Teaser_Poster.jpg/220px-Moana_Teaser_Poster.jpg",
            "https://www.youtube.com/watch?v=LKFuXETZUsI"
            )
my_neighbour_totoro=media.Movie("My Neighbour Totoro",
                          "A story about two sisters and and their interactions with friendly wood spirits in postwar rural Japan.",
                          "https://upload.wikimedia.org/wikipedia/en/0/02/My_Neighbor_Totoro_-_Tonari_no_Totoro_%28Movie_Poster%29.jpg",
                          "https://www.youtube.com/watch?v=92a7Hj0ijLs"
                         )
only_yesterday=media.Movie("Only Yesterday",
                     "A story about a twenty-seven-year-old office worker who travels to the countryside while reminiscing about her childhood in Tokyo.",
                     "https://upload.wikimedia.org/wikipedia/en/4/46/OYpost.jpg",
                     "https://www.youtube.com/watch?v=x0ZrjocXVJ4"
                      )
#LIST OF MOVIE OBJECTS THAT WILL BE FED TO A FUNCTION IN 'fresh_tomatoes.py' FILE
movies=[toy_story,finding_dory,the_good_dinosaur,shrek,inside_out,kung_fu_panda3,moana,my_neighbour_totoro,only_yesterday]
#MOVIE LIST FED TO 'open_movies_page()' FUNCTION IN FILE 'fresh_tomatoes.py'
fresh_tomatoes.open_movies_page(movies)
