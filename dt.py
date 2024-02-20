# Data Types


# print(type)
# ____________________________________________________________________________________________________________________
# Text Type: Str
# Commonly seen: anywhere and everywhere


# print("I rode my bike.") #string
# print(type("I rode my bike."))

# print("I also"+"eat sushi.")
# print("I also" + " " + "eat sushi.")


# ____________________________________________________________________________________________________________________
# Numeric Types: int, float, complex
# Commonly seen: in all backend languages every 3 lines

# print(4) # int
# print(type(4))

#-----------------------------------------


# print(3.0) # float
# print(type(3.0))

# print(14.55) # float
# print(type(14.55))

#-----------------------------------------


# print(4+0j) # complex
# print(type(4+0j))

# ____________________________________________________________________________________________________________________
# Sequence Types: list, tuple, range
# Commonly seen: in quick refernce material and in math

 # list positions start at 0

# print(["Volvo", "BMW", "Mercedes", "Toyota"])
# print(["Volvo", "BMW", "Mercedes", "Toyota"][0]) # first item in the list
# print(["Volvo", "BMW", "Mercedes", "Toyota"][3]) # fourth item in the list
# print(["Volvo", "BMW", "Mercedes", "Toyota"][4]) # fifth item (if there was one there...should display an IndexError)

#-----------------------------------------

# print(("Laws of Physics", "Matter", "Medical Records", "Death")) # tuples are immutable, cannot be added to, removed, or reassigned.
# print(("Laws of Physics", "Matter", "Medical Records", "Death")[4])
# print(("Laws of Physics", "Matter", "Medical Records", "Death")[3])

#-----------------------------------------

# print(range(10)) # ranges' default starts at 0 for the starting number
# print(range(10)[1])

# print(range(4, 14)) # this range starts from 4 and ends at 14
# print(range(4, 14)[6])

# ____________________________________________________________________________________________________________________
# Mapping Type: dict
# Commonly seen: in databases

# print({"name" : "Jane" , "age" : "32"}) #dictionary
# print({"name" : "Jane" , "age" : "32"}["name"])
# print({"name" : "Jane" , "age" : "32"}["Jane"]) # KeyError

k = {
    "firstname" : "Diego",
    "lastname" : "Torres",
    "age" : "19",
    "birthmonth" : "5",
    "birthday" : "17"
} # another dictionary format

l = {

    "patient1" : {
        "id" : "1",
        "name" : "Diego Torres",
        "bloodType" : "O",
        "birthYear" : "2004",
        "birthMonth" : "05",
        "birthDay" : "17",
        "race" : "Asian/Hispanic"
    },

    "patient2" :{
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
# print(l["patient1"]) # prints the dictionary with the key of "patient1"
# print(l["patient1"]["name"]) # prints the value of the key of "name" from the dictionary with the key of "patient1"


# ____________________________________________________________________________________________________________________
# Set Types: set, frozenset
# Common seen: unknown

# print({"Strawberry", "Banana", "Kiwi"}) # a set of unordered collection of unique elements

#-----------------------------------------

# print(frozenset({"Strawberry", "Banana", "Kiwi"})) # an immutable set

# ____________________________________________________________________________________________________________________
# Boolean Type: bool 
# Commonly seen: in logic/if statements

# print(True)
# print(0 == True)
# print(1 == True)

# print(False)
# print(0 == False)
# print(1 == False)

# ____________________________________________________________________________________________________________________
# Binary Type: bytes, bytearray, memoryview
# Commonly seen: unknown

# print(b"Hello World") # bytes

#-----------------------------------------

# print(bytearray(5)) # bytearray

#-----------------------------------------

# print(memoryview(bytes(5))) # memoryview


# ____________________________________________________________________________________________________________________
# None Type: NoneType
# Commonly seen: unknown

# print(None) # None


