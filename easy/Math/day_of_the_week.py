# 1185. Day of the Week

# Given a date, return the corresponding day of the week for that date.

# The input is given as three integers representing the day, month and year respectively.

# Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

# Note: January 1, 1971 was a Friday.

# Example 1:

# Input: day = 31, month = 8, year = 2019
# Output: "Saturday"

# Example 2:

# Input: day = 18, month = 7, year = 1999
# Output: "Sunday"

# Example 3:

# Input: day = 15, month = 8, year = 1993
# Output: "Sunday"
 
# Constraints:

# The given dates are valid dates between the years 1971 and 2100.

# time complexity: O(year-1971) but since the max year could be 2100, it is effectively O(1)
# space complexity: O(1)
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
        weekday = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]

        # covering the years before current date
        days = 0
        for y in range(1971, year):
            if (y%400==0) or (y%4==0 and y%100!=0):
                days+=366
            else:
                days+=365

        for m in range(1, month):
            days+=month_days[m-1]
            # Feb gets an extra day on a leap year
            if m==2 and ((year%400==0) or (year%4==0 and year%100!=0)):
                days+=1
        # Add days in the current month
        # day=1 means 0 days have passed in that month
        days+=day-1

        return weekday[days%7]