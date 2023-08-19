import calendar as  cl
import datetime as  tm
import psutil   as  ps
import os

os.system("clear")

#----------------Batery_info------------------#
inf_batery  =   ps.sensors_battery()
porcent     =   inf_batery.percent
batery      =   int(porcent)

#-----------------Time_info-------------------#
inf_time    =   tm.datetime.now()
fecha       =   inf_time.strftime("%d/%m/%Y")
hora        =   inf_time.strftime("%H:%M")
year        =   inf_time.strftime("%Y")
month       =   inf_time.strftime("%m")

#------------------Day_info-------------------#
inf_cal = cl.TextCalendar(cl.SUNDAY)

mes_0 = inf_cal.formatmonth(int(year), int(month)-1)
mes_1 = inf_cal.formatmonth(int(year), int(month))
mes_2 = inf_cal.formatmonth(int(year), int(month)+1)

#------------------Viw_info-------------------#
print(f"{mes_0} \n {mes_1} \n {mes_2}")
print(f"    {batery}%     {hora}      {fecha}  ")

