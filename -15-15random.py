import random

random_numbers = [random.randint(-15, 15) for _ in range(10)]

squared_numbers = [num ** 2 for num in random_numbers]

print("Random Numbers:", random_numbers)
print("Squared Numbers:", squared_numbers)
