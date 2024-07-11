first = int(input('Enter 1st number: '))
second = int(input('Enter 2nd number: '))
third = int(input('Enter 3rd number: '))

if first == second == third:
    print(3)
elif (first == second) or (first == third) or (second == third):
    print(2)
else:
    print(0)
