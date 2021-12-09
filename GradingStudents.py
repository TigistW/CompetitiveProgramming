#https://www.hackerrank.com/challenges/grading/problem
def gradingStudents(grades):
    
    for i in range(len(grades)):
        if (grades[i]>=38 and grades[i]<=100):
            if (grades[i]%5==3 or grades[i]%5==4):
                grades[i]=grades[i]+(5-(grades[i]%5))
        else:
            continue 
    return grades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
