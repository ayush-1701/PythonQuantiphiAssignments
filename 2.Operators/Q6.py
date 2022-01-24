# Write a Python program to calculate the number of days between two dates.
from datetime import date

startDate = date(2014, 7, 2)
endDate = date(2014, 7, 11)
result = endDate - startDate
print(result.days, "days")
