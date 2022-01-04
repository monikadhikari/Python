'''
Program:  List comprehension

Description: Completing the list comprehenson excercises using list comprehenssion and sorting

    Simple List Comprehension & Sorting Template
    Complete the list comprehension exercises here
    Any functions you write must also have
    (1) a docstring that describes the input parameters
        and the value returned
    (2) at least two significant tests that verify the function
'''
###### 1. List comprehension analysis
### Code
def linc(a,b=2):
 '''
 The input parameter is list and the function is returning only integer values . Output parameter is also list type.
 '''
### PUT CODE HERE
 return [x+b for x in a if type(x) is int]
x = [1,2,'3',4]
y = linc(x)  # [3,4,6]
z = linc(x,1) # [2,3,5]
print(x)
print(y)
print(z)

###### 2. the listInc() function
def listInc(a):
    '''
    The input parameter is list and it returns a list of integer values increament by 1
    '''
### YOUR CODE HERE
    return [i+1 for i in a if type(i) is int]
### listInc() tests
assert listInc([7,2,4,8]) == [8,3,5,9], 'listInc failed [7,2,4,8]'
assert listInc([9,-1,0.0,5]) == [10,0,6], 'listInc failed [9,-1,0.0,5]'
print('listInc is OK\n')

###### 3. the listOut() function
def listOut(a):
    '''
    This function takes input list and print the list's values line by line
    '''
### YOUR CODE HERE
    [print(i) for i in a]
### listOut() tests
listOut([7,2,'OK',8])
print()
listOut([[1,2],2.0,'$',8])
print()

###### 4. statements that move items between lists
### end of A to beginning of B
a,b = [1,2,3], [4,5,6]
b.insert(0,a.pop())
print(a,b)
### beginning of A to end of B
a,b = [1,2,3], [4,5,6]
### YOUR CODE HERE
b.append((a.pop(0)))
print(a,b,'\n')

###### 5a. the rotateForward() function
def rotateForward(a):
    '''
    This function is taking list as an input rotating the list and return it
    '''
    [a.insert(0,a.pop())]
    return a
    
### rotateForward() tests
assert rotateForward([1,2,3,4]) == [4,1,2,3], 'rotateForward failed'
print('rotateForward ok\n')

###### 5b. the rotateBackward() function
def rotateBackward(a):
    '''
    This function is taking list as an input rotating the list in backward direction and return it 
    '''
   
    [a.append((a.pop(0)))]
    return a
### YOUR CODE HERE
### rotateForward() tests
assert rotateBackward([1,2,3,4]) == [2,3,4,1,], 'rotateBackward failed'
print('rotateBackward ok\n')

###### 6. Analysis of iSort()
def iSort(x,n=2):
    '''
    This function takes input as a list and return the sorted list by key elements
    '''
    return sorted(x,key=lambda a:a[n])
### PUT CODE HERE
x = [(1,'one','uno'),(2,'two','dos'),(3,'three','tres')]
print(iSort(x))
print(iSort(x,1))
print()

###### 7. Length sorting
z = ['bzz','z','cz','azzz']
z=sorted(z,key=lambda l:(l.rindex(l[-1])+1))
print(z,'\n')

###### 8. the backSort() function
def backSort(a):
    '''
    This function takes input as a list and return the sorted list by last value of the string
    '''
    return sorted(a,key=lambda a:a[-1])
### backSort() tests
assert backSort(['red','yellow','blue','green','black']) == \
       ['red', 'blue', 'black', 'green', 'yellow'], 'backSort FAILED'
print('backSort OK')



