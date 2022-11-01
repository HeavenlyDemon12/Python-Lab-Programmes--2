a=int(input('enter the value of a'))
b=int(input('enter the value of b'))
c=int(input('enter the value of c'))
if((a>b) and (a>c)):
    print('a is greater',str(a))
if((b>a) and (b>c)):
    print('b is greater',str(b))
if((c>a) and (c>b)):
    print('c is greater',str(c))