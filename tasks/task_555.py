from math import factorial

print("Enter natural number:", end=" ")
n = int(input())
for i in range(n):
    for j in range(n - i + 1):
        print(end=" ")

    for j in range(i + 1):
        # C**k_n = n!/(k!*(n-r)!)
        print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")
    print()
