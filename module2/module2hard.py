n = int(input('Enter the first number from 3 to 20: '))

combinations = []

for i in range(1, (n // 2) + 1):
    for j in range(i, n):
        if (n % (i + j) == 0) and (j != i):
            combinations.append(f'{i}{j}')

result = ''.join(combinations)

print(result)
