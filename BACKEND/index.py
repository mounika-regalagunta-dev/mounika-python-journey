# # print odd numbers from 1 to 10
for i in range(1,11):
    if i % 2!= 0:
        print('odd', i)
#output:-
odd 1
odd 3
odd 5
odd 7
odd 9

# # # even numbers from 1 to 10
for i in range(1,11):
    if i % 2 == 0:
       print(i)
#output:-
2
4
6
8
10

# # count the even numbers from 1 to 10
count=0
for i in range(1,11):
    if i % 2 == 0:
        print(i)
        count+=1
print("Total:",count)
#output:-
2
4
6
8
10
Total: 5

# # print output as odd number followed by hello
# # # 1 hello 3 hello 5 hello 7 hello
for i in range(1,11):
    if i % 2!=0:
        print(i)
        print("hello")
#output:-
1
hello
3
hello
5
hello
7
hello
9
hello

# # print output as odd number followed by hello and if the condition false we get output as hello
# # # 1 hello hello 3 hello hello
for i in range(1,11):
    if i % 2!=0:
        print(i)
    print("hello")
#output:-
1
hello
hello
3
hello
hello
5
hello
hello
7
hello
hello
9
hello
hello

# # print 1234 sum
sum=0
for i in range(1,5):
    sum+=i
print(sum)
#output:-
10

# # Hands-on-practice

# # sum of odd numbers, from 1 to 10
sum=0
for i in range(1,11):
    if i % 2 != 0:
        sum=sum+i
print(sum)
#output:-
25

# #Sum of even numbers from 1 to 10
sum=0
for i in range(1,11):
    if i % 2 == 0:
        sum+=i
print(sum)
#output:-
30

# # sum of numbers from 1 to 10
sum=0
for i in range(1,11):
    sum=sum+i
print(sum)
#output:-
55

# # Find the Greatest of two numbers
def hello(a,b):
    if a>b:
        print("a is greatest")
hello(20,10)
#output:-
a is greatest

# #Find the Greatest of two numbers
a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
if a>b:
    print("a is greatest",a)
elif b>a:
   print("b is gratest",b)
else:
   print("Both are Equal")
#output:-
Enter First Number:45
Enter Second Number:78
b is gratest 78

# #Find the Greatest of Three Numbers
a=int(input("Enter the First Number:"))
b=int(input("Enter the Second Number:"))
c=int(input("Enter the Third Number:"))
if a>=b and a>=c:
    print("Greatest number is:",a)
elif b>=a and b>=c:
    print("Greatest Number is:",b)
else:
    print("Greatest number is c",c)
#output:-
Enter the First Number:54
Enter the Second Number:87
Enter the Third Number:54
Greatest Number is: 87


# # Find the Leap Year
year=int(input("Enter a year:"))
if(year % 4 == 0 and year % 100 !=0) or (year % 400==0):
    print("It is a leap year",year)
else:
    print("Not a Leap Year",year)
#output:-
Enter a year:2025
Not a Leap Year 2025

# #print 1 to 10 Prime numbers
n = int(input("enter a number"))
for i in range(2,n+1):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        print(i)
#output:-
enter a number10
2
3
5
7

