# from random import randrange
# 
# class Pet():
#     boredom_decrement = 4
#     hunger_decrement = 6
#     boredom_threshold = 5
#     hunger_threshold = 10
#     sounds = ['Gbuh']
# 
#     def __int__(self, name='Rex', pet_type='dog'):
#         self.name = name
#         self.hunger = randrange(self.hunger_threshold)
#         self.boredom = randrange(self.boredom_threshold)
#         self.sounds = self.sounds[:]
#         self.pet_type = pet_type
# 
#     def clock_tick(self):
#         self.boredom += 1
#         self.hunger += 1
# 
#     def mood(self):
#         if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
#             if self.pet_type == 'dog':
#                 return 'happy... Bguh'
#             elif self.pet_type == 'cat':
#                 return 'Happy... Meaaw'
#             else:
#                 return 'unknown animal'
#         elif self.hunger > self.hunger_threshold:
#             if self.pet_type == 'dog':
#                 return 'hungry... Gbuh'
#             elif self.pet_type == 'cat':
#                 return 'hungry... meaaw'
#             else:
#                 return 'unknown animal'
#         else:
#             return 'bored'
# 
#     def __str__(self):
#         state = 'Im ' + self.name + '.'
#         state += ' I feel ' + self.mood() + '.'
#         return state
# 
#     def hi(self):
#         print(self.sounds[randrange(len(self.sounds))])
#         self.reduce_boredom()
#         return self.reduce_boredom()
# 
#     def teach(self, word):
#         self.sounds.append(word)
#         self.reduce_boredom()
#         return self.reduce_boredom(), self.sounds
# 
#     def feed(self):
#         self.reduce_hunger()
#         return self.reduce_hunger()
# 
#     def reduce_hunger(self):
#         self.hunger = max(0, self.hunger - self.hunger_decrement)
#         return self.hunger
# 
#     def reduce_boredom(self):
#         self.boredom = max(0, self.boredom - self.hunger_decrement)
#         return self.boredom
# 
# pet1 = Pet()
# print(pet1.hi())


