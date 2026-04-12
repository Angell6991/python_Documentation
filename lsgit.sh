#!/bin/bash

###--------------Colores_ANSI--------------###
RED='\033[0;31m'    # color para Changes
GREEN='\033[0;32m'  # color para No changes
NC='\033[0m'        # Sin color "reset color"

###-----------Listar_directorios-----------###
LIST=($(ls -a))

###----------Consulta_cambios_git----------###
for file   in  "${LIST[@]}";  do

    if [[ -d "$file" && -d "$file/.git" ]]; then
        git_inspec=$(git -C "$file" status -s)

        if [[ -n "$git_inspec" ]]; then
            echo -e "$file  ->  ${RED}Changes${NC}"
        else
            echo -e "$file  ->  ${GREEN}No changes${NC}"
        fi
    fi

done


