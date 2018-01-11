# -*- coding: utf-8 -*-
import media
import fresh_tomatoes
# MY FAVOURITE MOVIES(INSTANCES OF CLASS 'Movie')
toy_story = media.Movie("Toy Story",
                        "Story about a boy and his toys that come to life",
                        "https://goo.gl/jmrzhq",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc"
                        )
finding_dory = media.Movie("Finding Dory",
                           "Adventure of a forgetful fish & friends",
                           "https://goo.gl/zFJDNP",
                           "https://www.youtube.com/watch?v=NQu-153MnGQ"
                           )
the_good_dinosaur = media.Movie("The Good Dinosaur",
                                "Adventure of an Apatosaurus & a human",
                                "https://goo.gl/RSP6T7",
                                "https://www.youtube.com/watch?v=O-RgquKVTPE"
                                )
shrek = media.Movie("Shrek",
                    "Adventure of an ogre,a donkey & a princess",
                    "https://goo.gl/TCm1KA",
                    "https://www.youtube.com/watch?v=W37DlG1i61s"
                    )
inside_out = media.Movie("Inside Out",
                         "Story of the mind of a young girl",
                         "https://goo.gl/naNXv8",
                         "https://www.youtube.com/watch?v=seMwpP0yeu4"
                         )
kung_fu_panda3 = media.Movie("Kung Fu Panda 3",
                             "Story of a panda declared as a warrior",
                             "https://goo.gl/9JH5Bc",
                             "https://www.youtube.com/watch?v=10r9ozshGVE"
                             )
moana = media.Movie("Moana",
                    "Adventure of a Polynesian village's chief's daughter",
                    "https://goo.gl/bnzjnB",
                    "https://www.youtube.com/watch?v=LKFuXETZUsI"
                    )
my_neighbour_totoro = media.Movie("My Neighbour Totoro",
                                  "Story about two sisters & wood spirits",
                                  "https://goo.gl/scpoyM",
                                  "https://www.youtube.com/watch?v=92a7Hj0ijLs"
                                  )
only_yesterday = media.Movie("Only Yesterday",
                             "Story of a woman's past & present",
                             "https://goo.gl/wFbDdt",
                             "https://www.youtube.com/watch?v=x0ZrjocXVJ4"
                             )
# LIST OF MOVIE OBJECTS FED TO 'fresh_tomatoes.py'
movies = [toy_story, finding_dory, the_good_dinosaur, shrek, inside_out,
          kung_fu_panda3, moana, my_neighbour_totoro, only_yesterday]
# MOVIE LIST FED TO 'open_movies_page()' FUNCTION IN FILE 'fresh_tomatoes.py'
fresh_tomatoes.open_movies_page(movies)
