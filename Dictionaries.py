# inventory={"gold":500,
#            "pouch":['f','t','g'],
#            "backpack":['x','b','r']
# }
# inventory['pocket']=['s','s','t']
# inventory['backpack'].sort()
# inventory['backpack'].remove('b')
# inventory['gold']+=50
# print(inventory)
import numpy as np

l = [1, 2, 3, 4]
l = np.array(l)
print(type(l))
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
for i in Prices.keys():
    total+=Prices[i]*stock[i]
print(total)

