import random
import sys
import os

print("Hello World")
name = "Derek"

# 5 data types in python

print(5/2)
print(5//2)

quote = "\"Hellow World\""
print(quote)

string1 = "abc"
multi_line_quote = '''first line
second line
third line
'''

print(multi_line_quote)
new_quote = string1 + multi_line_quote
print(new_quote)

print("%s %s %s" %('I like this',string1,new_quote))

print("first line", end = "")
print("same line")

#lists
grocery_list = ['Juice', 'Tomatoes','Potateoes']
print("first",grocery_list[0])
print(grocery_list[1:3])

medicine_list = ['Asprin','Coufgh']
to_do_list = [grocery_list,medicine_list]
print(to_do_list)
print(to_do_list[1][1])

grocery_list.insert(1,"Pickle")
print(grocery_list)
grocery_list.remove("Pickle")
print(grocery_list)
grocery_list.sort()
print(grocery_list)
del grocery_list[2]
print(grocery_list)
print(medicine_list)
to_do_list2 = grocery_list + medicine_list
print (to_do_list2)
print(len(to_do_list2))
print(len(to_do_list))
print(max(to_do_list))
print(max(to_do_list2))


#tuples cannot modify like lists
pi_tuple = (3,1,4,1,5,9)
print(pi_tuple)
new_list = list(pi_tuple)
print(new_list)
new_tuple = tuple(new_list)
print(new_tuple)
print(len(new_tuple))

#dictionaries or maps
#unique keys, cannot join dics together like lists

super_villains = {'Spiderman' : 'Peter Parker',
					'Batman' : 'Bruce Wayne',
					'superman' : 'Clark Kent',
					'Hulk' : 'Banner'}

print(super_villains)
print(super_villains['Spiderman'])
del super_villains['Spiderman']
print(super_villains)
super_villains['Batman'] = 'Master Wayne'
print(super_villains)
print(len(super_villains))
print(super_villains.get('Batman'))
print(super_villains.keys())
print(super_villains.values())

#conditionals
# if else elif

age = 21
if age > 16 :
	print('You are old enough to drive')
else :
	print('nope')
#
if age>=21 :
	print("old enough")
elif age>=16:
	print("nope")
else :
	print("what")

age = 15
if((age>=1) and (age<=18)):
	print("chal gaya bc")

#for loops
for x in range(0,10):
	print(x, ' ',end = "")

print('\n')

for y in grocery_list:
	print(y)

for x in [1,2,3,4,4]:
	print(x)

num_list = [[1,2,3],[10,20,30],[100,200,300]]

for x in range(0,3):
	for y in range(0,3):
		print(num_list[x][y], end = " ")

#while loop
random_num = random.randrange(0,100)
while(random_num!=15):
 print(random_num)
 random_num = random.randrange(0,100)

print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

i = 0
while(i<=20):
 	if(i%2 == 0):
 	 	print("Even",i)
 	print(i)
 	i = i + 1
 	
 #functions

def addNumber(fNum,lNum):
	sumNum = fNum + lNum
	return(sumNum)

print(addNumber(1,2))

age = input("Enter age")
print(age)
print("asdf")