# import sys
# sys.setExecutionLimit(60000)
# from random import randrange
#
# class Pet(object):
#     boredom_decrement = 4
#     hunger_decrement = 6
#     boredom_threshold = 5
#     hunger_threshold = 10
#     sounds = ['Mrrp']
#     def __init__(self, name = "Kitty"):
#         self.name = name
#         self.hunger = randrange(self.hunger_threshold)
#         self.boredom = randrange(self.boredom_threshold)
#         self.sounds = self.sounds[:]  # copy the class attribute, so that when we make changes to it, we won't affect the other Pets in the class
#
#     def clock_tick(self):
#         self.boredom += 1
#         self.hunger += 1
#
#     def mood(self):
#         if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
#             return "happy"
#         elif self.hunger > self.hunger_threshold:
#             return "hungry"
#         else:
#             return "bored"
#
#     def __str__(self):
#         state = "     I'm " + self.name + ". "
#         state += " I feel " + self.mood() + ". "
#         # state += "Hunger %d Boredom %d Words %s" % (self.hunger, self.boredom, self.sounds)
#         return state
#
#     def hi(self):
#         print(self.sounds[randrange(len(self.sounds))])
#         self.update_boredom()
#
#     def teach(self, word):
#         self.sounds.append(word)
#         self.update_boredom()
#
#     def feed(self):
#         self.update_hunger()
#
#     def update_hunger(self):
#         self.hunger = max(0, self.hunger - self.hunger_decrement)
#
#     def update_boredom(self):
#         self.boredom = max(0, self.boredom - self.boredom_decrement)
#
# class Cat(Pet):
#     sounds = ['Meow']
#
#     def mood(self):
#         if self.hunger > self.hunger_threshold:
#             return "hungry"
#         if self.boredom <2:
#             return "grumpy; leave me alone"
#         elif self.boredom > self.boredom_threshold:
#             return "bored"
#         elif randrange(2) == 0:
#             return "randomly annoyed"
#         else:
#             return "happy"
#
# class Dog(Pet):
#     sounds = ['Woof', 'Ruff']
#
#     def mood(self):
#         if (self.hunger > self.hunger_threshold) and (self.boredom > self.boredom_threshold):
#             return "bored and hungry"
#         else:
#             return "happy"
#
#     def feed(self):
#         Pet.feed(self)
#         print("Arf! Thanks!")
#
# class Bird(Pet):
#     sounds = ["chirp"]
#     def __init__(self, name="Kitty", chirp_number=2):
#         Pet.__init__(self, name) # call the parent class's constructor
#         # basically, call the SUPER -- the parent version -- of the constructor, with all the parameters that it needs.
#         self.chirp_number = chirp_number # now, also assign the new instance variable
#
#     def hi(self):
#         for i in range(self.chirp_number):
#             print(self.sounds[randrange(len(self.sounds))])
#         self.update_boredom()
#
# class Lab(Dog):
#     def fetch(self):
#         return "I found the tennis ball!"
#
#     def hi(self):
#         print(self.fetch())
#         print(self.sounds[randrange(len(self.sounds))])
#
# class Poodle(Dog):
#     def dance(self):
#         return "Dancin' in circles like poodles do."
#
#     def hi(self):
#         print(self.dance())
#         Dog.hi(self)
#
# def whichone(petlist, name):
#     for pet in petlist:
#         if pet.name == name:
#             return pet
#     return None # no pet matched
#
# pet_types = {'dog': Dog, 'lab': Lab, 'poodle': Poodle, 'cat': Cat, 'bird': Bird}
# def whichtype(adopt_type="general pet"):
#     return pet_types.get(adopt_type.lower(), Pet)
#
# def play():
#     animals = []
#
#     option = ""
#     base_prompt = """
#         Quit
#         Adopt <petname_with_no_spaces> <pet_type - choose dog, cat, lab, poodle, bird, or another unknown pet type>
#         Greet <petname>
#         Teach <petname> <word>
#         Feed <petname>
#
#         Choice: """
#     feedback = ""
#     while True:
#         action = input(feedback + "\n" + base_prompt)
#         feedback = ""
#         words = action.split()
#         if len(words) > 0:
#             command = words[0]
#         else:
#             command = None
#         if command == "Quit":
#             print("Exiting...")
#             return
#         elif command == "Adopt" and len(words) > 1:
#             if whichone(animals, words[1]):
#                 feedback += "You already have a pet with that name\n"
#             else:
#                 # figure out which class it should be
#                 if len(words) > 2:
#                     Cl = whichtype(words[2])
#                 else:
#                     Cl = Pet
#                 # Make an instance of that class and append it
#                 animals.append(Cl(words[1]))
#         elif command == "Greet" and len(words) > 1:
#             pet = whichone(animals, words[1])
#             if not pet:
#                 feedback += "I didn't recognize that pet name. Please try again.\n"
#                 print()
#             else:
#                 pet.hi()
#         elif command == "Teach" and len(words) > 2:
#             pet = whichone(animals, words[1])
#             if not pet:
#                 feedback += "I didn't recognize that pet name. Please try again."
#             else:
#                 pet.teach(words[2])
#         elif command == "Feed" and len(words) > 1:
#             pet = whichone(animals, words[1])
#             if not pet:
#                 feedback += "I didn't recognize that pet name. Please try again."
#             else:
#                 pet.feed()
#         else:
#             feedback+= "I didn't understand that. Please try again."
#
#         for pet in animals:
#             pet.clock_tick()
#             feedback += "\n" + pet.__str__()
#
# play()

def testEqual_2(a, b):
    if a == b:
        print('Pass')
    else:
        print(f'Fail, expected {a} but got {b}')


def testEqual(actual, expected, places=5):
    '''
    Does the actual value equal the expected value?
    For floats, places indicates how many places, right of the decimal, must be correct
    '''
    if isinstance(expected, float):
        if abs(actual - expected) < 10 ** (-places):
            print('Pass')
            return True
    else:
        if actual == expected:
            print('Pass *** RuneStone')
            return True
    print(f'Test Failed: expected {actual} but got {expected}')
    return False


def square(x):
    return x * x

