def player_movement(position, left_arrow, right_arrow, shift):
    if shift is True:
        left_arrow *= 2
        right_arrow *= 2
    position = position - left_arrow + right_arrow
    return position