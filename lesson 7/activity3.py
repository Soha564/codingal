print("Enter marks of 5 subjects:")
mark1 = int(input())
mark2 = int(input())
mark3 = int(input())
mark4 = int(input())
mark5 = int(input())

total = mark1 + mark2 + mark3 + mark4 + mark5
avg = total / 5

if avg >= 91 and avg <= 100:
    print("Grade:A1")
elif avg >= 81 and avg < 90:
    print("Grade: A2")
elif avg >= 71 and avg < 80:
    print("Grade: B1")
elif avg >= 61 and avg < 70:
    print("Grade: B2")
elif avg >= 51 and avg < 60:
    print("Grade: C1")
elif avg >= 41 and avg < 50:
    print("Grade: C2")
elif avg >= 31 and avg < 40:
    print("Grade: D1")
elif avg >= 21 and avg < 30:
    print("Grade: D2")
elif avg >= 11 and avg < 20:
    print("Grade: E1")
elif avg >= 1 and avg < 10:
    print("Grade: E2")
else:
    print("Unfortunately, you did not earn a grade.")