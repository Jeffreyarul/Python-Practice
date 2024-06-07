l = [2, 7, 11, 19]
target = 9
flag = False
for i in range(len(l)):
    for j in range(i, len(l)):
        print(i, j)
        print(l[i], l[j])
        if l[i]+l[j]==target:
            print("Answer is : ", i, j)
            flag = True
            break
    if flag:
        break
