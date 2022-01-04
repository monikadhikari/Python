#annoucement
print("Program to encode a word\n")

## Data gather

inp=input("Enter a word: ")

#Logic
res=""

## ord Funtion find the ascii code or char
for i in list(inp):
    res+=str(ord(i)-97)+" "
    

#Print
print("The code for",inp,"is:",res)
    
