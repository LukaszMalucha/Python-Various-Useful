# -*- coding: utf-8 -*-


############################################################## Copying Sequences

s = [1,2,3,4,5,6,7,8,9]
s[::-1]
    
cp = []
cp = [e for e in s]

cp = s.copy() ## only mutable

cp = s[0:len(s)]

cp = s[:] ## only mutable

cp = list(s) ## only mutable


###################################################################### Deep Copy

s = [[0,1], [2,3]]

cp = [e.copy() for e in s]


######################################################################## Slicing

sl = s[1:6:2]


################################################# In-place Concat and Repetition

l1 = [1,2,3]
l2 = [4,5,6]

l1 = l1 + l2

l1 += l2
l1 *= 2


##################################################### Assignments in Mutable Seq

l = [1,2,3,4,5]

l[1:3] = (10, 20, 30)

l[1:3] = []


######################################################################## Sorting

l = [1,2,3,4,5]

ord('a')


t = 10,3,5,8,9,6,1

sorted(t)

s = {10,3,5,8,9,6,1}

sorted(s)

d = {'a':100, 'b':200, 'c':10}

sorted(d)

sorted(d, key= lambda k: d[k])

t = 'asd', 'asda', 'dfdf', 'dfghdf'

def sort_key(s):
    return len(s)

sorted(t, key=sort_key)

sorted(t, key=lambda s: len(s), reverse = True)

l = 'this is where we stand at the moment'.split()

sorted(l, key=lambda s: len(s))

l.sort(key=lambda s:len(s))






























