a="chaitanya"
b="kumar"
c=a+b
print(c)
#output:-
chaitanyakumar

a="hjg"
b="vfg"
print(a+" "+b)
#output:-
hjg vfg

h="tty"
g="yf"
c=" "
d=h+c+g
print(d)
output:-
tty yf

a="kbhp"
print("hi i am going for morning routine walk in "+a)
#output:-
hi i am going for morning routine walk in kbhp

a="kbhp"
b="mor"
print("hi i am going for "+b+ " routine walk in "+a)

# chaitanya-> input 
# o/p -> aiaa
n="chaitanya"
m="ai"
for i in n:
    if i in m:
        print(i)
# #output:-
a
i
a
# a

# concat even positions in string chaitanya
a="chaitanya"
for i in range(0,9,2):
    print(a[i])
#output:-
c
a
t
n
a

# take two indexes and concat that part of indexes 
# # ex-> 1,4 -> chaitanya -> hai 
# 4  means -> 3
m="chaitanya"
for i in range(1,4):
    print(m[i])
#output:-
h
a
i
