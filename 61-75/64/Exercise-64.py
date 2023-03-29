# Solution 1

def mae(y_true, y_pred):
    return round(
        sum([abs(i[1] - i[0]) for i in zip(y_true, y_pred)])
        / len(y_true),
        3,
    )


def mae(y_true, y_pred):
    errors = [abs(i[1] - i[0]) for i in zip(y_true, y_pred)]
    return round(sum(errors) / len(y_true), 3)