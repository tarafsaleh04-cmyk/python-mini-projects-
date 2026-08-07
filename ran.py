import random
randNum= random.randint(0,100)

while (True):
    enter= int(input('pick from  0 to 100: '))
    if (enter == randNum):
        print('right the number is ', randNum)
        break
    elif (enter > randNum) :
        print(' wronnng the number you chosse is bigger')
        
    else:
        print('wrong the number you pick is less than ')
        

    