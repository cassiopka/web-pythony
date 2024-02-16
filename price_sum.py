import csv

def calculate_total_spending(filename):
    adult_total = 0
    pensioner_total = 0
    child_total = 0
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            adult_total += float(row['Взрослый'])
            pensioner_total += float(row['Пенсионер'])
            child_total += float(row['Ребенок'])

    return adult_total, pensioner_total, child_total

adult_total, pensioner_total, child_total = calculate_total_spending('products.csv')
print("{:.2f} {:.2f} {:.2f}".format(adult_total, pensioner_total, child_total))
