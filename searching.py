# Print a specific part of a string without using slicing
a="MOUNIka"
for i in range (0,5):
    print(a[i])
#Output;-
M
O
U
N
I

# Print the string to replace "is" with "si" without using replace method
a="is"
b="si"
for i in a:
    if i==b:
        b+=i
print(b)
#Output:-
si

# Print the string to replace "is" with "si" with using replace method
a="si"
print(a.replace("is","si"))
#Output:-
si
