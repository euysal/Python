def calculateCost(nAdult, nChild, sOrNot):
   adult=10
   child=5
   sOrNot=bool(sOrNot)
   

   
   if sOrNot==True:
      cost= (adult*nAdult)+(child*nChild)
      cost=float(cost)
      cost=cost - cost*15/100
   else:  #sOrNot==False:
      cost= (adult*nAdult)+(child*nChild)
      cost=float(cost)
      #else: 
      1#print 'Are you sudent? '
       
   return cost
          

cost1 = calculateCost(2, 5, False)
print 'The total cost you need to pay for tickets is $', cost1

cost2 = calculateCost(2, 1, True)
print 'The total cost you need to pay for tickets is $', cost2
                             
cost3 = calculateCost(0, 8, False)
print 'The total cost you need to pay for tickets is $', cost3
                             
cost4 = calculateCost(3, 3, True)
print 'The total cost you need to pay for tickets is $', cost4

cost5 = calculateCost(6, 0, True)
print 'The total cost you need to pay for tickets is $', cost5

                             
userAdult=raw_input('How many adult tickets do you want to buy? ')
userAdult=int(userAdult)

                             
userChild=raw_input('How many child tickets do you want to buy? ')
userChild=int(userChild)


userStudent=raw_input('Are you student? Yes / No ')
if userStudent=='Yes':
   userStudent=True
else :
   userStudent=False
  

userCost = calculateCost(userAdult,userChild, userStudent)
print 'The total amount you need to buy is $',userCost


