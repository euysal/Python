
def calculateBill(totalHam, totalHot, totalMilk):

    totalHam = int(totalHam)
    totalHot=int(totalHot)
    totalMilk=int(totalMilk)
    
    bill= (totalHam *3)+ (totalHot*2) + (totalMilk*3)
    bill = float(bill)
    # 10% of the total for tax
    total= bill +(bill*10 /100)
    return total

print 'Hamburger $3 each'
print 'Hot Dog $2'
print 'Milk Shake $3'



userHam=raw_input('Please enter how many hambuger would you like to have:')
userHot=raw_input('Please enter how many hot dog would you like to have:')
userMilk=raw_input('Please enter how many milk shake would you like to have:')
bill1= calculateBill(userHam, userHot, userMilk)
print 'Your bill is $:',bill1




userHam=raw_input('Please enter how many hambuger would you like to have: ')
userHot=raw_input('Please enter how many hot dog would you like to have: ')
userMilk=raw_input('Please enter how many milk shake would you like to have: ')
bill2= calculateBill(userHam, userHot, userMilk)
print 'Your bill is ','$',bill2

userHam=raw_input('Please enter how many hambuger would you like to have: ')
userHot=raw_input('Please enter how many hot dog would you like to have: ')
userMilk=raw_input('Please enter how many milk shake would you like to have: ')
bill3= calculateBill(userHam, userHot, userMilk)
print 'Your bill is ','$',bill3

sum=bill1+bill2+bill3

print 'Your total 3 orders is : $', sum

