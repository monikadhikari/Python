##Announce
print("Calculate the Area of Circle\n")

##Gathering data
diameter=input("Enter the diameter of Circle: ")
pi=3.14


## Data coversion
diameter=int(diameter)

##Logic
radius=diameter/2
area=pi*(radius**2)


###
print("The area of a circle of radius",radius,"is",area)
