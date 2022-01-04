## Description

print("Program to compute a letter grade for a numerical score")


## Definig Grade function
def gradeCalculator(score):
    grade=None
    score=float(score)
    if score>=95.0:
        grade="A+"
    elif score>=90 and score<95:
        grade="A"
    elif score>=85 and score<90:
        grade="A-"
    elif score>=80 and score<85:
        grade="B+"
    elif score>=75 and score<80:
        grade="B"
    elif score>=70 and score<75:
        grade="B-"
    elif score>=65 and score<70:
        grade="C+"
    elif score>=60 and score<65:
        grade="C"
    elif score>=55 and score<60:
        grade="C-"
    else:
        grade="F"
    res="The letter grade for {} percent is {}."
    res=res.format(score,grade)
    
    
    return res


## User input 

score=float(input("Enter the numerical score: "))

## Calling Function
response=gradeCalculator(score)

##Displaying Result 
print(response)