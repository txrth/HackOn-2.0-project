import datetime
day =28
year = 2021
month = 5
hour=2
mins = 3

time_string = str(str(day) + "/" + str(month) + "/" + str(year) + " " + str(hour) + ":" + str(mins) + ":00.000")
format_string = "%d/%m/%y %H:%M:%S.%f"

datetime.datetime(year,month,day,hour,mins,0,0)