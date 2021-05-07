last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
# Task 1
subjects = ["physics", "calculus", "poetry", "history"]
# Task 2
grades = [98, 97, 85, 88]
# Task 3
physics = [subjects[0], grades[0]]
calculus = [subjects[1], grades[1]]
poetry = [subjects[2], grades[2]]
history = [subjects[3], grades[3]]
gradebook = [physics,calculus,poetry,history]
# Task 4
#print(gradebook)
# Task 5
computer_science = ["computer science", 100]
gradebook.append(computer_science)
#print(gradebook)
# Task 6
visual_arts = ["visual arts", 93]
gradebook.append(visual_arts)
#print(gradebook)
# Task 7
visual_arts[1] = (93 + 5)
# Task 8
poetry.remove(grades[2])
# Task 9
poetry.append("Pass")
# Task 10
full_gradebook = "Last Semester: " + "\n" + str(last_semester_gradebook) + "\n\n" + "This Semester: " + "\n" + str(gradebook)

# Print Gradebook
#print(gradebook)
print(full_gradebook)