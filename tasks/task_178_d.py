print("-" * 60)
print("Task - find amount of elements, which satisfy the condition\nAk < (Ak-1 + Ak+1) / 2.")
print("-" * 60)
print("Enter sequence of integer numbers by ' ':")
sequence = [int(i) for i in input().split(' ')]
result = 0
for i in range(1, len(sequence) - 1):
    if sequence[i] < (sequence[i-1]+sequence[i+1]) / 2:
        result += 1
print("Result:", result)
