def billGenerate(dict1,bill):
    print("----your bill is----")
    for i in dict1:
        if dict1[i]!=0:
            if i=='Idly':
                a=600*dict1[i]
                print(f"{i}*{dict1[i]}->{a}")
            elif i=='Vada':
                a=500*dict1[i]
                print(f"{i}*{dict1[i]}->{a}")
            elif i=='Coffee':
                a=200*dict1[i]
                print(f"{i}*{dict1[i]}->{a}")
            elif i=='Dosa':
                a=800*dict1[i]
                print(f"{i}*{dict1[i]}->{a}")
            elif i=='Upma':
                a=350*dict1[i]
                print(f"{i}*{dict1[i]}->{a}")
    print(f"Your Total Bill is --> {bill}")
def TajHotel():
    bill=0
    dict1={
        "Idly":0,
        "Vada":0,
        "Coffee":0,
        "Dosa":0,
        "Upma":0,
    }
    while True:
        print("1.IDLY------>600 Rs")
        print("2.Vada------>500 Rs")
        print("3.Coffee---->200 Rs")
        print("4.Dosa------>800 Rs")
        print("5.Upma------>350 Rs")
        # print("Select 0 If you do not want to order anything")
        food=int(input("select your food or enter 0 to exit\n"))
        if food==0:
            break
        quantity=int(input("enter the quantity\n"))
        
        if food==1:
            bill=bill+600*quantity
            dict1['Idly']=dict1['Idly']+quantity
        elif food==2:
            bill=bill+500*quantity
            dict1['Vada']=dict1['Vada']+quantity
        elif food==3:
            bill=bill+200*quantity
            dict1['Coffee']=dict1['Coffee']+quantity
        elif food==4:
            bill=bill+800*quantity
            dict1['Dosa']=dict1['Dosa']+quantity
        elif food==5:
            bill=bill+350*quantity
            dict1['Upma']=dict1['Upma']+quantity
        elif food==0:
            break
        else:
            print("enter the right choice")
        print(f" Bill is :{bill}") 
        billGenerate(dict1,bill)
    print("-----Thank you for Visit------")
    # print(f" Your Bill is :{bill}") 
    billGenerate(dict1,bill)
    print("------Visit again------") 
    # print(dict1["Idly"])
def main():
    TajHotel()
if __name__=="__main__":
    main()

            