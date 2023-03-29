def generate_sql(table_name, col_names, constraints):
    cols = [
        " ".join((col, constraint)).strip()
        for col, constraint in zip(col_names, constraints)
    ]
    return (
        f'CREATE TABLE {table_name} (\n\t'
        + ',\n\t'.join(cols)
        + '\n)'
    )