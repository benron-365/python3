def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
  
year = 2078

 
if is_leap_year(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


#When you run this program, it will output:
#2077 is not a leap year

#This program uses the following rules to determine if a year is a leap year: 

#- If the year is divisible by 4, it is a leap year, unless...
#- ...the year is also divisible by 100, in which case it is not a leap year, unless...
#- ...the year is also divisible by 400, in which case it is a leap year.

#These rules apply to years in the Gregorian calendar, which is the most widely used calendar in the world.
