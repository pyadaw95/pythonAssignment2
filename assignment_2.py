# 1.1 Write a Python Program to implement your own myreduce() function which works exactly like
# Python's built-in function reduce()


#===========================================================================================
# 1.2 Write a Python program to implement your own myfilter() function which works exactly like
# Python's built-in function filter()

#===========================================================================================
2. Implement List comprehensions to produce the following lists.
   Write List comprehensions to produce the following Lists

pattern1 = [x for x in 'ACADGILD']
print(pattern1)

#Output:
# ['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
#---------------------------------------------

pattern2 = [i*j  for i in ['x', 'y', 'z'] for j in range(1,5)]
print(pattern2)

#Output:
#['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
#--------------------------------------------

pattern3 = [i*j for i in [1,2,2,4] for j in ['x', 'y', 'z']]
print(pattern3)

#Output:
#['x', 'y', 'z', 'xx', 'yy', 'zz', 'xx', 'yy', 'zz', 'xxxx', 'yyyy', 'zzzz']
#-------------------------------------------

pattern4 = [[i] for i in [2,3,4,3,4,5,4,5,6]]
print(pattern4)

#Output:
# [[2], [3], [4], [3], [4], [5], [4], [5], [6]]
#-------------------------------------------

pattern5 = [[j for j in range(i,i+4)] for i in range(2,6)]
print(pattern5)

#Output:
#[[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
#-------------------------------------------

pattern6 = [(i,j) for j in range(1,4) for i in range(1,4)]
print(pattern6)

#Output:
#[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]

#===========================================================================================
# 3. Implement a function longestWord() that takes a list of words and returns the longest one.

lst = ['Python', 'CPP', 'Power BI', 'Java', 'C', 'C#']
longestStringAt = 0

for indx in range(len(lst)-1):
    if len(lst[longestStringAt]) < len(lst[indx+1]):
        longestStringAt = indx + 1
else:
    print(lst[longestStringAt])

#Output:
# Power BI

#===========================================================================================
# 1.1 Write a Python Program(with class concepts) to find the area of the triangle using the below
# formula. area = (s*(s-a)*(s-b)*(s-c)) ** 0.5 Function to take the length of the sides of triangle 
# from user should be defined in the parent class and function to calculate the area should be defined in subclass.

class triangle:
    def sideDetails(self, s1, s2, s3):
        self._side1 = s1
        self._side2 = s2
        self._side3 = s3
        
class area(triangle):
    def triangleArea(self, *args):
        super(area,self).sideDetails(*args)
        
        s = (self._side1+self._side2+self._side3)/2
        ar = (s*(s-self._side1)*(s-self._side2)*(s-self._side3))**(0.5)
        return ar

s1 = int(input())
s2 = int(input())
s3 = int(input())

a = area()
triArea = a.triangleArea(s1,s2,s3)

print(triArea)

#===========================================================================================
# 1.2 Write a function filter_long_words() that takes a list of words and an integer n and 
# returns the list of words that are longer than n.

def filter_long_word(passedList, n):
    longerList = []
    for val in passedList:
        if len(val) > n:
            longerList.append(val)
    else:
        return longerList
 
lst = ['abc','pk','pthon', 'hello', 'world', 'c']
n = 3
newList = filter_long_word(lst, n)
print(newList)

#===========================================================================================
# 2.1 Write a Python program using function concept that maps list of words into a list of integers
# representing the lengths of the corresponding words​ . Hint: ​ If a list [ ab,cde,erty] is passed
# on to the python function output should come as [2,3,4]
# Here 2,3 and 4 are the lengths of the words in the list.

def stringLen(str):
    return len(str)

strLst = ['ab', 'x', 'xyz', 'pqrst', 'jk']    
intLst = list(map(stringLen,strLst))
print(intLst)

#===========================================================================================
# 2.2 Write a Python function which takes a character (i.e. a string of length 1) and returns 
# True if it is a vowel, False otherwise.

def isVowel(char):
    result = True
    for i in ['A','E','I','O','U']:
        if char == i or char == i.lower():
            break
    else:
        result = False
    
    return result
    
print(isVowel('n'))

#---------------- OR ----------------------

def isVowel(char):
    result = True
    returnCode = 'aeiou'.find(char.lower())
    if returnCode == -1:
        result = False
    return result
    
print(isVowel('E'))




































