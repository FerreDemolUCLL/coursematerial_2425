class Location:
    def __init__(self, latitude, longitude, name, country):
        self._latitude = latitude
        self._longitude = longitude
        self.name = name
        self.country = country

    def verify_guess_is_close_enough(self, longitude, latitude):
        return abs(self._longitude - longitude) <= 1 and abs(self._latitude - latitude) <= 1

    def question_hard(self):
        return f"{self.name}:"

    def question_simple(self):
        return f"{self.name}, {self.country}:"

    def full_info(self):
        return f"{self.country}, {self.name}: ({self._latitude:.2f},{self._longitude:.2f})"


class Game:
    def __init__(self):
        self.locations = []
        self.score = 0
        self.n_games = 5

    def load_locations_from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                name, country, longitude, latitude = line.strip().split(', ')
                self.locations.append(Location(float(latitude), float(longitude), name, country))

    def ask_number_of_rounds(self):
        while True:
            try:
                n = input("How many locations would you like to try to guess? (max = 20, default = 5)\n")
                if not n:
                    return 5
                n = int(n)
                if 1 <= n <= min(20, len(self.locations)):
                    return n
            except ValueError:
                pass
            print("Invalid input. Please enter a number between 1 and 20.")

    def play_round(self, location):
        attempts = 2
        while attempts > 0:
            if attempts == 2:
                print(location.question_hard())
            else:
                print(location.question_simple())
            try:
                longitude = float(input("Longitude guess: "))
                latitude = float(input("Latitude guess: "))
                if location.verify_guess_is_close_enough(longitude, latitude):
                    self.score += 2 if attempts == 2 else 1
                    print(f"Congratulations! The answer was {location.full_info()}\n")
                    return
                else:
                    print("Try again...\n")
            except ValueError:
                print("Invalid input. Please enter valid numbers for longitude and latitude.")
            attempts -= 1
        print(f"Too bad! The answer was {location.full_info()}\n")

    def play_new_game(self, user):
        print(f"Starting a new game for {user}...\n")
        self.n_games = self.ask_number_of_rounds()
        for i in range(self.n_games):
            print(f"{self.n_games - i} locations left, your current score is {self.score}\n")
            self.play_round(self.locations[i])
        print(f"Game over! Final score for {user}: {self.score}")


# Test the program
if __name__ == "__main__":
    geoguesser = Game()
    geoguesser.load_locations_from_file("locations.txt")
    geoguesser.play_new_game("Ruben")  # Here you can obviously fill in your name