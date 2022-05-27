class Guest:
    def __init__(self, first, last , interest , phone):
        self.first = first
        self.last = last
        self.interest = interest
        self.phone = phone

g_1 = Guest("Eve", "Dela Cruz", "Anime", 123)
g_2 = Guest("Adam", "Perez", "Russian literature", 321)



class Customers:
    greetings = "Welcome to Coffee Palace!"
    def __init__(self, Name, Beverages, Food, Total):
        self.Name = Name
        self.Beverages = Beverages
        self.Food = Food
        self.Total = Total

c_1 = Customers("Nate", "Espresso", "Pasta on rye", 220)
c_2 = Customers("Elaine", "Strawberyy Frappucino", "Tuna Wrap", 270)
c_3 = Customers("Samirah", "Iced caffe latte", "Cinnamon Roll", 225)
c_4 = Customers("Jerry", "Caramel Macchiato", "Glazed Doughnut", 230)
c_5 = Customers("Paz", "Iced Tea", "Blue berry Pancakes", 315)

print(Customers.greetings)
print(c_2.Name)
print(c_2.Beverages)
print(c_2.Food)
print(c_2.Total)
print(Customers.greetings)
print(c_4.Name)
print(c_4.Beverages)
print(c_4.Food)
print(c_4.Total)
print("\n\n\n")


class ClubMembers:
    def __init__(self, name, birthday, age, favorite_food, goal):
        self.name = name
        self.birthday = birthday
        self.age = age
        self.favorite_food = favorite_food
        self.goal = goal

    def display1(self):
        print("Name: ",self.name)
        print("Birthday: ", self.birthday)
        print("Age: ", self.age)
        print("Favorite Food: ", self.favorite_food)
        print("Goal: ", self.goal)

class ClubOfficers(ClubMembers):
    def __init__(self, name, birthday, age, favorite_food, goal, Position):
        self.Position = Position
        ClubMembers.__init__(self, name,birthday,age,favorite_food,goal)

    def display2(self):
        print("Name: ", self.name)
        print("Birthday: ", self.birthday)
        print("Age: ", self.age)
        print("Favorite Food: ", self.favorite_food)
        print("Goal: ", self.goal)
        print("Position: ", self.Position)


m_1 = ClubMembers("Tom", "Jan 16", "14", "Ice Cream" , "To be Happy")
m_2 = ClubOfficers("Vera","June 22", "16", "Beef", "To be World's greatest chef", "Treasurer")

m_1.display1()
m_2.display2()
print("\n\n\n")

# 2.4 code exercise

flavors = ["Vanilla", "Chocolate", "Strawberry", "Cookies n' cream", "Bubblegum"]
toppings = ["Almonds", "Banana Slices", "Choco Syrup" ,"Caramel Syrup", "White Chocolate Chips"]

ice_cream = dict(zip(flavors, toppings))
print(ice_cream)
print("\n")

ice_cream["Chocolate"] = "Blueberries"
ice_cream.update({"Matcha:": "Pistaccho", "Ube": "Mango Slices"})
print(ice_cream)
print("\n\n\n")

groceries = {"Chicken": 8, "Apples": 6, "Cucumbers": 3, "Milk": 2, "Oranges": 4}
remove = groceries.pop("Oranges")
print(groceries)
print("\n\n\n")

speakers = {"Sir Rafael": 54, "Ms Joan": 33, "Ms Danna": 67}
name = speakers.keys()
print(name)
print("\n\n\n")

tryout_results = {"Carl": "Passed", "Quentin": "Failed", "John Y.": "Passed", "Peter": "Failed",
                  "Max T": "Passed", "Joseph": "Passed", "Jone": "Failed", "Jorge": "Failed",
                  "George": "Passed", "Ben": "Passed", "Jerome": "Passed", "Rick": "Failed",
                  "Max G": "Failed", "John P": "Failed", "Vince": "Passed"}
print(tryout_results.get("Jorge"))
print("\n\n\n")

f = open("pythonessay.txt", "w")
f.write("I like Python")
f = open("pythonessay.txt", "a")
f.write("\n I plan to learn data visualization.")
f.write("\n I want to work in the field of data science")
f.write("\n I plan to make a better world")
f = open("pythonessay.txt", "r")
print("\n\n\n")


# module 4

from functionfile import personal_greeting
from functionfile import your_province
print("\n\n\n")

personal_greeting("Anna")
your_province("Batangas")
print("\n\n\n")


a = 5
def var_test():
    a = 25
    print(a)
var_test()
print(a)

print('hello')
print("Hello")

















