def calculatePay(rate, hour):
  rate=float(rate)
  hour=float(hour)
  amount=0
  if hour<=40.0:
     amount=rate*hour
 
  elif hour<=60.0 and hour>40.0:
        extra= hour-40
        amount= (40.0*rate)+(extra*(rate*1.5))
        
  elif hour>60.0:
         extra=hour-60
         amount = (40.0*rate) + (20.0*(rate*1.5)) + (extra*(rate*2.0))       
                    
  return amount                             
           

result1 = calculatePay(30, 20)
print 'The amount you will get for this hours of work is $', result1                            
result2 = calculatePay(15.50, 50)
print 'The amount you will get for this hours of work is $', result2                               
result3 = calculatePay(11, 70.25)
print 'The amount you will get for this hours of work is $', result3

userRate=raw_input('Please enter a rate per hour ')
userRate=float(userRate)
userHours=raw_input('Please enter how many hours you worked  ')
userHours=float(userHours)
 
userWork = calculatePay(userRate, userHours)
print 'You will get amount of $',userWork, 'paycheck for this work  '
