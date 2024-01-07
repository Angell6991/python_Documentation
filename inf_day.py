import calendar as cl
import datetime as tm
import psutil as ps
import os

os.system("clear")

###############################################
###-------------Battery_info-----------------###
###############################################
inf_battery = ps.sensors_battery()
percent = inf_battery.percent
battery = int(percent)

###############################################
###---------------Time_info-----------------###
###############################################
inf_time = tm.datetime.now()
fecha = inf_time.strftime("%d/%m/%Y")
hora = inf_time.strftime("%H:%M")
year = inf_time.strftime("%Y")
month = inf_time.strftime("%m")

###############################################
###----------------Day_info-----------------###
###############################################
inf_cal = cl.TextCalendar(cl.SUNDAY)

#--------------Previous_Month-----------------#
try:
    prev_month = int(month) - 1
    if prev_month == 0:
        mes_0 = inf_cal.formatmonth(int(year) - 1, 12)
    else:
        mes_0 = inf_cal.formatmonth(int(year), prev_month)
except IndexError:
    mes_0 = inf_cal.formatmonth(int(year) - 1, 12)

#---------------Current_Month-----------------#
mes_1 = inf_cal.formatmonth(int(year), int(month))

#----------------Next_Month-------------------#
try:
    next_month = int(month) + 1
    if next_month == 13:
        mes_2 = inf_cal.formatmonth(int(year) + 1, 1)
    else:
        mes_2 = inf_cal.formatmonth(int(year), next_month)
except IndexError:
    mes_2 = inf_cal.formatmonth(int(year) + 1, 1)

###############################################
###---------------View_info------------------###
###############################################

text_1 = "\033[36m" + f"{mes_0} \n" + "\033[35m" + f"{mes_1} \n" + "\033[36m" + f"{mes_2}"
text_2 = "\033[37m" + " " + "\033[32m" + "  " + "\033[39m" + f"{battery}" + "%" + "\033[37m" + "  " + "\033[32m" + "  " + "\033[39m" + f"{hora}" + "\033[37m" + " " + "\033[32m" + "   " + "\033[39m" + f"{fecha}" + "\033[37m" + " "

print(text_1)
print(text_2)

