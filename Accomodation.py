n=4
if(n>0):
    print('Number is positive')
else:
    print('Number is negative')

import sys
n=len(sys.argv)
print("The arguments other than filename are:")
for i in range(1,n):
    print(sys.argv[i],end=" ")

import keyword
print(keyword.kwlist)