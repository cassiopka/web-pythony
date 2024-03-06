string1 = input().strip()
string2 = input().strip()

if sorted(string1) == sorted(string2):
    print("YES")
else:
    print("NO")
