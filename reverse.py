#reverse a number and palindrome:            
n = int(input("enter a number"))
reverse = 0
while n > 0:
    a = n % 10
    reverse = reverse * 10 + a
    n= n // 10
print(reverse)
#Output:-
enter a number 29
92    

#  Calculate the sum of digits of a number using a while loop.
n = int(input("enter a number"))
reverse = 0
while n > 0:
    a = n % 10
    reverse = reverse + a
    n= n // 10
print(reverse)
#Output:-
enter a number 65
11

# reverse a string:
word = input("Enter a string")
reverse = " "
for i in word:
    reverse = i + reverse
print(reverse)   
#Output:-
Enter a string "python"
"nohtyp"   