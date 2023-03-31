def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    sorted_scores = sorted(scores, reverse = True)
    return sorted_scores[0:3]

def highest_to_lowest(scores):
    return sorted(scores, reverse = True)

def top_three(scores):
    sorted_scores = sorted(scores, reverse = True )
    if sorted_scores[0:1] == sorted_scores[0:2]:
        return f"Tie between {sorted_scores[0:1]} and {sorted_scores[0:2]}"
    