# 1. sum of odd num using functions:
def sum_odd_numbers(a,b):
    sum = 0
    for i in range(a,b):
        if i % 2 != 0:
            sum+= i
    return sum
a = int(input("Enter a Number: "))
b = int(input("Enter a Number: "))
num = sum_odd_numbers(a,b)
print(num) 
#Output:-
Enter a Number: 23
Enter a Number: 29
75      

# 2.  sum of prime numbers using functions :
def sum_prime_numbers(n):
    sum = 0
    for i in range(2,n+1):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            sum+=i
    return sum
n = int(input("Enter a Number: "))
num = sum_prime_numbers(n)
print(num) 
#Output:-
Enter a Number: 34
160 
# sum = 0
# for i in range(2,20):
#     for j in range(2,i):
#         if i % j == 0:
#             break
#     else:
#         sum+=i
# print(sum) 
#Output:-
Enter a Number: 34
160    

         