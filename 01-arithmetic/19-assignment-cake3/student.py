def cake(eggs, flour, butter, sugger):
    m1 = min(eggs//5, flour//250)
    m2 = min(butter//200, sugger//250)
    return min(m1,m2)
# write your code here