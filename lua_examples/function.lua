local function sum(data)
    local   total   =   0

    for i = 1, #data do
        total   =   total   +   tonumber(data[i]) 
    end

    return total
end

-- texting function
-- print(sum({1, 2, -1}))

-- pasar como function expotable
return {
    sum =   sum
}

