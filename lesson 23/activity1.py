# First, create a dictionary that consists of - id, name, class and subject integration of students. Then, write a program to retrieve unique entries and eliminate the rest

students = {
    'id1':{
        'name' : [ 'Sarah'],
        'class' : ['VIII'],
        'subjects' : ['Maths', 'Science']
    },
    'id2':{
        'name' : ['John'],
        'class' : ['VII'],
        'subjects' : ['English', 'Science']
    },
    'id3':{
        'name' : [ 'Sarah'],
        'class' : ['VIII'],
        'subjects' : ['Maths', 'Science']
    }
}

result = {}

for key, value in students.items():
    print(result.values())
    if value not in result.values():
        result[key] =  value
    
print(result)