print("Answer this question")
name= input('Name:')
print("What is the year that you were born?",(name),"?")
year = int(input('age:'))

#fetching date class from datetime module  
from datetime import date
# creating the date object of today's date
todays_date = date.today()
#printing todays date
print("Current year: ", todays_date.year)

#Calculating the age of the user
age = todays_date.year-year

print("You age is : ",(age) )