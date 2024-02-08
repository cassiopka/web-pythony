def find_second_highest(n, scores):
    scores_list = list(map(int, scores.split()))
    unique_scores = sorted(set(scores_list), reverse=True)
    return unique_scores[1]

n = int(input())
scores = input()
result = find_second_highest(n, scores)
print(result)