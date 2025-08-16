student = {'Name': 'Soha', 'Year' : 9, 'Age': 13, 'Address' : 'UK'}
print(student)

print("Name - ", student['Name'])
print("Year - ", student['Year'])
print("Age - ", student['Age'])
print("Address", student['Address'])
student['subjects'] = ['Science', 'Maths', 'English', 'Art']
print (student)

student['Year'] = 9   
print(student)

for key, value in student.items():
    print(key, ":", value) # Or you could type print(key) // print(value)
