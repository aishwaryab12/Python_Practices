#list & tuple allows us to work with sequential data
#set are collection of unordered values without duplicates

'''
courses = ['math', 'sci', 'eng', 'History']

print(courses)
print(len(courses))
print(courses[:2])
print(courses[2:])
print(courses[-2::1])
print(courses[-1:-3:-1])

#list methods
courses.append('Art')
print(courses)

courses.insert(2,'Geo')
print(courses)

#nested list
new_courses=['ML','Data Sci']
courses.insert(0,new_courses)
print(courses)
print(courses[0])

#concatenate element of list
courses.extend(new_courses)
print(courses)

courses.remove(new_courses)
print(courses)

deleted=courses.pop()
print('deleted course is {}'.format(deleted))
print(courses)

courses.reverse()
print(courses)
sorted_list=sorted(courses)
print('sorted() function : {}'.format(courses))
print('sorted list : {}'.format(sorted_list))
#sort the list in place
courses.sort()
print('sort method : {}'.format(courses))

num=[5,6,1,7,8]
num.sort()
print('\n',num)
num.sort(reverse=True)
print('reversed list : ',num)
print('min :',min(num))
print('max :',max(num))
print('sum :', sum(num))
print('index of 7 :',num.index(7))
print('is 7 in list : ',7 in num)

courses = ['math', 'sci', 'eng', 'History']

for index,course in enumerate(courses,2):
    print(index,' :',course)

print('\nconverted list to comma separated str : ')
course_str = ','.join(courses)
print(course_str)

new_list=course_str.split(',')
print('\nnew list created from comma separated string : ',new_list)

'''
#Tuple - we can't modify / immutable

list1 = ['a', 'b', 'c', 'd']
list2=list1
print('list1 ',list1)
print('list2 ',list2)
list1[0] = 'z'
print('list1 ',list1)
print('list2 ',list2)

tup1=('a', 'b', 'c')
tup2=tup1
print('tup1 ',tup1)
print('tup2 ',tup2)

#tup1[0] = 'z' #immutable so will throw error

#Set

course_set={'Math','Sci','Eng','History','Math'}
art_set={'Design','Math'}
print('course_set : ',course_set) #output / seq of values changes with each execution
print('art set : ',art_set)
#membership test / sets are optimized for it

print('Math' in course_set)

print('set intersection : ',course_set.intersection(art_set))
print('set diff : ',course_set.difference(art_set))
print('set union : ',course_set.union(art_set))

#empty list
list1 = []
list1 = list()

tuple1 = ()
tupl1 = tuple()

set1 = {} #this isn't right its empty dict
set1 = set()

