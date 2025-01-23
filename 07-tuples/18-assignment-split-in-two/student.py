def split_in_two(xs):
    middle = (len(xs) + 1) // 2

    ys = xs[:middle]
    zs = xs[middle:]
    return (ys, zs)