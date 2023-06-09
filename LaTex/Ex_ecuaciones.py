from sympy import*
from pylatex import*
from pylatex.utils import*
import os

os.system("clear")

var =   ["x","y","z"]
var =   symbols(var)
n   =   len(var)
A   =   [[var[0]**2,0,0],[0,var[1]**2,0],[0,0,var[2]**2]]
A   =   Array(A)
B   =   []

for i in range(n):
    B.append(diff(A, var[i]))

#-------------------------#
print(A)
print()
for i in range(n):
    print(B[i])

#-------------------------#
Alatex  =   latex(A)
Blatex  =   []

for i in range(n):
    Blatex.append(latex(B[i])) 



#------creando_pdf--------#
doc     =   Document()

with doc.create(Section('Sección 1')):
    doc.append('¡Hola, mundo!')
    
    doc.append(Math(data=[NoEscape(Alatex)]))

    for i in range(n):
        doc.append(Math(data=[NoEscape(f"B_{i} = " + Blatex[i])]))

doc.generate_pdf("Doc_LaTex", clean_tex=True)
os.system("zathura Doc_LaTex.pdf &")

