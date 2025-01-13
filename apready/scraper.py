
def scrap(lines: list, symbs: list):   
    new_list = []

    for line in lines:
        for symb in symbs:
            idx = line.find(symb)
            if idx >= 0:
                pass
    
        new_list.append(line)

    
    return new_list
    
    