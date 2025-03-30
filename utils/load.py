import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path)
    df['Pago'] = df['Pago'].astype(str).str.replace(',', '').astype(float)
    df['Fecha Pago'] = pd.to_datetime(df['Fecha Pago'], dayfirst=True)
    return df

def save_new_payment(file_path, nuevo_pago):
    df = pd.read_csv(file_path)
    df['Pago'] = df['Pago'].astype(str).str.replace(',', '').astype(float)
    df['Fecha Pago'] = pd.to_datetime(df['Fecha Pago'], dayfirst=True)
    df = pd.concat([df, pd.DataFrame([nuevo_pago])], ignore_index=True)
    df.to_csv(file_path, index=False)