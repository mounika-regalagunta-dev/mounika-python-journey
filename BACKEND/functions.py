def hello():
    print("hello")
    print("world")
print(hello)
print(hello())
a=hello()
print(a)
#output:-
<function hello at 0x0000019A4BC83E20>
hello
world
None
hello
world
None

def hello():
    print("hello")
    print("world")
    return 10
print(hello)
print(hello())
q=hello()
print(q)
#output:-
<function hello at 0x000001FE61D43E20>
hello
world
10
hello
world
10


def hello():
    for i in range(10):
        return i
print(hello())
#output:-
0

def mouni():
    m=0
    print("123")
    print("145")
a=mouni()
print(a)
print(mouni)
print(mouni())
#output:-
123
145
None
<function mouni at 0x0000027244363E20>
123
145
None


