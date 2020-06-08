# The following list comprehension exercises will make use of the
# defined Human class.
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"


humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
a = []
another = []
for i in humans:
    a.append(i.name)
for f in range(len(a)):
    if a[f][0] == "D":
        another.append(a[f])
print(another)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = []
anotherone = []
for i in humans:
    b.append(i.name)
for f in range(len(b)):
    if b[f][-1] == "e":
        anotherone.append(b[f])
print(anotherone)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
c = []
cg = []
for i in humans:
    c.append(i.name)
for f in range(len(c)):
    if (
        c[f][0] == "C"
        or c[f][0] == "D"
        or c[f][0] == "E"
        or c[f][0] == "F"
        or c[f][0] == "G"
    ):
        cg.append(c[f])
print(cg)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = []
for ag in humans:
    d.append(ag.age + 10)
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = [f"{x.name}-{x.age}" for x in humans]
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = [(x.name, int(x.age)) for x in humans if int(x.age) >= 27 and int(x.age) <= 32]
print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
g = [Human(x.name.upper(), int(x.age) + 5) for x in humans]
print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
import math

h = [math.sqrt(int(x.age)) for x in humans]
print(h)
