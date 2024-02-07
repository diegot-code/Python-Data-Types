# Data Types


# print(type)
# ____________________________________________________________________________________________________________________
# Text Type: Str
# Commonly seen: anywhere and everywhere

a = "I rode my bike." #string

# print(a)
# print(type(a))

first_str = "I also"
last_str = "eat sushi"

# print(first_str+last_str)
# print(first_str + " " + last_str)


# ____________________________________________________________________________________________________________________
# Numeric Types: int, float, complex
# Commonly seen: in all backend languages every 3 lines
b = 4 # int


# print(b)
# print(type(b))

c = 3.0 # float
# print(c)
# print(type(c))

d = 14.55 # float
# print(d)
# print(type(d))

e = (4+0j) # complex
# print(e)
# print(type(e))

test = "6"
# print(test + b)
# print(int(test) + b)


# ____________________________________________________________________________________________________________________
# Sequence Types: list, tuple, range
# Commonly seen: in quick refernce material and in math

f = ["Volvo", "BMW", "Mercedes", "Toyota"] # list positions start at 0

# print(f)
# print(f[0]) # first item in the list
# print(f[3]) # fourth item in the list
# print(g[4]) # fifth item (if there was one there...)

g = ("Laws of Physics", "Matter", "Medical Records", "Death") # tuples are immutable, cannot be added to, removed, or reassigned.

# print(g)
# print(g[4])
# print(g[3])

h = range(10) # ranges' default starts at 0 for the starting number

# print(h)
# print(h[1])

i = range(4, 14) # this range starts from 4 and ends at 14

# print(i)
# print(i[6])


# ____________________________________________________________________________________________________________________
# Mapping Type: dict
# Commonly seen: in databases

j = {"name" : "Jane" , "age" : "32"} #dictionary

# print(j)
# print(j["name"])
# print(j["Jane"])

k = {
    "firstname" : "Diego",
    "lastname" : "Torres",
    "age" : "19",
    "birthmonth" : "5",
    "birthday" : "17"
} # another dictionary format

l = {

    "human1" : {
        "id" : "1",
        "name" : "Diego Torres",
        "bloodType" : "O",
        "birthYear" : "2004",
        "birthMonth" : "05",
        "birthDay" : "17",
        "race" : "Asian/Hispanic"
    },

    "human2" :{
        "id" : "2",
        "name" : "John Doe",
        "bloodType" : "A",
        "birthYear" : "44BC",
        "birthMonth" : "01",
        "birthDay" : "01",
        "race" : "Yes"
    }
 } # most common format using dictionaries known as a nested dictionaries

# print(l)
# print(l["human1"]) # prints the dictionary with the key of "human1"
# print(l["human1"]["name"]) # prints the value of the key of "name" from the dictionary with the key of "human1"


# ____________________________________________________________________________________________________________________
# Set Types: set, frozenset
# Common seen: unknown

m = {"Strawberry", "Banana", "Kiwi"} # a set of unordered collection of unique elements

# print(m)

n = frozenset({"Strawberry", "Banana", "Kiwi"}) # an immutable set

# print(n)


# ____________________________________________________________________________________________________________________
# Boolean Type: bool 
# Commonly seen: in logic/if statements

o = True

# print(o)
# print(0 == o)
# print(1 == o)

p = False

# print(p)
# print(0 == p)
# print(1 == p)


# ____________________________________________________________________________________________________________________
# Binary Type: bytes, bytearray, memoryview
# Commonly seen: unknown

q = b"Hello World" # bytes

# print(q)

r = bytearray(5) # bytearray

# print(r)

t = memoryview(bytes(5)) # memoryview

# print(t)


# ____________________________________________________________________________________________________________________
# None Type: NoneType
# Commonly seen: unknown


u = None # None

print(u)


