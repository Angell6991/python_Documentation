io.write("Inserte la un valor de 1 á 10: ")
local   valor   =  tonumber( io.read() )


if  valor   >   10  then
    print("valor mayor que 10")

elseif  valor   ==  10  then
   print("aprovado") 

elseif  valor   >=  6  then
   print("aprovado") 

elseif  valor   >=  5  then
   print("sobresaliente") 

elseif  valor   >=  0   then
    print("reprovado")

else
    print("valor no valido")

end


-- | Operador  |  Signficado
-- | ---------------------------
-- | ==        |  Igualdad 
-- | ~=        |  Diferente 
-- | <         |  Menor que 
-- | <=        |  Menor o igual 
-- | >         |  Mayor que 
-- | >=        |  Mayor o igual 


