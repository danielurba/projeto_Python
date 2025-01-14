lloyd = {
"name" : "Lloyd",
"homework" : [90.0, 97.0, 75.0, 92.0],
"quizzes" : [88.0, 40.0, 94.0],
"tests" : [75.0, 90.0]
    }

alice = {
"name" : "Alice",
"homework" : [100.0, 92.0, 98.0, 100.0],
"quizzes" : [82.0, 83.0, 91.0],
"tests" : [89.0, 97.0],
    }

tyler = {
"name" : "Tyler",
"homework" : [0.0, 87.0, 75.0, 22.0],
"quizzes" : [0.0, 75.0, 78.0],
"tests" : [100.0, 100.0]
    }
students = [lloyd, alice, tyler]
for student in students:
    print (student["name"])
    print (student["homework"])
    print (student["quizzes"])
    print (student["tests"])

def average(numbers):
    total = sum(numbers)
    total = float(total)
    return total / len(numbers)
def getaverage(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    return 0.1 * homework + 0.3 * quizzes + 0.6 * tests
def getlettergrade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def getclassaverage(classlist):
    results = []
    for student in classlist:
        studentavg = getaverage(student)
        results.append(studentavg)
    return average(results)

students = [alice, lloyd, tyler]
media = (getclassaverage(students))
print (media)
print (getlettergrade(media))
