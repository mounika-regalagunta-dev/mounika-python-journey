#find the length of string without length method 
n="Mounika"
count=0
for i in n:
    count+=1
print(count)
#output:-
7

# find the count of a's in a given input
m="mounika"
count=0
for i in m:
    if i == 'a':
        count+=1
print(count)
#output:-
1

# reverse a string 
a="mounika"
for i in range(len(a)-1,-1,-1):
    print(a[i])
#output:-
a
k
i
n
u
o
m

# find no of aeiou in a string
u="mounika"
c="aeiou"
count=0
for i in u:
    if i in c:
        count+=1
print(count)
#output:-
4


