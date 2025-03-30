def filter_data(df, nombre, curso, start_date, end_date):
    filtered_df = df.copy()
    if nombre:
        filtered_df = filtered_df[filtered_df['Nombres'].str.contains(nombre, case=False)]
    if curso != 'Todos':
        filtered_df = filtered_df[filtered_df['Curso'] == curso]
    filtered_df = filtered_df[(filtered_df['Fecha Pago'] >= start_date) & (filtered_df['Fecha Pago'] <= end_date)]
    return filtered_df