import calendar
import datetime

report_date = datetime.date.today()
print(f"Report Date: {report_date}")
print("Calendar for the current month:")
year = report_date.year
month = report_date.month
cal = calendar.month(year, month)
print(cal)
                                    