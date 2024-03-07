def format_name(title, first_name, last_name):
    return f"{title}. {first_name} {last_name}"

def sort_people_by_age(people):
    return sorted(people, key=lambda x: int(x[2]))

def print_sorted_names(people):
    titles = {"M": "Mr", "F": "Ms"}
    for person in sort_people_by_age(people):
        title = titles.get(person[3], "Unknown")
        formatted_name = format_name(title, person[0], person[1])
        print(formatted_name)

if __name__ == "__main__":
    N = int(input())
    people = [input().split() for _ in range(N)]

    print_sorted_names(people)
