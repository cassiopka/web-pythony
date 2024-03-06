n = int(input())
scores = input()

scores_list = list(map(int, scores.split()))
unique_scores = sorted(set(scores_list), reverse=True)
second_highest = unique_scores[1]

print(second_highest)
