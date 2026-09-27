number = int(input("Enter a number: "))
n = int(input("Enter the number of powers: "))

for power in range(1, n + 1):
    answer = number ** power
    print(number, "^", power, "=", answer)