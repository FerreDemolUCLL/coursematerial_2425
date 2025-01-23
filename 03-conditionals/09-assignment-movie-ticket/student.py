def movie_ticket(duration, imax, student, ticket_count):
    total = 0
    if duration <= 90:
        total = 10
    elif duration <= 120:
        total = 11
    elif duration <= 150:
        total = 12
    else: total = 15

    if imax:
        total = total + (total*0.2)

    total *= ticket_count
    
    if student:
        total -= 3*ticket_count

    return total