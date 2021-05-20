from app_defines import *


class DatetimeOperation:

    def __init__(self):
        print("constructor called for CommonUtil edit ")

    def prepare_dateFromString(self, dateStr):
        #print("Received str for date conversion : ", dateStr)

        new_date = dateStr.split('-')
        new_Year = new_date[0]
        new_Month = new_date[1]
        new_Day = new_date[2]

        date_final = date(int(new_Year), int(new_Month), int(new_Day))
        return date_final

    def isleapYear(self, year):
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        elif year % 4 == 0:
            return True
        else:
            return False

    def calculateNoOfDaysInYear(self, year):
        #print("calculateNoOfDaysInYear->Received year:", str(year))
        noOfDays = 365
        new_year = int(year)
        if self.isleapYear(new_year):
            noOfDays = 366
        print("calculateNoOfDaysInYear ---end")
        return noOfDays

    def calculateNoOfDaysInMonth(self, month_name, year):
        if month_name == "January":
            month = 1;
        elif month_name == "February":
            month = 2;
        elif month_name == "March":
            month = 3;
        elif month_name == "April":
            month = 4;
        elif month_name == "May":
            month = 5;
        elif month_name == "June":
            month = 6;
        elif month_name == "July":
            month = 7;
        elif month_name == "August":
            month = 8;
        elif month_name == "September":
            month = 9;
        elif month_name == "October":
            month = 10;
        elif month_name == "November":
            month = 11;
        elif month_name == "December":
            month = 12;
        else:
            print("calculateNoOfDaysInMonth--> Invalid month")

        print("Received year:", str(year))
        new_year = int(year)
        print("calculateNoOfDaysInMonth ---start")
        return monthrange(new_year, month)[1], month

    def getFromAndToDates_Account_Statement(self, month, year, noOfDays):
        fromDate_Month = month
        fromDate_Year = year

        fromDate = date(int(fromDate_Year), int(fromDate_Month), 1)
        toDate = fromDate + timedelta(noOfDays - 1)

        print("getFromAndToDates_Account_Statement : ", fromDate, toDate)
        return fromDate, toDate

    def fetchMonthName(self, monthNumber):
        print("fetchMonthName for :", monthNumber)
        if monthNumber == 1:
            month_name = "January"
        elif monthNumber == 2:
            month_name = "February"
        elif monthNumber == 3:
            month_name = "March"
        elif monthNumber == 4:
            month_name = "April"
        elif monthNumber == 5:
            month_name = "May"
        elif monthNumber == 6:
            month_name = "June"
        elif monthNumber == 7:
            month_name = "July"
        elif monthNumber == 8:
            month_name = "August"
        elif monthNumber == 9:
            month_name = "September"
        elif monthNumber == 10:
            month_name = "October"
        elif monthNumber == 11:
            month_name = "November"
        elif monthNumber == 12:
            month_name = "December"
        else:
            print("Invalid number")
        return month_name

    def calculate_dayDifference(self, borrowDate, returnDate):
        print("borrowDate: ", borrowDate, " returnDate :", returnDate)

        borrow_time = borrowDate.split('-')
        borrowDay = borrow_time[0]
        borrowMonth = borrow_time[1]
        borrowYear = borrow_time[2]

        borrow_date = date(int(borrowYear), int(borrowMonth), int(borrowDay))

        return_time = returnDate.split('-')
        returnDay = return_time[0]
        returnMonth = return_time[1]
        returnYear = return_time[2]

        return_date = date(int(returnYear), int(returnMonth), int(returnDay))

        delta = return_date - borrow_date
        return delta.days