import sys

people = []
for line in sys.stdin:
    die = line.split()
    a = int(die[0])
    b = int(die[1])
    c = int(die[2])
    d = int(die[3])
    people.append((a+b)/2 + (c+d)/2)


if people[0]>people[1]:
    print("Gunnar")
elif people[1]>people[0]:
    print("Emma")
else:
    print("Tie")
