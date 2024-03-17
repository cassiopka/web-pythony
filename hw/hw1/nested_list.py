students = []
for _ in range(int(input())):
  name = input()
  score = float(input())
  students.append([name, score])
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)    
second_highest_score = sorted(set(score for name, score in students))[1]
for name, score in sorted_students:
  if score == second_highest_score:
    print(name)
