s={}
print(s)
print(type(s))
d={1,8,90,76,67}
print(d)
print(type(d))
#methods
p={1,56,78,34,67,'python'}
print(p)
print(type(p))
p.add(16)
p.update({12,65,43,79})
print(p)
k=p.union({76.4,98,764,33})
print(k)
#output:-
{}
<class 'dict'>
{1, 67, 8, 90, 76}
<class 'set'>
{1, 34, 67, 56, 'python', 78}
<class 'set'>
{1, 34, 67, 65, 43, 12, 78, 79, 16, 56, 'python'}
{1, 34, 67, 65, 33, 98, 764, 43, 12, 76.4, 78, 79, 16, 56, 'python'}


