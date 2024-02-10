n = int(input())
passengers = []
for _ in range(n):
    enter, exit = map(int, input().split())
    passengers.append((enter, 1))
    passengers.append((exit, -1))
passengers.sort()

t = int(input())

count = 0
for time, action in passengers:
    if time > t:
        break
    count += action

print(count)
