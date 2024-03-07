def compute_average_scores(scores):
    transposed_scores = list(zip(*scores))
    averages = [sum(student_scores) / len(student_scores) for student_scores in transposed_scores]
    return tuple(round(avg, 1) for avg in averages)

if __name__ == '__main__':
    n, x = map(int, input().split())
    scores = []
    for _ in range(x):
        scores.append(tuple(map(float, input().split())))
    average_scores = compute_average_scores(scores)
    for score in average_scores:
        print(score)
