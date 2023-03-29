# Solution 1
def swap_elements(new_list):
    temp = new_list[0]
    new_list[0] = new_list[-1]
    new_list[-1] = temp
    return new_list

# Solution 2
def swap_elements(new_list):
    (new_list[0], new_list[-1]) = (new_list[-1], new_list[0])
    return new_list