class Pokemon:
    def __init__(self, number, name, type):
        self.number = number
        self.name = name
        self.type = type
        self.name_found = False
        self.type_found = False

class Pokedex:
    def __init__(self):
        self.pokemons = {}

    def add_pokemon(self, number, name, type):
        self.pokemons[name] = Pokemon(number, name, type)

    def get_pokemon(self, name):
        if name in self.pokemons:
            return self.pokemons[name]
        else:
            raise ValueError(f"{name} is not in the Pokedex")

    def add_progress(self, name, type):
        if name in self.pokemons:
            self.pokemons[name].name_found = True
            if type is not None:
                self.pokemons[name].type_found = True
        else:
            raise ValueError(f"{name} is not in the Pokedex")

    def check_pokemon(self, name, type):
        if name not in self.pokemons:
            return f"{name} is not the name of a Pokemon"

        pokemon = self.pokemons[name]
        if pokemon.name_found:
            if type is None:
                return f"You have already found {name}"
            elif pokemon.type_found:
                return f"You already found the type for pokemon {name}, so your guesses were ignored"
            elif type != pokemon.type:
                return f"You have already found {name} - {type} is not the correct type for pokemon {name}"
            else:
                pokemon.type_found = True
                return f"You have already found {name} - Congratulations, You have found the type for pokemon {name}"
        else:
            pokemon.name_found = True
            if type is None:
                return f"Congratulations. You have found {name}"
            elif type != pokemon.type:
                return f"Congratulations. You have found {name} - {type} is not the correct type for pokemon {name}"
            else:
                pokemon.type_found = True
                return f"Congratulations. You have found {name} - Congratulations, You have found the type for pokemon {name}"

    def display_pokedex(self):
        output = "####################\n"
        for pokemon in self.pokemons.values():
            name = pokemon.name if pokemon.name_found else "???"
            type = pokemon.type if pokemon.type_found else "???"
            output += f"{pokemon.number} | {name} | {type}\n"
        output += "####################"
        return output

    def write_progress(self, filename):
        with open(filename, 'w') as file:
            for pokemon in self.pokemons.values():
                if pokemon.name_found:
                    if pokemon.type_found:
                        file.write(f"{pokemon.name},{pokemon.type}\n")
                    else:
                        file.write(f"{pokemon.name},\n")

def read_pokemon_data(filename):
    pokemons = []
    with open(filename, 'r') as file:
        for line in file:
            number, name, type = line.strip().split(',')
            pokemons.append((number, name, type))
    return pokemons

def read_progress_data(filename):
    progress = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 2:
                progress.append((parts[0], parts[1]))
            else:
                progress.append((parts[0], None))
    return progress

def play_game():
    pokedex = Pokedex()
    pokemon_data = read_pokemon_data('pokemons.txt')
    for number, name, type in pokemon_data:
        pokedex.add_pokemon(number, name, type)

    progress_data = read_progress_data('progress.txt')
    for name, type in progress_data:
        pokedex.add_progress(name, type)

    stop_game = False

    while not stop_game:
        choice = input("What do you want to do? (G)uess Pokemon - (S)how Status - (Q)uit? ").strip().upper()

        if choice == "G":
            name = input("Please enter the name of the Pokemon: ").strip()
            type = input("Please enter the type for this Pokemon (leave blank if you don't want to guess the type): ").strip()
            type = type if type else None
            print(pokedex.check_pokemon(name, type))

        elif choice == "S":
            print(pokedex.display_pokedex())

        elif choice == "Q":
            pokedex.write_progress('progress.txt')
            stop_game = True

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    play_game()