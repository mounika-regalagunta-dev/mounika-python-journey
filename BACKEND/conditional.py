age=18
if age<20:
    print("eligible for vote")
else:
    print("not eligible for vote")
#output:-
eligible for vote

n=10
if (n<=9):
    print("A")
elif(n>6):
    print("B")
else:
    print("C")
#output:-
B


a=10
b=25
if a<23 and b<56:
    print("Two conditions are true")
#output:-
Two conditions are true


f=87
n=54
if f>65 or n<23:
    print("Atleast one condition is true")
#output:-
Atleast one condition is true


a=10
b=20
if a==40:
    if a>b:
        print('inner if block')
    else:
        print('inner else block')
else:
    print('outer else block')
#ouput:-
outer else block


k='Python Developer'
for x in k:
    print(x)
#output:-
P
y
t
h
o
n

D
e
v
e
l
o
p
e
r

k='Python Developer'
for x in range(len(k)-1,-1,-1):
    print(k[x],'=====',x)
#ouput:-
r ===== 15
e ===== 14
p ===== 13
o ===== 12
l ===== 11
e ===== 10
v ===== 9
e ===== 8
D ===== 7
  ===== 6
n ===== 5
o ===== 4
h ===== 3
t ===== 2
y ===== 1
P ===== 0

r=range(20)
for x in r:
    print(x)
#output:-
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19

d=[[10,20,30], [50,60,50],[70,80,90]]
for x in range(len(d)-1,-1,-1):
    print(d[x])
#output:-
[70, 80, 90]
[50, 60, 50]
[10, 20, 30]

l='Python Developer'.split()
for x in l:
    print(x)
#output:-
Python
Developer

n=2
for x in range(1,11):
    print(n,'*',x,'=',n*x)
#output:-
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18
2 * 10 = 20

p='Python Developer'
print(len(p))
a=0
while a<len(p):
        print(p[a])
        a+=1
#ouput:-
16
P
y
t
h
o
n

D
e
v
e
l
o
p
e
r

a=0
while a<=10:
        print(a)
        a+=1
#output:-
0
1
2
3
4
5
6
7
8
9
10

n=2
a=1
while a<=10:
    print(n,'*',a,'=',n*a)
    a+=1
#output:-
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18
2 * 10 = 20


x=0.1+0.2
print(x)
print(x==0.3)
#output:-
0.30000000000000004
False

    