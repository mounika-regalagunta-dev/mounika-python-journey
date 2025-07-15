# Print the Patterna of H 
rows=5
for i in range(1,rows+1):
    res=" " 
    for j in range(1,rows+1):
        if j==1 or j==rows or i==(rows//2)+1:
            res+="*"+" "
        else:
            res+=" "+" "

    print(res)

# Print the Patterna of E
rows=5
for i in range(1, rows+1):
    res=" "
    for j in range(1,rows+1):
        if i==1 or i==rows or j==1 or i==(rows//2)+1:
            res+="*" + " "
        else:
            res+=" "+" "
    print(res)

# Print the Patterna of N
rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if j==1 or j==rows or i==j:
            res+="*"+" "
        else:
            res+=" "+" "
    print(res)