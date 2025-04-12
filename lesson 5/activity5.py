# Simulates a student management system to check if a student is eligible for an exam based on their attendance, grades, and whether they have completed assignments.

total_classes = 120
classes_attended = int(input("Please enter the amount of classes you have atttended:"))
assignment_completed = int(input("Please enter the number of assignments completed to dat (out of 10)"))
average_grade_percent = float(input("Please enter your average grade percentage:"))

attendance_percent = (classes_attended / total_classes) * 100
attendance_percent = round(attendance_percent, 2)

if attendance_percent >= 75:
    print(f"Your attendance is {attendance_percent}%. you have the correct attendance requirements.")
else:
    print(f"Your attendance is {attendance_percent}%. you have not met the correct attendance requirements.")
    make_up_classes = total_classes - classes_attended
    print(f"You need to attend {make_up_classes} more classes to meet the correct attendance requirements.")

if assignment_completed >= 8:
    print(f"You have submitted {assignment_completed} assignments, which meets the requirement for your exam.")
else:
    print(f"You have submitted {assignment_completed} assignments. However you needed to complete a minimum of 8 assignments to be elegible for the exam.")

if average_grade_percent >= 60:
    print(f"Your average grade is {average_grade_percent}%. You have met the average grade requirement.")
else:
    print(f"Your average grade is {average_grade_percent}%. You needed to have a minimum of 60% as your average grade.")

# Final Decision
if attendance_percent >= 75 and assignment_completed >= 8 and average_grade_percent >= 60:
    print("Congratulations, you have met all the requirements and are now elegible for the exam.")
else:
    print("Sorry, you have not met all the requirements meaning you are not elegible for the exam. Please try to improve your attendance, assignments or grades. ")