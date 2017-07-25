name='Eda'
status='student'
school='Ucsc'
major='software engineering'
community='Dublin'
gpa=3.2
credit= 14.5
age=27
currentStatus=True
hybrid= False 
weekend=False

daysOfSchool=4
priceOfGas=2.97
milesOfcommute=85.8
milesPerGallon=24
weeklyMiles=milesOfcommute*daysOfSchool
money= (weeklyMiles/milesPerGallon)*priceOfGas


print name, 'is a ', status, ' at ', school
print currentStatus
print name, 'live/lives in ' , community
print name, 'is/are' , age , 'years old'
print name, 'takes/take' , credit , 'class', 'and her/his gpa is ', gpa


print 'Total miles weekly to drive to the school from home is ', weeklyMiles
print 'And weekly spending money for this gas', '$', money
print 'Is the car hybrid? ', hybrid
print 'Do you have school on the weekends?', weekend

a=5
b=4
c=False

print 'a==b', a==b , c
print 'a/b=',a/b
print 'a-b=', a-b
print 'a*b=', a*b
print 'a+b=', a+b


