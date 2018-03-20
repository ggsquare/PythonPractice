import random 
import sys
import os

#Lists
'''
groceries = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']
print('First: ', groceries[0])

print(groceries[1:3]) #up to

other_events = ['Wash Car', 'Pick up Kids', 'Cash check']

to_do = [other_events, groceries] #list of lists

print(to_do[1][1])

#list functions
groceries.insert(1, 'Pickle') #groceries[1] = 'Pickle'
print(groceries)

groceries.append('Onions')
groceries.sort()
print(groceries)
groceries.reverse()
print(groceries)
del groceries[4]
print(groceries)

print(len(groceries))
print(max(groceries))
print(min(groceries))

#Tuples
pi_tup = (3,1,4,1,5,9)
new_tup = list(pi_tup)
new_list = tuple(new_tup)

#len(tuple) min(tuple) max(tuple)

#Dictionaries
villains = {'Fiddler': 'Isaax', 'Pied Piper': 'Thomas'}
print(villains['Fiddler'])

#del villains['Pied Piper']
print(len(villains))
print(villains.get('Fiddler'))
print(villains.keys()) #or values


#Conditional
age = 20

if age > 16:
    print('Drive')
else:
    print('Not old enough')

if age >= 21:
    print('Drink')
elif age >= 16:
    print('Drive')
else:
    print('WAH')

#Logical
if((age >= 1) and (age <= 18)):
    print('Minor')
elif not(age == 30):
    print('You dont get a bday')


#for
for x in range(0,10): #up to 10
    print(x)


#functions
def add(x, y):
    return x + y 

print(add(3,5))

##NEW, reading from standard in, may need to do this in interviews
print('What is your name?')
name = sys.stdin.readline()
print('Hello ' + name)
#name = input('What is yo name')

#strings
s = "Hello world"
s.capitalize()
s.find('e')
s.isalpha()
s.isalnum()
print(len(s))
s.replace('lo', 'pp')

s.strip() #Get rid of whitespace
new_list = s.split(" ")
print(new_list)

#Simple file I/o, just use pandas or numpy
test_file = open('test.txt', 'wb') #wb if want to write to file eventually
test_file.write(bytes('Write me to the file\n', 'UTF-8'))

test_file.close()
'''
#cool : os.remove('test.txt')

#OOP
class Animal:
    __name = "" #__ implies variables are private!
    __height = 0
    __weight = 0
    __sound = 0

    #constructor, self like 'this' in C++
    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound 

    def set_name(self, name):
        self.__name = name
    def get_name(self, name):
        return self.__name
    def toString(self):
        return "{} is {} cm tall and {} kg and say {}".format(self.__name, self.__height, self.__weight, self.__sound)
    
cat = Animal('Whiskers', 33, 10, 'Meow')
print(cat.toString())

#inheritance
class Dog(Animal): #THATS IT
    __owner = ""

    #overwrite Animal constructor
    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner
        super(Dog, self).__init__(name, height, weight, sound)

    #SET AND GET OWNER METHODS 





