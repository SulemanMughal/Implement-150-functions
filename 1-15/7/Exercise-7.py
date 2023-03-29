# Solution 1

def remove_common_elements(l1, l2):
    for i in l1[:]:
        if i in l2:
            l1.remove(i)
            l2.remove(i)
    return (l1, l2)



# Solution 2
def remove_common_elements(l1, l2):
    (l1, l2) = (
        [i for i in l1 if i not in l2],
        [j for j in l2 if j not in l1],
    )
    return (l1, l2)