# Print numbers from 1 to 10 using a loop.
for i in range(1,11):
    print(i)
#output:-
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

# Print all even numbers between 1 and 20
for i in range(1,21):
    if i % 2 == 0:
        print("even",i)
#output:-
even 2
even 4
even 6
even 8
even 10
even 12
even 14
even 16
even 18
even 20

# Print the characters of the string "Python" one by one using a loop.
k="Python"
for x in k:
    print(x)   
#output:-
P
y
t
h
o
n

# Print the sum of numbers from 1 to 100.
sum=0
for i in range(1,101):
    sum=sum+i
print(sum)
#output:-
5050

# Print multiplication table of 5 (like 5 x 1 = 5, ... 5 x 10 = 50).
n=5
for i in range(1,11):
    print(n,"*" ,i, "=",n*i)
#output:-
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
5 * 10 = 50

# Print all elements of a list using a loop.
list=["apple", "banana", "cherry"]
for x in list:
    print(x)
#output:-
apple
banana
cherry

# Print only the vowels from the string "education" using a loop.
a="education"
for x in a:
    if x in "aeiou":
        print(x)
#output:-
e
u
a
i
o

# Count how many times the letter 'a' appears in the string "banana" using a loop.
a='banana'
count=0
for x in a:
    if x =='a':
        count+=1
print(count)
#output:-
3

# Print numbers from 10 to 1 using a loop (reverse order).
for x in range(10,0,-1):
    print(x)
#output:-
9
8
7
6
5
4
3
2
1

# Ask the user to enter 5 numbers using a loop and print their sum.
sum=0
for i in range(1,6):
    sum=sum+i
print(sum)
#output:-
15
