def gradingStudents(grades):
    new_grades = []
    for marks in grades:
        if marks > 37:
            rem = marks%5
            if rem >=3: marks = 5*(int(marks/5)+1)
        new_grades.append(marks)
    for mark in new_grades:
        print(mark)


arr = [int(x) for x in '73 67 38 33'.split(" ")]
gradingStudents(arr)