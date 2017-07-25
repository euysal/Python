import random
import time
import sys

# we need to add one more ' quote =1
reelList = ['orange', 'orange', 'orange', 'lemon', 'lemon', 'lemon', \
              'plum', 'plum', 'plum', 'cherries', 'cherries', 'cherries', \
              'banana', 'banana', 'banana', 'bar', 'bar', 'Lucky 7']
nPicturesInReel = reelList

nCoins = 100 # it is pocket money =2
print 'You have', nCoins, 'coins to start.  Good luck.'
print

# we create function by useing def keywords =3
def payTable(myList):
    picture1 = myList[0]
    picture2 = myList[1]
    picture3 = myList[2]
    if myList.count(picture1) == 3:
        if picture1== 'Lucky 7':
            nCoinsWon = 500
        elif picture1== 'bar':
            nCoinsWon = 100
        else:
            nCoinsWon = 10

    else:
        # it needs to compare picture2 to picture3 otherwise I always get  2 coins , it is a logic error = 10
        if (picture1 == picture2) or (picture2 == picture3) or (picture1 == picture3):
            nCoinsWon = 2
        else:
            nCoinsWon = 0

    return nCoinsWon # I returned nCoinsWon
        

while True:

    bet = raw_input('How many coins do you want to bet (defaults to 1, enter 0 to quit): ')
    # bet is str so check for str '0'
    if bet == '0':
        print 'Sorry to see you go.  Come back again soon.'
        sys.exit(0)     # New, but works to quit the program
    if bet == '':
       bet = 1

    # Extra Extra HW asking user to enter only integer number    
    try:
        bet=int(bet)
    except:
        print'pls, enter only integer numbers'
        continue

    if bet<0:
        print 'pls, enter only positive integer numbers'
        continue
    
    # Extra HW , do not let user play if user doesnt have enough money 
    if bet>nCoins:
        print ' sorry your budget is not enought to bet, try bet again ! '
        continue
        

    resultList = []
    for spin in range(3):
    
       
        #we have to create random choice from 0 to length of nPicturesInReel = 4
        thisReelIndex = random.randrange(0, len(nPicturesInReel))
        thisPicture = reelList[thisReelIndex]
        resultList.append(thisPicture)

    print 'Spinning ... '
    print
    time.sleep(.5)
    print '     ', resultList[0]
    time.sleep(.5)
    print '     ', resultList[1]
    time.sleep(.5)
    print '     ', resultList[2]
    print
    
    # it gives an error in here, thats why I declare bet value as integer after input = 5
    # it has to be minus not plus because we need to minus bet number from totalcoins = 9
    nCoins = nCoins - bet

    print 'bet', bet , ' table' , resultList
    payOut = bet * payTable(resultList)
    #it gives error in here, the problem was payTable function didnt return how much coins user earned = 6
    
    #if it is a comparation, we need to use '==' = 7
    if payOut == 0:
        print 'Sorry - you lose.'
    else:
        print 'You won', payOut, 'coins.  Cha-ching!'
        if payOut > 50:
            print '                         WOOOOO  HOOOOOOOOOOO!!!!'
            
    nCoins = nCoins + payOut
    
    #it needs to be comma ',' not plus '+' = 8
    print 'coins' , nCoins, 'bet  ' , bet, 'payout ' , payOut 
    
    print 'You now have' , nCoins ,  'coins.'
    print
    
