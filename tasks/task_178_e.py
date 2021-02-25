import math
print("-" * 60)
print("Task - find amount of elements, which satisfy the condition\n2**k < Ak < k!")
print("-" * 60)
print("Enter sequence of integer numbers by ' ':")
sequence = [int(i) for i in input().split(' ')]
result = 0
for i in range(len(sequence)):
    if 2**i < sequence[i] and sequence[i] > math.factorial(i):
        result += 1
print("Result:", result)