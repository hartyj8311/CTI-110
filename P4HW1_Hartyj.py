# CTI 110
# P4HW1 - Grade list
# HartyJ
# 11/1/22

# Ask the user for 6 grades for the 6 modules
# Add them to a list.

grades = []

# grades = int(input("Enter grade for Module1:")
# grades[0] = grade1

for grade in range(6):
    grade = int(input("Enter grade: "))
    grades.append(grade)

print("The grades are: ", grades)
print("Highest grade: ", max(grades))
print("Lowest grade: ", min(grades))

# Now the average - devide the sum by the length (count)
total = sum(grades)
count = len(grades)
average = total / count
print("Total is: ", total)
print("Average is: ", average)
             
