'''
# String & methods
msg = 'day 1'

print(len(msg))
print(msg[:])
print(msg[0:2])
print(msg[:2])
print(msg[0:])

print(msg.lower())
print(msg.upper())
print(msg.count('1'))
print(msg.find('y'))
print(msg.find('aish'))
msg_new=msg.replace('day','hope')
print(msg_new)

greeting = 'good morning'
name = 'aishwarya'

print('{} ,{}'.format(greeting,name))
print(f'{greeting} ,{name.upper()}') # for python 3.6 & above

#List slicing

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#index +  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#index - [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1]

#list[start:end:step]
print (my_list[1:])
print (my_list[:-3])
print (my_list[0:5:1])
print (my_list[0:5:2])
print (my_list[10:-8:-1]) #-ve step will traverse reverse
print (my_list[ : :-1])


#string slicing

sample_url='https://www.youtube.com'

print (sample_url[::-1]) #reverse string

print (sample_url[-3:]) #print only com
print(sample_url[len(sample_url)-3:])

'''

#string formatting


