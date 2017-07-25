import random 

myList=['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll']  
print 'This is my list= ', myList
print 

randomIndex=random.randint(0, len(myList)-1)
print 'this is my random index= ', randomIndex
currentIndex=randomIndex
while True:

  if randomIndex in range(0,len(myList)):
    currentIndex=randomIndex
  print 'this is my element in array=  ',myList[currentIndex]
  print
  
  answer=raw_input('Press n for next, p for previous, or q to quit=  ')
  answer=str(answer)
  if answer=='n' and currentIndex >= 0:
      nextIndex=currentIndex+1
      randomIndex=nextIndex
      print 'this is next element= ', myList[nextIndex], 'and index number= ', nextIndex
      print
    
  elif answer=='p' and currentIndex < len(myList)-1:
      prevIndex=currentIndex-1
      randomIndex=prevIndex
      print 'this is previous element= ', myList[prevIndex], 'and previous number= ', prevIndex
      print
      
  elif answer=='q':
    break
 
  else:
     print 'You havent choice right option, please re-enter again'
     print
     continue
    
  
  
  
              
