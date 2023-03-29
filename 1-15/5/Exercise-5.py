# Solution 1

def swap_elements(new_list, pos1, pos2):
    temp = new_list[pos1]
    new_list[pos1] = new_list[pos2]
    new_list[pos2] = temp
    return new_list


# Solution 2

def swap_elements(new_list, pos1, pos2):
    (new_list[pos1], new_list[pos2]) = (new_list[pos2], new_list[pos1])
    return new_list