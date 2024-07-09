grades = [
    [5, 3, 3, 5, 4],
    [2, 2, 2, 3],
    [4, 5, 5, 2],
    [4, 4, 3],
    [5, 5, 5, 4, 5]
]

students = {
    'Johnny',
    'Bilbo',
    'Steve',
    'Khendrik',
    'Aaron'
}

average_grades = []

for grade in grades:
    average_grades.append(sum(grade) / len(grade))

students_list = list(students)
students_list.sort()

marks = dict(zip(students_list, average_grades))

print(marks)
