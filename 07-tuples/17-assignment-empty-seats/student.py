def empty_seats(used_seats):
    used_seats = sorted(used_seats)
    seats = 0
    for i in range(len(used_seats) - 1):
        seats += used_seats[i + 1] - used_seats[i] - 1
    return seats