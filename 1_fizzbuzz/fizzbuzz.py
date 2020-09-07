for i in range(1, 101):
    if i % 5 == 0 and i % 3 ==0:
        print ("フィズバズ")
    elif i % 5 == 0:
        print ("バズ")
    elif i % 3 == 0:
        print ("フィズ")
    else:
        print (i)
