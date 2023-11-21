# Create a class movie using constructor
# -> statis variables : theatre name, location
# -> attributes : movie_name, director ,show_time,rating
# -> create 3 movie objects

class Movie:
    theatre_name = "Regal Cinemas"
    location = "East Hill, Kozhikode, Kerala 673005, India"

    def __init__(self, movie_name, director, show_time, rating):
        self.mn = movie_name
        self.dir = director
        self.st = show_time
        self.rt = rating

    def display(self):
        print()
        print(f"Theatre name:{Movie.theatre_name}")
        print(f"Location: {Movie.location}")
        print(f"Movie name:\033[95m{self.mn}\033[0m")
        print(f"Director: {self.dir}")
        print(f"Show time: {self.st}")
        print(f"Rating: {self.rt}")


mov1 = Movie(
    "Jurassic World Dominion", "Colin Trevorrow",
    "10:00 AM, 1:00 PM, 4:00 PM, 7:00 PM, 10:00 PM", "PG-13")
mov1.display()

mov1 = Movie(
    "Minions: The Rise of Gru", "Kyle Balda, Brad Bird",
    "10:30 AM, 1:30 PM, 4:30 PM, 7:30 PM, 10:30 PM", "PG")
mov1.display()

mov1 = Movie(
    "The Batman", "Matt Reeves",
    "11:00 AM, 2:00 PM, 5:00 PM, 8:00 PM", "PG-13")
mov1.display()
