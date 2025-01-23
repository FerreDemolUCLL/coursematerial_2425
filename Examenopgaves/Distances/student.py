import math

def read_animal_data(filename):
    animal_data = {}
    with open(filename, 'r') as file:
        for line in file:
            name, species = line.strip().split(',')
            animal_data[name] = species
    return animal_data

def read_location_data(filename):
    location_data = {}
    with open(filename, 'r') as file:
        for line in file:
            time, name, x, y = line.strip().split(',')
            if name not in location_data:
                location_data[name] = []
            location_data[name].append((time, int(x), int(y)))
    return location_data

def calculate_travelled_distance(locations):
    total_distance = 0.0
    for i in range(1, len(locations)):
        x1, y1 = locations[i-1][1], locations[i-1][2]
        x2, y2 = locations[i][1], locations[i][2]
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        total_distance += distance
    return total_distance

def most_active_animal(location_data):
    max_distance = 0
    most_active = None
    for animal, locations in location_data.items():
        distance = calculate_travelled_distance(locations)
        if distance > max_distance:
            max_distance = distance
            most_active = animal
    return most_active, max_distance

def most_lazy_animal(location_data):
    min_distance = float('inf')
    most_lazy = None
    for animal, locations in location_data.items():
        distance = calculate_travelled_distance(locations)
        if distance < min_distance:
            min_distance = distance
            most_lazy = animal
    return most_lazy, min_distance

def flag_predator_prey_contact(location_data, animal_data):
    predators = {'Lion', 'Tiger', 'Bear', 'Snake'}
    prey = {'Zebra', 'Monkey', 'Cow', 'Giraffe'}
    contacts = []

    for time in range(24):
        time_str = f"{time:02}:00"
        for animal1, locations1 in location_data.items():
            if locations1[time][0] != time_str:
                continue
            x1, y1 = locations1[time][1], locations1[time][2]
            for animal2, locations2 in location_data.items():
                if animal1 == animal2 or locations2[time][0] != time_str:
                    continue
                x2, y2 = locations2[time][1], locations2[time][2]
                distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
                if distance <= 2.0:
                    species1 = animal_data[animal1]
                    species2 = animal_data[animal2]
                    if (species1 in predators and species2 in prey) or (species1 in prey and species2 in predators):
                        contacts.append(f"Time {time_str}, {animal1} ({species1}), {animal2} ({species2}), Distance {distance:.2f}")

    with open('contacts.txt', 'w') as file:
        for contact in contacts:
            file.write(contact + '\n')

# Example usage
animal_data = read_animal_data("animals.txt")
location_data = read_location_data("locations.txt")

most_active, active_distance = most_active_animal(location_data)
print(f"Most active animal: {most_active} with distance {active_distance:.2f}")

most_lazy, lazy_distance = most_lazy_animal(location_data)
print(f"Most lazy animal: {most_lazy} with distance {lazy_distance:.2f}")

flag_predator_prey_contact(location_data, animal_data)
print("Contacts between predators and prey are saved in 'contacts.txt'.")