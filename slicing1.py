#Take a string print all upper case letters at first and lower case letters at last  with using methods
a="MouNikA"
upr=""
lwr=""
for i in a:
    if i.isupper():
        upr+=i
    else:
        lwr+=i
print(upr+lwr)
#Output:-
MNAouik

#Take a string print all upper case letters at first and  flollowed by lower case letters at last special characters  with using methods
b="chA iTn @Ru"
upr=""
lwr=""
spe=""
for i in b:
    if i.isupper():
        upr+=i
    elif i.islower():
        lwr+=i
    else:
        spe+=i
print(upr+lwr+spe)
#Output:-
ATRchinu  @

# By using count method
b="chAn iTn @Ru"
upr=""
lwr=""
count=0
for i in b:
    n=i.isalnum();
    if n!=True:
        count+=1
print(count)
#Output:-
3

#ASCII VALUES 65-90=A  97-122=a   48-57=0-9 remaining=special characters
a="Chai tYa@Na"
for i in a :
    print(ord(i))
#Output;-
67
104
97
105
32
116
89
97
64
78
97

#Take a string print all upper case letters at first and lower case letters at last  without using method
v="Chai tYa@Na"
upr=""
lwr=""
spe=""
for i in v:
    print(ord(i))
    if ord(i)>=65 and ord(i)<=90:
        upr+=i
    elif ord(i)>=97 and ord(i)<=122:
        lwr+=i
    else:
        spe+=i
print(upr,lwr,spe)
print(upr+lwr+spe)
#Output:-
67
104
97
105
32
116
89
97
64
78
97
CYN haitaa  @
CYNhaitaa @
