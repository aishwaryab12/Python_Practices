student = {'name': 'Ana', 'Age': 25, 'Courses': ['Math', 'Sci']}
print(student)
print(student['Courses'])
#print(student['phone']) #key error

print(student.get('phone'))
print(student.get('phone', 'Not Found'))

student['Phone'] = '555-555'
student['name'] = 'John'

print(student)

student.update({'name': 'Jimmy', 'Age':45})
print(student)

del student['Age']
print(student)

Phone = student.pop('Phone')
print(Phone)

print(student)
print(len(student))

print(student.keys())
print(student.values())

print(student.items())

for keys,values in student.items():
    print(keys,' : ',values)