# my_test = testEqual(square(9), 100)
# my_test_2 = testEqual_2(square(-10), 100)
# my_test_3 = testEqual_2(square(1.5), 2.25)
# my_test_4 = testEqual_2(square(0), 0)
# my_test_5 = testEqual_2(sorted([1, 7, 4]), [1, 4, 7])
# my_test_6 = testEqual_2(sorted([1, 7, 4], reverse=True), [7, 4, 1])
# my_test_7 = testEqual(sorted([1, 7, 4], reverse=False), [1, 4, 7])

# def distance(x1, y1, x2, y2):
#     distance_x= x2 - x1
#     distance_y = y2 - y1
#     distance_squared = distance_x**2 + distance_y**2
#     result = distance_squared**0.5
#     return result
# print(distance(0,0 ,1,1))
# print(2**0.5)
# assert distance(0,0 ,1,1) == 2**0.5
#
# assert distance(1, 2, 1, 2) == 0
# assert distance(1,2, 4,6) == 5

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

# r = Rectangle(8, 4)
# print('Area: ', r.get_area())
# print('Width: ', r.width)
# print('Height: ', r.height)
# assert r.get_area() == 32
# assert r.height == 4

# import unittest
# class TestGetAreaRectangle(unittest.TestCase):
#     def runTest(self):
#         rectangle = Rectangle(8, 4)
#         self.assertEqual(rectangle.get_area(), 32, 'incorrect')

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def distance_from_origin(self):
#         return ((self.x ** 2) + (self.y ** 2)) ** 0.5
#
#     def move(self, dx, dy):
#         self.x = self.x + dx
#         self.y = self.y + dy
#
#     def __str__(self):
#         return f'{self.x}, {self.y}'
#
# p = Point(3, 4)
# assert p.x == 3
# assert p.y == 4
#
# assert p.distance_from_origin() == 5.0
#
# p.move(2, 1)
# print(p)
# print(p.distance_from_origin())
# assert p.distance_from_origin() == 7.0710678118654755
#
# try:
#     for i in range(5):
#         print(1.0 / (3-i))
# except Exception as error_inst:
#     print("Got an error", error_inst)


import pandas as pd

# info = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'],
#       'Salary':[100000, 80000, 50000, 60000]}
# my_data_frame = pd.DataFrame(info)
# print(my_data_frame, '\n')
#
# id_info = my_data_frame[['ID', 'Name']]

# print(id_info)

new_data = {'Name': ['David', 'Alex', 'Jessy', 'Peter'], 'Age': [21, 40, 24, 30], 'Country': ['Brazil', 'Egypt', 'Romania', 'Thailand'], 'Course': ['Python', 'JavaScript', 'C++', 'Java'], 'Marks': [79, 89, 90, 78]}
new_data_1 = pd.DataFrame(new_data)
print(new_data_1)
a = new_data_1[['Name', 'Age']]
b = new_data_1['Name'] # Series use one pair of []
# print(a)
# print(b)
# loc[row_label, column_label]
c = new_data_1.loc[0, 'Name']
# xx = new_data_1.loc['Alex', 'Course']
# print(xx)
# print(c)
# iloc[row_index, column_index]
d = new_data_1.iloc[0, 4]
# print(d)

e = new_data_1.set_index("Name")
# print(e)
# print(new_data_1.head())
# slicing
# print(new_data_1.loc[0:2, 'Name'])

# print(new_data_1.iloc[0:2, 0:2])

# print(new_data_1.loc['David':'Jessy', 'Name':'Country'])

csv_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv'
df = pd.read_csv(csv_path)
# print(df)
# print(df.head())
# must  install xlrd
# xlsx_path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204/Datasets/TopSellingAlbums.xlsx'
# df = pd.read_excel(xlsx_path)
# print(df.head())
# print(df[['Length']])
var = '01234567'
# print(var[::2])
import numpy as np
# xx =np.array([0,1])
# zz =np.array([1,0])
# yy = np.dot(xx,zz)
# print(yy)

X=np.array([[1,0],[0,1]])
Y=np.array([[2,1],[1,2]])
z = np.dot(X,Y)
# print(z)
# print('1,2,3,4'.split(','))
print("This is line C\n")