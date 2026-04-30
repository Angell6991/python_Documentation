#!/bin/bash

# compilar and view document latex
# pdflatex principal.tex && zathura principal.pdf &

document_latex="$1"

if [ -z "$document_latex" ]; then
    echo "Uso: $0 archivo.tex"
    exit 1
fi

# Ejecutar latexmk y analizar salida en tiempo real
latexmk -pvc -pdf -synctex=1 -interaction=nonstopmode "$document_latex" 2>&1 | while read -r line
do
    echo "$line"

    # Detectar errores típicos de LaTeX
    if echo "$line" | grep -E -q "^!|Error|Missing \$|Runaway argument|Failure"; then
        notify-send "LaTeX" "Compilation error"
    fi
done
