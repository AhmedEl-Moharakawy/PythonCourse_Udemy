#Q: Years!
"""
● Assume a year is 12 months, but each month is 30 days
○ That is a year has 12 * 30 = 360 days
● Read an integer: whole number of days
○ Total years total months remaining days
● Inputs ⇒ Outputs
○ 360 1 0 0 each 360 days a year
○ 30 0 1 0 each 30 days a month
○ 10 0 0 10 just days infant!
○ 391 1 1 1 391 = 360 + 30 + 1 = 1 year, 1 month, 1 day
○ 61 0 2 1 61 = 2*30 + 1
○ 200 0 6 20 200 = 30*6 + 20
○ 1000 2 9 10 1000 = 2*360 + 9*30 + 10
○ 5000 13 10 20
"""

#Answer:
days = int(input("Enter the number of days: "))

years = days // 360 
months = (days - years*360) // 30
rem_days = days - (years * 360) - (months*30)

print(int(years),int(months),int(rem_days))