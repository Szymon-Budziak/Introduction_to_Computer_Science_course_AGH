x = float(input("Enter x: "))
eps = 0.001
total_result = 0
result1 = 1
a = -1
n = 2
starting_number = 0

while starting_number < 20:
    for i in range(2, 50):
        if i % 2 == 0:
            result1 = result1 * i
            total_result = a * ((1/result1)*(x**n)) + total_result
            a = (a) * (a)
            i += 1
            n += 2
        else:
            result1 = result1 * i
            i += 1
    starting_number += 1
print(total_result + 1)
