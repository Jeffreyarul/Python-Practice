# inventory={"gold":500,
#            "pouch":['f','t','g'],
#            "backpack":['x','b','r']
# }
# inventory['pocket']=['s','s','t']
# inventory['backpack'].sort()
# inventory['backpack'].remove('b')
# inventory['gold']+=50
# print(inventory)

Prices={'banana':4,
        'apple':2,
        'orange':1.5,
        'pear':3
}
print(Prices)
stock={
    'banana':100,
    'apple':150,
    'orange':250,
    'pear':325
}
total=0
for i,j in Prices.items():
    for x,y in stock.items():
        if i==x:
            total+=j*y
            print(total)

