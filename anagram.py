def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

string1 = input().strip()
string2 = input().strip()

if are_anagrams(string1, string2):
    print("YES")
else:
    print("NO")
