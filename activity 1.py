#activity1
numbers = int(input("enter numbers"))
randomnum = []


for x in range(number):
    givennumber = int(input("enter number: "))
    if givennumber > 0:
        print("positive")
    elif givennumber < 0:
        print("negative")
    randomnumber.append(givennumber)
    print(randomnum)

for i in randomnum:
    if i > 0:
        print(i, "this number is positive")
    elif i < 0:
        print(i, "this number is negative")