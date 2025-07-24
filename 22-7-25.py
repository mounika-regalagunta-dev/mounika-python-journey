# Print the next 5 prime numbers from a given number
def is_prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True
    
num=int(input("Enter a number"))
count=0
while count<5:
    if is_prime(num)==True:
        print(num)
        count+=1
    num+=1

