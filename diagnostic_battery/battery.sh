#!/bin/bash

clear

#   tiempo de duracion 1 hora = 3600 segundos
time_duration=3600

#   time interval 2 minutos = 120 seguntos
delta_time=120

#   mensaje para seleccionar tipo de toma de datos
echo    "selecciona sí la toma de datos se realizara en la carga o descarga de la bateria:"
echo    "select 1 for charge"
echo    "select 2 for discharge"
read    type_data


#   toma de datos carga
if      [ $type_data -eq 1 ];then
    rm  battery_charge/data.dat
    echo    "Taking data..."

    for ((i=0; i<=$time_duration; i=i+$delta_time));
        do
            variable_01=$i
            variable_02=$(cat /sys/class/power_supply/BAT0/capacity)
            echo    "$variable_01;;$variable_02"    >>  battery_charge/data.dat
            sleep   $delta_time
        done

    echo    "Data collection completed"


#   toma de datos descarga
elif    [ $type_data -eq 2 ];then
    rm  battery_discharge/data.dat
    echo    "Taking data..."

    for ((i=0; i<=$time_duration; i=i+$delta_time));
        do
            variable_01=$i
            variable_02=$(cat /sys/class/power_supply/BAT0/capacity)
            echo    "$variable_01;;$variable_02"    >>  battery_discharge/data.dat
            sleep   $delta_time
        done

    echo    "Data collection completed"


#   caso de no seleccionar algun tipo de toma de datos
else
    echo    "opcción no valida, solo se puede digitar 1 ó 2"


fi

