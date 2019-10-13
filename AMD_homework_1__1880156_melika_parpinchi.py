# ===== PROBLEM1 =====
# Exercise 1 - Introduction - Say "Hello, World!" With Python
    print "Hello, World!"

# Exercise 2 - Introduction - Python If-Else
    #!/bin/python
    import math
    import os
    import random
    import re
    import sys
    n = int(input())
    if n%2!=0:
        print('Weird');
    elif n%2==0 and 2<=n<=5:
        print('Not Weird');
    elif n%2==0 and 6<=n<=20:
        print('Weird');
    elif n%2==0 and n>20:
        print('Not Weird');

# Exercise 3 - Introduction - Arithmetic Operators
    a = int(raw_input())
    b = int(raw_input())
    print(a+b)
    print(a-b)
    print(a*b)

# Exercise 4 - Introduction - Python: Division
    from __future__ import division
    a = int(raw_input())
    b = int(raw_input())
    print(a//b)
    print(a/b)

# Exercise 5 - Introduction - Loops
    n = int(raw_input())
    for i in range (0,n):
        print(i**2)

# Exercise 6 - Introduction - Write a function
    def is_leap(year): #just like it is said in the question!!
        leap = False
        if year % 400 == 0:
            return True
        if year % 100 == 0:
            return False
        if year % 4 == 0:
            return True
        else:
            return False
        return leap

# Exercise 7 - Introduction - Print Function
    from __future__ import print_function
    if __name__ == '__main__':
        n = int(raw_input())
    for i in range (n):
        print(i+1, end="")

# Exercise 8 - Basic data types - List Comprehensions
    ar = []
    p = 0
    if __name__ == '__main__':
        x = int(raw_input())
        y = int(raw_input())
        z = int(raw_input())
        n = int(raw_input())
        for i in range(x + 1):  # nested loop
            for j in range(y + 1):
                for k in range(z + 1):
                    if i + j + k != n:
                        ar.append([])
                        ar[p] = [i, j, k]
                        p += 1
    print(ar)

# Exercise 9 - Basic data types - Find the Runner-Up Score!
    if __name__ == '__main__':
        n = int(raw_input())
        arr = map(int, raw_input().split())
    arr.sort()
    m = max(arr)
    i=0
    while(i<n):
        if m ==max(arr):
            arr.remove(max(arr))
        i+=1
    print(max(arr))

# Exercise 10 - Basic data types - Nested Lists
    students = [] #empty list of students
    for _ in range(int(raw_input())):
        name = raw_input()
        score = float(raw_input())
        grade = [name, score]
        students.append(grade) #append the name and score of the students
    students = sorted(students, key=lambda x: x[1]) #sorted will sort and return the element in that array (return the sorted elements, using x[1] as the key.)
    second_highest = students[0][1] #it will choose the second highest number in the sorted list
    for name, grade in students:
        if grade > second_highest:
            second_highest = grade
            break
    print('\n'.join([name for name, grade in sorted(students) if grade == second_highest]))

# Exercise 11 - Basic data types - Finding the percentage
    from decimal import Decimal  # Convert the floats to decimals
    if __name__ == '__main__':
        n = int(raw_input())
        student_marks = {}
        for _ in range(n):
            line = raw_input().split()  # split is for dividing the elements of input
            name, scores = line[0], line[1:]  # choosing the indexes
            scores = map(float, scores)
            student_marks[name] = scores
        query_name = raw_input()
    query_scores = student_marks[query_name]
    total_scores = sum(query_scores)
    avg = Decimal(total_scores / 3)  # there are 3 lessons
    print(round(avg, 2))  # the round will make the float to integer

# Exercise 12 - Basic data types - Lists
    #the code is so simple!
    if __name__ == '__main__':
        N = int(raw_input())
        result = []
        for n in range(N):
            x = raw_input().split(" ") #string to list
            command = x[0]
            if command == 'insert':
                result.insert(int(x[1]), int(x[2]))
            elif command == 'remove':
                result.remove(int(x[1]))
            elif command == 'append':
                result.append(int(x[1]))
            elif command == 'sort':
                result = sorted(result)
            elif command == 'print':
                print(result)
            elif command == 'pop':
                result.pop()
            elif command == 'reverse':
                result = result[::-1]

# Exercise 13 - Basic data types - Tuples
    if __name__ == '__main__':
        n = int(raw_input())
        integer_list = map(int, raw_input().split())
        print hash(tuple(integer_list)) #the one line code! it will put the input in tuple and hash and print it!

# Exercise 14 - Strings - sWAP cASE
    def swap_case(s):
        result=[]
        for a in s:
            if (a.isupper()) == True:  #isupper() checks if the character is upper
                result+=(a.lower()) #change it to lower and add it to result!
            elif (a.islower()) == True: #islower() checks if the character is lower
                result+=(a.upper())
            elif (a.isspace()) == True: #isspace() checks if the character is space
                result+= a
            else:
                result+=a
        return "".join(result)

# Exercise 15 - Strings - String Split and Join
    def split_and_join(line):
        a = line.split(" ")
        line = "-".join(a)
        return line

# Exercise 16 - Strings - What's Your Name?
    def print_full_name(a, b):
        print(f"Hello {a} {b}! You just delved into python.") #f-string, prefix the string with the f so the string can be formatted in the same like str.format().

# Exercise 17 - Strings - Mutations
    def mutate_string(string, position, character):
        l = list(string)
        l[position] = character #it simply change the character in the position with new character
        string = ''.join(l)
        return string

# Exercise 18 - Strings - Find a string
    def count_substring(string, sub_string):
        counter=0
        i=0
        while i<len(string):
            if string.find(sub_string,i)>=0: #find() method finds the first occurrence of the specified value,returns -1 if the value is not found.syntax: string.find(value, start, end)
                i=string.find(sub_string,i)+1
                counter+=1 #to find out how many times it has occurred
            else: break
        return counter
        return

# Exercise 19 - Strings - String Validators
    if __name__ == '__main__':
        s = raw_input()
        r = ["False", "False", "False", "False", "False"] #bydefult we have a list of false and if the isnum() etc are true the false will change to true!
        for i in s:
            if i.isalnum():
                r[0] = "True"
            if i.isalpha():
                r[1] = "True"
            if i.isdigit():
                r[2] = "True"
            if i.islower():
                r[3] = "True"
            if i.isupper():
                r[4] = "True"
        print '\n'.join(r)

# Exercise 20 - Strings - Text Alignment
    #Replace all ______ with rjust, ljust or center.
    thickness = int(raw_input()) #This must be an odd number
    c = 'H'
    #Top Cone
    for i in range(thickness):
        print (c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1)
    #Top Pillars
    for i in range(thickness+1):
        print (c*thickness).center(thickness*2)+(c*thickness).center(thickness*6)
    #Middle Belt
    for i in range((thickness+1)/2):
        print (c*thickness*5).center(thickness*6)
    #Bottom Pillars
    for i in range(thickness+1):
        print (c*thickness).center(thickness*2)+(c*thickness).center(thickness*6)
    #Bottom Cone
    for i in range(thickness):
        print ((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6)
    #just did it randomly!!!! it took me too much time!!!

# Exercise 21 - Strings - Text Wrap
    def wrap(string, max_width):
        wraps = textwrap.fill(string,max_width) #The fill() method generates a string. It adds the new line character after exceeding the specified width.
        return wraps

# Exercise 22 - Strings - Designer Door Mat
    char1='.|.'
    char2='-'
    def welcome(n,m): #the image is just mirrored from the middle of it so the below part is just reversed of the top part!so we make one of them and put the welcome between them(i got the idea from hackerrank!)
        wel = [(char1*(2*i + 1)).center(m, char2) for i in range(n//2)]
        print('\n'.join(wel + ['WELCOME'.center(m, char2)] + wel[::-1]))
    if __name__ == '__main__':
        n, m = map(int,input().split())
        welcome(n,m)

# Enter your code here. Read input from STDIN. Print output to STDOUT
# Exercise 23 - Strings - String Formatting
# Exercise 24 - Strings - Alphabet Rangoli
# Exercise 25 - Strings - Capitalize!
    # Complete the solve function below.
    def solve(s):
        for x in s.split():
            s = s.replace(x, x.capitalize(), 1) #this code will capitalize the first argument of string, syntax: string.replace(old, new, count)
        print(s)
    # i dont know why it doesn't work!!

# Exercise 26 - Strings - The Minion Game
# Exercise 27 - Strings - Merge the Tools!
# Exercise 28 - Sets - Introduction to Sets
# Exercise 29 - Sets - No Idea!
# Exercise 30 - Sets - Symmetric Difference
# Exercise 31 - Sets - Set .add()
# Exercise 32 - Sets - Set .discard(), .remove() & .pop()
# Exercise 33 - Sets - Set .union() Operation
# Exercise 34 - Sets - Set .intersection() Operation
# Exercise 35 - Sets - Set .difference() Operation
# Exercise 36 - Sets - Set .symmetric_difference() Operation
# Exercise 37 - Sets - Set Mutations
# Exercise 38 - Sets - The Captain's Room
# Exercise 39 - Sets - Check Subset
# Exercise 40 - Sets - Check Strict Superset
# Exercise 41 - Collections - collections.Counter()
# Exercise 42 - Collections - DefaultDict Tutorial
# Exercise 43 - Collections - Collections.namedtuple()
# Exercise 44 - Collections - Collections.OrderedDict()
# Exercise 45 - Collections - Word Order
# Exercise 46 - Collections - Collections.deque()
# Exercise 47 - Collections - Company Logo
# Exercise 48 - Collections - Piling Up!
# Exercise 49 - Date time - Calendar Module
# Exercise 50 - Date time - Time Delta
# Exercise 51 - Exceptions -
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    def STDOUT(STDIN):
        for i in range(STDIN):
            try:
                x, y = map(int, input().split())
                print(int(x/y))
            except ZeroDivisionError: #Raised when division or modulo by zero takes place for all numeric types
                print('Error Code: integer division or modulo by zero')
            except ValueError as v: #Raised when a function gets argument of correct type but improper value
                print('Error Code:',v)
    if __name__ == '__main__':
        STDIN = int(input())
        STDOUT(STDIN)

# Exercise 52 - Built-ins - Zipped!
# Exercise 53 - Built-ins - Athlete Sort
# Exercise 54 - Built-ins - Ginorts
# Exercise 55 - Map and lambda function
    cube = lambda x: x ** 3
    def fibonacci(n):#the simplest way for fibonacci is recursive method
        # return a list of fibonacci numbers
        if n==1 or n==2:
            return 1
        else:
            return fibonacci(n-1)+fibonacci(n-2)
            #i do not know what is the problem with this!
    if __name__ == '__main__':
        n = int(input())
        print(list(map(cube, fibonacci(n))))

# Exercise 56 - Regex - Detect Floating Point Number
# Exercise 57 - Regex - Re.split()
# Exercise 58 - Regex - Group(), Groups() & Groupdict()
# Exercise 59 - Regex - Re.findall() & Re.finditer()
# Exercise 60 - Regex - Re.start() & Re.end()
# Exercise 61 - Regex - Regex Substitution
# Exercise 62 - Regex - Validating Roman Numerals
# Exercise 63 - Regex - Validating phone numbers
# Exercise 64 - Regex - Validating and Parsing Email Addresses
# Exercise 65 - Regex - Hex Color Code
# Exercise 66 - Regex - HTML Parser - Part 1
# Exercise 67 - Regex - HTML Parser - Part 2
# Exercise 68 - Regex - Detect HTML Tags, Attributes and Attribute Values
# Exercise 69 - Regex - Validating UID
# Exercise 70 - Regex - Validating Credit Card Numbers
# Exercise 71 - Regex - Validating Postal Codes
# Exercise 72 - Regex - Matrix Script
# Exercise 73 - Xml - XML 1 - Find the Score
# Exercise 74 - Xml - XML 2 - Find the Maximum Depth
# Exercise 75 - Closures and decorators - Standardize Mobile Number Using Decorators
# Exercise 76 - Closures and decorators - Decorators 2 - Name Directory
# Exercise 77 - Numpy - Arrays
import numpy
    def arrays(arr):
        lst=numpy.array(arr,float) #change them to floats
        print(lst[::-1]) #reverse the array
    arr = input().strip().split(' ')
    result = arrays(arr)
    print(result)

# Exercise 78 - Numpy - Shape and Reshape
    #all was said in the question itself!
    import numpy
    lst = numpy.array(input().split(),int)
    print(lst.reshape(3,3))

# Exercise 79 - Numpy - Transpose and Flatten
# Exercise 80 - Numpy - Concatenate
# Exercise 81 - Numpy - Zeros and Ones
    import numpy
    lst = list(map(int,input().split()))
    print(numpy.zeros(lst,dtype = numpy.int)) #Return a new array of given shape and type, with ones.
    print(numpy.ones(lst,dtype = numpy.int))#Return a new array of given shape and type, filled with zeros.

# Exercise 82 - Numpy - Eye and Identity
    import numpy
    lst = list(map(int, input().split()))
    n = lst[0]
    m = lst[1]
    numpy.set_printoptions(sign=' ')
    print (numpy.eye(n, m, k = 0)) #the code was right but a space was missing so i asked one of my friends and added this

#  n = number of rows in the output.m = number of columns in the output..k = index of the diagonal: 0 (the default) refers to the main diagonal, a positive value refers to an upper diagonal, and a negative value to a lower diagonal.
# Exercise 83 - Numpy - Array Mathematics
# Exercise 84 - Numpy - Floor, Ceil and Rint
    import numpy
    #everything is explained in the question
    A = numpy.array(input().split(), float)
    numpy.set_printoptions(sign=' ') # it's a useful peace of code! :))
    print (numpy.floor(A))
    print (numpy.ceil(A))
    print (numpy.rint(A))

# Exercise 85 - Numpy - Sum and Prod
# Exercise 86 - Numpy - Min and Max
# Exercise 87 - Numpy - Mean, Var, and Std
# Exercise 88 - Numpy - Dot and Cross
# Exercise 89 - Numpy - Inner and Outer
    #all were just been said in the question!
    import numpy
    A = numpy.array(input().split(), int)
    B = numpy.array(input().split(), int)
    print(numpy.inner(A,B), numpy.outer(A,B), sep='\n')
# Exercise 90 - Numpy - Polynomials
# Exercise 91 - Numpy - Linear Algebra

# ===== PROBLEM2 =====

# Exercise 92 - Challenges - Birthday Cake Candles
    #!/bin/python3
    import math
    import os
    import random
    import re
    import sys
    # Complete the birthdayCakeCandles function below.
    def birthdayCakeCandles(ar):
        return ar.count(max(ar)) # numbers of maximum integers in the array!
    if __name__ == '__main__':
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
        ar_count = int(input())
        ar = list(map(int, input().rstrip().split()))
        result = birthdayCakeCandles(ar)
        fptr.write(str(result) + '\n')
        fptr.close()

# Exercise 93 - Challenges - Kangaroo
    #!/bin/python3
    import math
    import os
    import random
    import re
    import sys
    # with some help!: to have them in a same location: x1 + n*v1 =? x2 + n*v2 --> x1-x2 =? n*(v2-v1) --> n =? (x1-x2)/(v2-v1) --> (x1-x2)%(v2-v1) this should be equal to 0 so the n is an integer.
    def kangaroo(x1, v1, x2, v2):
        if(x1<=x2 and v1<=v2) or (x2<=x1 and v2<=v1): #to check if they are ever going to reach each other or not!
            return "NO"
        elif (x1-x2)%(v2-v1)==0:
            return "YES"
        else:
            return "NO"
    if __name__ == '__main__':
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
        x1V1X2V2 = input().split()
        x1 = int(x1V1X2V2[0])
        v1 = int(x1V1X2V2[1])
        x2 = int(x1V1X2V2[2])
        v2 = int(x1V1X2V2[3])
        result = kangaroo(x1, v1, x2, v2)
        fptr.write(result + '\n')
        fptr.close()

# Exercise 94 - Challenges - Viral Advertising
    #!/bin/python3
    import math
    import os
    import random
    import re
    import sys
    # Complete the viralAdvertising function below.
    def viralAdvertising(n):
        share = 5 #first 5 people that recieved the advertise
        like = 2 #the first ones that liked
        now = 2 #the ones that shared the advertise
        for day in range(2,n+1): #from the second day because the first day has its own likes
            share = math.floor(share // 2 * 3) #the floor will round the number to less
            like = math.floor(share // 2)
            now += like
        return now
    if __name__ == '__main__':
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
        n = int(input())
        result = viralAdvertising(n)
        fptr.write(str(result) + '\n')
        fptr.close()

# Exercise 95 - Challenges - Recursive Digit Sum
    # !/bin/python
    import math
    import os
    import random
    import re
    import sys
    # Complete the superDigit function below.
    def superDigit(n, k):
        print(sumDigit(sumDigit(n) * int(
            k)))  # this will sumup the numbers and multiple k times and its also recursive so it will do it untill n<=9
    def sumDigit(n):
        if len(n) == 1:  # if n<= 9 it would return it self and goes to superDigit
            return n
        else:
            sumDigit(str(sum(int(x) for x in str(n))))
            return sumDigit(n)  # this code should sumup the digits in the sting n but i don't know why isn't it working!!

# Exercise 96 - Challenges - Insertion Sort - Part 1
    #!/bin/python3
    import math
    import os
    import random
    import re
    import sys
    # Complete the insertionSort1 function below.
    #my own code didn't work so i took one from hakerrank solutions and tried to understand it!!!
    def insertionSort1(n, arr):
        x = arr[n-1]
        for i in range(n)[::-1]: #to check list elements in reverse order to become able to use 0
            if arr[i-1] > x and i-1 >= 0: #if the last element is smaller than its previous
                arr[i] = arr[i-1] #they have to change their place
                print(*arr, sep=' ')
            elif arr[i-1] < x: #if the last element is bigger than its previous
                arr[i] = x #it will stay at its place
                print(*arr, sep=' ')
                break
            elif arr[0] > x:  #if the first element is bigger than the last one
                arr[i] = x  #they have to change their place
                print(*arr, sep=' ')
    if __name__ == '__main__':
        n = int(input())
        arr = list(map(int, input().rstrip().split()))
        insertionSort1(n, arr)

# Exercise 97 - Challenges - Insertion Sort - Part 2
    #!/bin/python3
    import math
    import os
    import random
    import re
    import sys
    # Complete the insertionSort2 function below.
    def insertionSort2(n, arr):
        for i in range(1,n):
            for j in range(i): #nested loop, The inner loop will be executed one time for each iteration of the outer loop and so it check the previous int that is bigger or smaller than this one
                if(arr[i]<arr[j]):
                    arr[i],arr[j]=arr[j],arr[i] # we change their place
            print(*arr)
    if __name__ == '__main__':
        n = int(input())
        arr = list(map(int, input().rstrip().split()))
        insertionSort2(n, arr)

