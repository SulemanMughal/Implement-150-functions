def create_mask(l1, l2):
    return [1 if i ==j else 0 for i, j in zip(l1, l2)]