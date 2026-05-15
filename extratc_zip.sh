#!/bin/bash

### --- unzip   name.zip -d name_save <-  extratc .zip in bash linux

###------- Extract multiple .zip to current directory -------###
for f in *.zip; do  
  unzip -o "$f" -d "${f%.zip}"
done
