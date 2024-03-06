n, m = map(int, input().split())
cargoes = []

for _ in range(m):
    name, weight, value = input().split()
    weight, value = int(weight), int(value)
    cargoes.append((name, weight, value))

cargoes.sort(key=lambda x: x[2] / x[1], reverse=True)

total_weight = 0
loaded_cargoes = []

for cargo in cargoes:
    if total_weight + cargo[1] <= n:
        total_weight += cargo[1]
        loaded_cargoes.append(cargo)
    else:
        remaining_weight = n - total_weight
        loaded_weight = round(remaining_weight, 2)
        loaded_value = round(cargo[2] * (loaded_weight / cargo[1]), 2)
        loaded_cargoes.append((cargo[0], loaded_weight, loaded_value))
        break

for cargo in loaded_cargoes:
    print(f"{cargo[0]} {cargo[1]} {cargo[2]}")
