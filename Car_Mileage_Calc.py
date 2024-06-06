def mileage(dist,fuel):
    mile=dist/fuel
    return mile

def bonus(mil):
    if mil > 15 :
        money = 1000
    elif mil > 10:
        money = 500
    else:
        money =200        
    return money

def main():
    dist=int(input("enter a dist="))
    fuel=int(input("enter the amount of fuel ="))
    m=mileage(dist,fuel)
    mon=bonus(m)
    print(mon)
    print(m)


    return







if __name__=='__main__':
    main()