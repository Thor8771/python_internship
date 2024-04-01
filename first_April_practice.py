def num(n):
    dict1={
        'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0
           }
    if n==1:
        dict1['c']=1
        dict1['b']=1
        print(dict1)
    elif n==2:
        dict1['a'],dict1['b'],dict1['g'],dict1['e'],dict1['d']=1,1,1,1,1
        print(dict1)
    elif n==3:
        dict1['a'],dict1['b'],dict1['g'],dict1['c'],dict1['d']=1,1,1,1,1
        print(dict1)
    elif n==4:
       dict1['b'],dict1['g'],dict1['c'],dict1['f']=1,1,1,1
       print(dict1)
    elif n==5:
        dict1['a'],dict1['f'],dict1['g'],dict1['c'],dict1['d']=1,1,1,1,1
        print(dict1)
    elif n==6:
        dict1['a'],dict1['f'],dict1['g'],dict1['c'],dict1['d'],dict1['e']=1,1,1,1,1,1
        print(dict1)
    elif n==7:
        dict1['a'],dict1['g'],dict1['c'],dict1['b']=1,1,1,1
        print(dict1)
    elif n==8: 
        dict1['a'],dict1['f'],dict1['g'],dict1['c'],dict1['d'],dict1['e'],dict1['b']=1,1,1,1,1,1,1
        print(dict1)
    elif n==9:
        dict1['a'],dict1['f'],dict1['g'],dict1['c'],dict1['d'],dict1['b']=1,1,1,1,1,1
        print(dict1)
    else :
        dict1['a'],dict1['f'],dict1['b'],dict1['c'],dict1['d'],dict1['e']=1,1,1,1,1,1
        print(dict1)
num(9)
