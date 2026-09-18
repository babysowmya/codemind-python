from datetime import date
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        a = date(year, month, day).strftime("%A")
        return a
