
def scrap(lines: list, symbs: list):   
    new_list = []
    
    for line in lines:
        deleteLine = False

        for symb in symbs:
            idx = line.find(symb)
            if idx >= 0:
                line = line[:idx]
                if idx == 0:
                    deleteLine = True

        if not deleteLine:
            new_list.append(line)

    
    return new_list
    
    