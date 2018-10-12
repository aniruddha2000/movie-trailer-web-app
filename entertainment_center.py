import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life.",
                        "https://www.imdb.com/title/tt0114709/mediaviewer/rm3813007616",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc", "2")

avtar = media.Movie("Avatar", "A marine on a alien planel.",
                    "https://upload.wikimedia.org/wikipedia/sco/b/b0/Avatar-Teaser-Poster.jpg",
                    "https://www.youtube.com/watch?v=5PSNL1qE6VY", "2.15")

taken = media.Movie("Taken", "A former cia trying to recoect with his daughter.",
                    "https://www.google.com/search?q=taken+poster+images&tbm=isch&source=iu&ictx=1&fir=tk_yX_20cG7IyM%253A%252CbiNWp6ptTQ3e5M%252C_&usg=AFrqEzcvlBUk5-MgTBo-GmUJVL4RySKVfA&sa=X&ved=2ahUKEwiM57ffiLbdAhXEQ48KHaz9C_AQ9QEwBnoECAAQEA#imgrc=tk_yX_20cG7IyM:",
                    "https://www.youtube.com/watch?v=3Tz9tQr1Zgo", "2.35")

finding_dory = media.Movie("Finding Dory", "A fish name Dory finding his parents",
                           "https://en.wikipedia.org/wiki/File:Finding_Dory.jpg",
                           "https://www.youtube.com/watch?v=3JNLwlcPBPI", "2.65")

inception = media.Movie("Inception", "A movie on deep dreams",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=8hP9D6kZseM", "2.6")

Interstellar = media.Movie("Interstellar", "In the future, Earth is slowly becoming uninhabitable. Ex-NASA pilot Cooper, along with a team of researchers, is sent on a planet exploration mission to report which planet can sustain life.",
                           "https://www.google.com/imgres?imgurl=http://www.gstatic.com/tv/thumb/v22vodart/10543523/p10543523_v_v8_aa.jpg&imgrefurl=http://google.com/search?tbm%3Disch%26q%3DInterstellar&h=1440&w=960&tbnid=oiLKFjmOhDDUiM:&q=interstellar+storyline&tbnh=160&tbnw=106&usg=AI4_-kRduIsRiQ6N5miLRdZ8u471XfWxBw&vet=12ahUKEwipvKqluoDeAhWLtY8KHdZaDEQQ_B0wAXoECAcQCQ..i&docid=LOvrb3QP8MZCTM&itg=1&sa=X&ved=2ahUKEwipvKqluoDeAhWLtY8KHdZaDEQQ_B0wAXoECAcQCQ",
                           "https://www.youtube.com/watch?v=egkvnEYewMs", "3.12")

movies = [toy_story, avtar, taken, finding_dory]
fresh_tomatoes.open_movies_page(movies)