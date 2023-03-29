def generate_sql(table_name, col_names):
    return f'CREATE TABLE {table_name} (' + ', '.join(col_names) + ')'