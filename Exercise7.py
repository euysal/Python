import random 

myList=['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll']  
print 'This is my list= ', myList
print 

randomIndex=random.choice(myList)
print 'this is my random element= ', randomIndex

while True:

  if randomIndex in myList:
    currentIndex=myList.index(randomIndex)
    print 'this is my random element index=  ',currentIndex
  print
  
  answer=raw_input('Press n for next, p for previous, or anything else to quit=  ')
  answer=str(answer)
  if answer=='n':
      nextIndex=currentIndex+1
      nextIndex=int(nextIndex)
      print 'this is next element= ', myList[nextIndex], 'and index number= ', nextIndex
      print
    
  elif answer=='p':
      prevIndex=currentIndex-1
      prevIndex=int(prevIndex)
      print 'this is previous element= ', myList[prevIndex], 'and previous number= ', prevIndex
      print
      
  elif answer=='q':
    break
 
  else:
     print 'You havent choice right option, please re-enter again'
     print
     continue
    
  
  
  
              