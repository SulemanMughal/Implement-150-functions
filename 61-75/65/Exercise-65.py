def mse(y_true, y_pred):
    return round(
        sum([(i[1] - i[0]) ** 2 for i in zip(y_true, y_pred)])
        / len(y_true),
        3,
    )