n, m = map(int, input().split())
array = list(map(int, input().split()))
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

mood = 0
count_a = 0
count_b = 0

for i in array:
    if i in set_a:
        count_a += 1
    if i in set_b:
        count_b += 1

mood = count_a - count_b
print(mood)