numberList=[]

while True:
    userNum=raw_input('Please enter a number or Enter the key to quit=  ')

    if userNum=='':
       print
       break
    else:
       userNum=float(userNum)
       numberList.append(userNum)
        
        
print 'Length of my list in array=  ',len(numberList)
print 

#Alternative answer 1 
print 'My resulting list in array =  ',numberList

# Answer 1 
for number in numberList:
  print 'My resulting list=   ',number
   

#Answer 2
print
minimum=numberList[0]
for number in numberList:
  if minimum>number:
     minimum=number
print 'Minimum number is=  ',minimum

#Answer 3 
maximum=numberList[0]
for number in numberList:
  if number>maximum:
    maximum=number
print 'Maximum number is=  ', maximum    

#Answer 4 
print
total=0
for number in numberList:
  total=total+number 
print 'Sum of all the number is=  ',total


#Answer 5 
total1=0
average=0
divide=len(numberList)
divide=int(divide)
for number in numberList:
  total1=total1+number
  average=total/divide
  #print 'average and total and divide',average, total, divide
print 'Average of all the number is=  ',average
print
  
print 'Ok. Thanks, bye'     

 

