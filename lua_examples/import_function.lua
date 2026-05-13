-- sí function.lua esta dentro de otro dir example modules: modules/function.lua tiene cambiar / por punto de esta forma: 
-- local   fn  =   require("modules.function")

local   fn  =   require("function")

print(fn.sum({1,2,-3}))
