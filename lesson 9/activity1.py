#Write a program to check whether the student can take an exam or not. Students will be allowed only in two conditions: If they have a medical cause (‘Y’ for yes and ‘N’ for no). If yes, then they will be allowed. If No, then check attendance If attendance is above 75, then allowed; otherwise, not allowed.

medical_cause = input("Enter Medical Cause [('y' for yes and 'N' for no)]: ")
attendance = int(input("Enter your attendance: ") )

if medical_cause.lower() == 'y':
    if attendance > 75:
        print("You are allowed:")
    else:
        print("You are not allowed:")
else:
    print("You are not allowed:")
