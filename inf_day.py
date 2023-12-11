import calendar as  cl
import datetime as  tm
import psutil   as  ps
import os

os.system("clear")

###############################################
###-------------Batery_info-----------------###
###############################################
inf_batery  =   ps.sensors_battery()
porcent     =   inf_batery.percent
batery      =   int(porcent)

###############################################
###---------------Time_info-----------------###
###############################################
inf_time    =   tm.datetime.now()
fecha       =   inf_time.strftime("%d/%m/%Y")
hora        =   inf_time.strftime("%H:%M")
year        =   inf_time.strftime("%Y")
month       =   inf_time.strftime("%m")

###############################################
###----------------Day_info-----------------###
###############################################
inf_cal = cl.TextCalendar(cl.SUNDAY)

#--------------Previous_Month-----------------#
try:
    mes_0 = inf_cal.formatmonth(int(year), int(month) -1)
except IndexError:
    mes_0 = inf_cal.formatmonth(int(year)-1, 12)

#---------------Current_Month-----------------#
mes_1 = inf_cal.formatmonth(int(year), int(month))

#----------------Next_Month-------------------#
try:
    mes_2 = inf_cal.formatmonth(int(year), int(month) +1)
except IndexError:
    mes_2 = inf_cal.formatmonth(int(year)+1, 1)

###############################################
###---------------Viw_info------------------###
###############################################

text_1  = "\033[36m" + f"{mes_0} \n" + "\033[35m" +  f"{mes_1} \n" + "\033[36m" +  f"{mes_2}"
text_2  = "\033[37m" + " " + "\033[32m"  + "  " + "\033[39m" +  f"{batery}" + "%" + "\033[37m" + "  " + "\033[32m" + "  " + "\033[39m" + f"{hora}" + "\033[37m" + " " + "\033[32m" + "   " + "\033[39m" + f"{fecha}" + "\033[37m" + " "

print(text_1)
print(text_2)


