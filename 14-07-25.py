# Print the patterns of Z
rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if i==1 or i==rows or i+j==(rows)+1:
            res+="*"+" "
        else:
            res+=" "+" "
    print(res)

# Print the patterns of m
rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if j==1 or j==rows :
            res+="*"+" "
        else:
            res+=" "+" "
    print(res)
    
