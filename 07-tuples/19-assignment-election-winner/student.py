def election_winner(votes):
    if len(votes) == 0:
        return None
    
    votes = sorted(votes)
    current_vote = votes[0]
    current_count = 1
    max_vote = current_vote
    max_count = current_count

    for i in range(1, len(votes)):
        if votes[i] == current_vote:
            current_count += 1
        else:
            if current_count > max_count:
                max_vote = current_vote
                max_count = current_count
            current_vote = votes[i]
            current_count = 1

    if current_count > max_count:
        max_vote = current_vote
        max_count = current_count

    return max_vote