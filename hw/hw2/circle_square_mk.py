import random

def circle_square_mk(r, n):
    inside_circle = 0
    for _ in range(n):
        x = random.uniform(-r, r)
        y = random.uniform(-r, r)
        if x ** 2 + y ** 2 <= r ** 2:
            inside_circle += 1

    square = (inside_circle / n) * (4 * r ** 2)
    return square

if __name__ == "__main__":
    radius = 5
    n_experiments = 100000
    calculated_square = circle_square_mk(radius, n_experiments)
    actual_square = 3.14159 * radius ** 2  # Actual circle area formula = πr^2
    error = abs(calculated_square - actual_square)

    print(f"Calculated Square: {calculated_square}")
    print(f"Actual Square: {actual_square}")
    print(f"Error with {n_experiments} experiments: {error}")
