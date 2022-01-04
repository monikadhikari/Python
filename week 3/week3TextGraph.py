## Announcement

print("TextGraph: Draw a bar graph using characters\n")

#Data gather
inp=input("Enter up to 10 positive whole numbers less than 50: ")
numbers=inp.split()


## Logic and Print
for i in numbers:
    if i.isnumeric() and int(i)<50:
       print('=' * int(i))
    else:
        print("?")




