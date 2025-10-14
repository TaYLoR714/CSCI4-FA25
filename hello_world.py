#python code
import array as array


a = array.array('h',[26])
b = array.array('l', [1, 2, 3, 4, 5])
print (a.pop())
print (b.pop())
c = array.array('I',[6, 7, 8, 9, 10])
c.append(100)
print (c.pop())

Animals = ["cat", "dog", "snake", "bird"]
print(Animals[0])
print("snake" in Animals)
print("Elephant" in Animals)
Animals.sort()
Animals.append("Zebra")


print(Animals)


mylist = [10, 20, 30, 40,]
type (mylist)
mylist.append('100')
a.append(100)
print(mylist)

#python code
#f : Num -> Num

def f(x): #define a function using "def" <name>(<input list>)
    return (x+1) #must return some value
print(f(2), f(4), f(6))
print(f(20), f(40), f(60))

def f(y):
    return (y+49)
print(f(22), f(44), f(66))

def f(z):
    return (z+999)
print (f(50), f(100), f(150), f(200))

#collection of instructions
#collection of code
def f():
    print ("taylor is cool")
    print ("taylor is the best")
print ("this is outside the function")

def f(x):
    return 2*x
a = f(3)
print(a)
b = f(4)
print(b)
c = f(5)
print(c)
d = f(9999)
print(d)

def happy_birthday():
    print("Happy birthday to you!")
    print("Happy birthday dear Taylor")

happy_birthday()

def happy_birthday(name, age):
    print("Happy birthday to you!")
    print(f"Happy birthday dear {name}")
    print (f"You are {age} years old.")

happy_birthday("Bro", 20)
happy_birthday("Cuh", 30)
happy_birthday("Brother", 40)

def display_invoice(username, amount, due_date):
    print (f"Hello {username}")
    print (f"Your bill of ${amount} is due: {due_date}")

display_invoice("Taylor", 69.69, "05/04")

def add(x, y):
    z = x + y
    return z
print (add(1, 2))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("taylor", "reynolds")
print(full_name)

def main(x,y,z):
    print(x,y,z)

l = [1,2,3,4,5,5]
i = [0,3,4,4,5,5]
main("hello", l[i[1]],l[i[2]])



#lucas numbers

def lucas(named_variable):
    omar = [2, 1]
#0 -> 2, 1 -> 1
# omar.append(omar[1] + omar[0])
# omar[2] = omar[1] + omar[0]

    for n in range(2, named_variable):
    # for n which is equal to 2, 3, 4, 5
    # omar[n] = omar[n - 1] + omar[n - 2]
        omar.append(omar[n - 1] + omar[n - 2])
    return omar

print(lucas(6))








print ("hello world")