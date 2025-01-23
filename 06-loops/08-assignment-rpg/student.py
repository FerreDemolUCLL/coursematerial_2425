def rpg2(n_sides, goal):
    succes = 0
    total = 0

    for i in range(1, n_sides+1):
        for j in range(1, n_sides+1):
            total += 1
            if i + j >= goal:
                succes += 1
            
    return succes/total*100

def rpg3(n_sides, goal):
    succes = 0
    total = 0
    
    for i in range(1, n_sides+1):
        for j in range(1, n_sides+1):
            for k in range(1, n_sides+1):
                total += 1
                if i + j + k >= goal:
                    succes += 1
            
    return succes/total*100