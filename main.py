<<<<<<< HEAD
print("Student Grade Analytics")
print("-----------------------")

grades = [] #creates an empty list to store the grades

number_of_grades = int(input("How many grades do you want to enter? ")) #ask user how many grades they want to enter

for i in range(number_of_grades): #creates a loop that will run for the number of grades the user wants to enter
    grade = float(input("Enter a grade: "))
    grades.append(grade) #puts each grade into the list

print("Your grades:", grades)
average = sum(grades)/len(grades) #calculats the average from the number of grades in the list
print("Average grade:", round(average, 2))#keeps the average to 2 decimal places
if average >= 90:
    letter_grade = "A"
elif average >= 80:
    letter_grade = "B"
elif average >= 70:
    letter_grade = "C"
elif average >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"
print("Letter grade is:", letter_grade)

highest_grade = max(grades) #shows highest grade from list
lowest_grade = min(grades) #shows lowest grade from list
print("Highest grade:", highest_grade)
print("Lowest grade:", lowest_grade)

if average >= 70:
    status = "Passing"
else:
    status = "Not Passing"
print("Status:", status)


=======
print("Student Grade Analytics")
print("-----------------------")

grades = [] #creates an empty list to store the grades

number_of_grades = int(input("How many grades do you want to enter? ")) #ask user how many grades they want to enter

for i in range(number_of_grades): #creates a loop that will run for the number of grades the user wants to enter
    grade = float(input("Enter a grade: "))
    grades.append(grade) #puts each grade into the list

print("Your grades:", grades)
average = sum(grades)/len(grades) #calculats the average from the number of grades in the list
print("Average grade:", round(average, 2))#keeps the average to 2 decimal places
if average >= 90:
    letter_grade = "A"
elif average >= 80:
    letter_grade = "B"
elif average >= 70:
    letter_grade = "C"
elif average >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"
print("Letter grade is:", letter_grade)

highest_grade = max(grades) #shows highest grade from list
lowest_grade = min(grades) #shows lowest grade from list
print("Highest grade:", highest_grade)
print("Lowest grade:", lowest_grade)

if average >= 70:
    status = "Passing"
else:
    status = "Not Passing"
print("Status:", status)


>>>>>>> 057fbd93b8a6332d6a61f9bbf1073ee407697e77
