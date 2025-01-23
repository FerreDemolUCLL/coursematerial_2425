def ranking_table(ranking):
    # Calculate the maximum width for each column
    max_rank_width = len(str(len(ranking)))
    max_name_width = max(len(name) for name, _ in ranking)
    max_time_width = 4  # Since times are formatted to two decimal places

    # Format each row
    rows = []
    rank = 1
    for name, time in ranking:
        rank_str = str(rank).rjust(max_rank_width)
        name_str = name.ljust(max_name_width)
        time_str = f"{time:.2f}".ljust(max_time_width)
        rows.append(f"{rank_str} {name_str} {time_str}")
        rank += 1

    # Join all rows into a single string with newline characters
    return "\n".join(rows)
