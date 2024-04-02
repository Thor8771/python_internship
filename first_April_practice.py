def print1(n):
    # print(" ----\n|    |\n ----\n|    |\n ----")
    while n!=0:
        n=n%10;
        if n==1:
            print("     /|\n      |\n     --- ")
        elif n==2:
            print(" ----\n     |\n ----\n|     \n ----")
        elif n==3:
            print(" ----\n     |\n ----\n     |\n ----")
        elif n==4:
            print("     \n|    |\n ----\n     |\n ")
        elif n==5:
            print(" ----\n|     \n ----\n     |\n ----")
        elif n==6: 
            print(" ----\n|     \n ----\n|    |\n ----")
        elif n==7:
            print(" ----\n     |\n     \n     |\n ")
        elif n==8:
            print(" ----\n|    |\n ----\n|    |\n ----")
        elif n==9:
            print(" ----\n|    |\n ----\n     |\n ----")
        elif n==0: 
            print(" ----\n|    |\n     \n|    |\n ----")
        n=n/10
# print1(1)
def num(n):
    dict1={
        'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0
           }
    if n==1:
        dict1['c']=1
        dict1['b']=1
        
    elif n==2:
        dict1['a'],dict1['b'],dict1['g'],dict1['e'],dict1['d']=1,1,1,1,1
        # print(dict1)
    elif n==3:
        dict1['a'],dict1['b'],dict1['g'],dict1['c'],dict1['d']=1,1,1,1,1
        
    elif n==4:
       dict1['b'],dict1['g'],dict1['c'],dict1['f']=1,1,1,1
       
    elif n==5:
        dict1['a'],dict1['f'],dict1['g'],dict1['c'],dict1['d']=1,1,1,1,1
        
    elif n==6:
        dict1['a'],dict1['f'],dict1['g'],dict1['c'],dict1['d'],dict1['e']=1,1,1,1,1,1
        
    elif n==7:
        dict1['a'],dict1['g'],dict1['c'],dict1['b']=1,1,1,1
        
    elif n==8: 
        dict1['a'],dict1['f'],dict1['g'],dict1['c'],dict1['d'],dict1['e'],dict1['b']=1,1,1,1,1,1,1
        
    elif n==9:
        dict1['a'],dict1['f'],dict1['g'],dict1['c'],dict1['d'],dict1['b']=1,1,1,1,1,1
        
    else :
        dict1['a'],dict1['f'],dict1['b'],dict1['c'],dict1['d'],dict1['e']=1,1,1,1,1,1
    print(f" {dict1}   -> {n}")
    print1(n)  

    # print("")
# num(1)
# num(2)
# num(3)
num(4)
# num(5)
# num(6)
# num(7)
# num(8)
# num(9)
# num(0)
# # print1(0)
