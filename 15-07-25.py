# # Print the patterns of a diamond in the terms of *
rows=5
for i in range(1,rows+1):
    res=""
    for space in range(1,rows-i+1):
        res+=" "
    for j in range(1,i+1):
        res+="*"+" "
    print(res)
for i in range(rows-1,0,-1):
    res=""
    for space in range(rows-i):
        res+=" "
    for j in range(i):
        res+="*"+" "
    print(res)


# Print the pattern of a diamond in a terms of lowercase alphabets
rows=5
asc=97
for i in range(1,rows+1):
    res=""
    for space in range(1,rows-i+1):
        res+=" "
    for j in range(1,i+1):
        res+=chr(asc)+" "
        asc+=1
    print(res)
for i in range(rows-1,0,-1):
    res=""
    for space in range(rows-i):
        res+=" "
    for j in range(i):
        res+=chr(asc)+" "
        asc+=1
    print(res)

    