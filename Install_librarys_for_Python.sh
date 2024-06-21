#!/bin/bash

#---instalando_librerias---#

echo "Instalando librerias Python:"

sudo pacman -S python-numpy python-sympy python-pandas  python-matplotlib python-scikit-learn python-scipy

pip install pylatex pyinstaller einsteinpy plotly kaleido 

clear

pip list

echo "Instalación completada"
